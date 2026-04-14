#!/usr/bin/env python3
"""Validate draw.io XML files against the skill's hard constraints."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

GRID_RE = re.compile(r"^-?\d+$")
TEXT_TAGS = {"mxCell", "object", "UserObject"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate uncompressed draw.io XML against architecture skill constraints."
    )
    parser.add_argument("file", help="Path to the .drawio XML file")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON instead of plain text.",
    )
    return parser.parse_args()


def add_issue(bucket: list[dict[str, Any]], code: str, message: str, cell_id: str | None = None) -> None:
    item: dict[str, Any] = {"code": code, "message": message}
    if cell_id is not None:
        item["cell_id"] = cell_id
    bucket.append(item)


def parse_with_comment_detection(path: Path) -> tuple[ET.ElementTree | None, bool, str | None]:
    saw_comment = False
    try:
        for event, _elem in ET.iterparse(path, events=("comment",)):
            if event == "comment":
                saw_comment = True
                break
    except ET.ParseError as exc:
        return None, False, str(exc)

    try:
        tree = ET.parse(path)
        return tree, saw_comment, None
    except ET.ParseError as exc:
        return None, saw_comment, str(exc)


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def style_has(style: str | None, needle: str) -> bool:
    if not style:
        return False
    return needle in style


def is_int_string(value: str | None) -> bool:
    return bool(value) and bool(GRID_RE.match(value))


def build_cell_index(root: ET.Element) -> dict[str, ET.Element]:
    cells: dict[str, ET.Element] = {}
    for elem in root.iter():
        if local_name(elem.tag) == "mxCell":
            cell_id = elem.attrib.get("id")
            if cell_id:
                cells[cell_id] = elem
    return cells


def get_value_text(elem: ET.Element) -> str:
    value = elem.attrib.get("value", "")
    return value.strip()


def validate(path: Path) -> dict[str, Any]:
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []

    if not path.exists():
        add_issue(errors, "file_missing", f"File not found: {path}")
        return {"ok": False, "errors": errors, "warnings": warnings}

    raw_text = path.read_text(encoding="utf-8")

    tree, saw_comment, parse_error = parse_with_comment_detection(path)
    if parse_error:
        add_issue(errors, "xml_parse_error", f"XML parse error: {parse_error}")
        return {"ok": False, "errors": errors, "warnings": warnings}

    assert tree is not None
    root = tree.getroot()

    if local_name(root.tag) != "mxfile":
        add_issue(errors, "root_not_mxfile", "Root element must be <mxfile>.")

    diagram = None
    graph_model = None
    xml_root = None

    for elem in root.iter():
        name = local_name(elem.tag)
        if name == "diagram" and diagram is None:
            diagram = elem
        elif name == "mxGraphModel" and graph_model is None:
            graph_model = elem
        elif name == "root" and xml_root is None:
            xml_root = elem

    if diagram is None:
        add_issue(errors, "missing_diagram", "Missing <diagram> element.")
    if graph_model is None:
        add_issue(errors, "missing_graph_model", "Missing <mxGraphModel> element.")
    if xml_root is None:
        add_issue(errors, "missing_root", "Missing <root> element inside <mxGraphModel>.")
        return {"ok": False, "errors": errors, "warnings": warnings}

    if saw_comment or "<!--" in raw_text:
        add_issue(errors, "xml_comment_present", "XML comments are prohibited.")

    if graph_model is not None and graph_model.attrib.get("adaptiveColors") != "auto":
        add_issue(errors, "missing_adaptive_colors", '<mxGraphModel> must include adaptiveColors="auto".')

    cells = build_cell_index(xml_root)

    if "0" not in cells:
        add_issue(errors, "missing_cell_0", 'Missing structural cell <mxCell id="0"/>.')
    if "1" not in cells:
        add_issue(errors, "missing_cell_1", 'Missing structural cell <mxCell id="1" parent="0"/>.')
    elif cells["1"].attrib.get("parent") != "0":
        add_issue(errors, "invalid_cell_1_parent", 'Structural cell id="1" must have parent="0".')

    all_ids: list[str] = []
    for elem in xml_root.iter():
        elem_id = elem.attrib.get("id")
        if elem_id:
            all_ids.append(elem_id)
    seen: set[str] = set()
    duplicates: set[str] = set()
    for elem_id in all_ids:
        if elem_id in seen:
            duplicates.add(elem_id)
        seen.add(elem_id)
    for dup in sorted(duplicates):
        add_issue(errors, "duplicate_id", f"Duplicate id found: {dup}", dup)

    parent_to_children: dict[str, list[ET.Element]] = {}
    for cell_id, cell in cells.items():
        parent_id = cell.attrib.get("parent")
        if parent_id:
            parent_to_children.setdefault(parent_id, []).append(cell)

    for cell_id, cell in cells.items():
        is_vertex = cell.attrib.get("vertex") == "1"
        is_edge = cell.attrib.get("edge") == "1"
        style = cell.attrib.get("style", "")

        if is_vertex and is_edge:
            add_issue(errors, "vertex_edge_conflict", "Cell cannot be both vertex and edge.", cell_id)

        if is_edge:
            geometry = None
            for child in list(cell):
                if local_name(child.tag) == "mxGeometry":
                    geometry = child
                    break
            if geometry is None:
                add_issue(errors, "edge_missing_geometry", "Edge cell is missing <mxGeometry> child.", cell_id)
            elif geometry.attrib.get("relative") != "1" or geometry.attrib.get("as") != "geometry":
                add_issue(
                    errors,
                    "edge_invalid_geometry",
                    'Edge geometry must be <mxGeometry relative="1" as="geometry"/>.',
                    cell_id,
                )

        if is_vertex:
            value = get_value_text(cell)
            if value and not style_has(style, "whiteSpace=wrap"):
                add_issue(
                    errors,
                    "missing_white_space_wrap",
                    'Text vertex must include style fragment "whiteSpace=wrap".',
                    cell_id,
                )

            geometry = None
            for child in list(cell):
                if local_name(child.tag) == "mxGeometry":
                    geometry = child
                    break
            if geometry is None:
                add_issue(errors, "vertex_missing_geometry", "Vertex cell is missing <mxGeometry> child.", cell_id)
            else:
                for axis in ("x", "y"):
                    value_str = geometry.attrib.get(axis)
                    if value_str is not None:
                        if not is_int_string(value_str):
                            add_issue(errors, "non_integer_coordinate", f"Vertex {axis} must be an integer.", cell_id)
                        elif int(value_str) % 10 != 0:
                            add_issue(errors, "grid_misalignment", f"Vertex {axis} must align to multiples of 10.", cell_id)

        if cell_id in parent_to_children and cell_id not in {"0", "1"}:
            if not style_has(style, "container=1"):
                add_issue(errors, "missing_container_flag", 'Parent cell with children must include "container=1".', cell_id)
            for child in parent_to_children[cell_id]:
                geometry = None
                for grandchild in list(child):
                    if local_name(grandchild.tag) == "mxGeometry":
                        geometry = grandchild
                        break
                if geometry is None:
                    continue
                x = geometry.attrib.get("x")
                y = geometry.attrib.get("y")
                if x is None and y is None:
                    add_issue(
                        warnings,
                        "child_relative_coordinates_unclear",
                        "Child element under container has no x/y geometry; verify relative placement manually.",
                        child.attrib.get("id"),
                    )

    if "%3CmxGraphModel" in raw_text or "%3cmxgraphmodel" in raw_text:
        add_issue(errors, "encoded_diagram_payload", "Encoded diagram payload detected; output must be plain-text XML.")
    if "compressed=" in raw_text:
        add_issue(warnings, "compressed_attribute_present", "Compressed attribute found; verify file is not using compressed diagram payloads.")

    ok = not errors
    return {"ok": ok, "errors": errors, "warnings": warnings}


def emit_text(report: dict[str, Any], path: Path) -> int:
    status = "PASS" if report["ok"] else "FAIL"
    print(f"{status}: {path}")
    if report["errors"]:
        print("Errors:")
        for item in report["errors"]:
            suffix = f" [cell={item['cell_id']}]" if "cell_id" in item else ""
            print(f"- {item['code']}: {item['message']}{suffix}")
    if report["warnings"]:
        print("Warnings:")
        for item in report["warnings"]:
            suffix = f" [cell={item['cell_id']}]" if "cell_id" in item else ""
            print(f"- {item['code']}: {item['message']}{suffix}")
    return 0 if report["ok"] else 1


def main() -> int:
    args = parse_args()
    path = Path(args.file)
    report = validate(path)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["ok"] else 1
    return emit_text(report, path)


if __name__ == "__main__":
    raise SystemExit(main())
