#!/usr/bin/env python3
"""Look up cloud icon styles from the split markdown references."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REFERENCE_FILES = {
    "aws": "cloud-icons-aws.md",
    "azure": "cloud-icons-azure.md",
    "gcp": "cloud-icons-gcp.md",
}

DEFAULT_STYLE_SUFFIX = (
    "whiteSpace=wrap;html=1;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Look up a cloud icon style fragment from the architecture skill references."
    )
    parser.add_argument("provider", choices=sorted(REFERENCE_FILES), help="Cloud provider")
    parser.add_argument("service", nargs="+", help="Service display name, e.g. 'Bedrock' or 'Virtual Machine'")
    parser.add_argument(
        "--format",
        choices=["json", "style", "fragment"],
        default="json",
        help="Output format. 'style' includes the standard label/layout suffix; 'fragment' returns the raw style from the table.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all services for the provider instead of performing a lookup.",
    )
    return parser.parse_args()


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def reference_path(provider: str) -> Path:
    base = Path(__file__).resolve().parent.parent / "references"
    return base / REFERENCE_FILES[provider]


def parse_reference(provider: str) -> list[dict[str, Any]]:
    path = reference_path(provider)
    services: list[dict[str, Any]] = []
    current_category = ""

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("#### "):
            current_category = line[5:].strip()
            continue
        if not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) != 3:
            continue
        if parts[0] in {"Service", "Service Category"}:
            continue
        if set(parts[0]) == {"-"}:
            continue
        service, style_cell, description = parts
        style = style_cell.strip("`")
        if not style.startswith("shape="):
            continue
        services.append(
            {
                "provider": provider,
                "category": current_category,
                "service": service,
                "style_fragment": style,
                "description": description,
            }
        )
    return services


def resolve(provider: str, service_name: str) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    services = parse_reference(provider)
    target = normalize(service_name)
    exact = [item for item in services if normalize(item["service"]) == target]
    if exact:
        return exact[0], []
    partial = [item for item in services if target and target in normalize(item["service"])]
    return None, partial


def render_style(item: dict[str, Any]) -> str:
    style = item["style_fragment"]
    if "whiteSpace=wrap" in style:
        return style
    return f"{style}{DEFAULT_STYLE_SUFFIX}"


def main() -> int:
    args = parse_args()
    provider = args.provider
    services = parse_reference(provider)

    if args.list:
        payload = [item["service"] for item in services]
        if args.format == "json":
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print("\n".join(payload))
        return 0

    service_name = " ".join(args.service)
    item, suggestions = resolve(provider, service_name)
    if item is None:
        message = {
            "ok": False,
            "provider": provider,
            "service": service_name,
            "suggestions": [entry["service"] for entry in suggestions[:10]],
        }
        if args.format == "json":
            print(json.dumps(message, ensure_ascii=False, indent=2))
        else:
            print(f"No exact match for {service_name!r} in provider {provider}.")
            if suggestions:
                print("Suggestions:")
                for entry in suggestions[:10]:
                    print(f"- {entry['service']}")
        return 1

    payload = {
        "ok": True,
        "provider": item["provider"],
        "category": item["category"],
        "service": item["service"],
        "description": item["description"],
        "style_fragment": item["style_fragment"],
        "style": render_style(item),
    }

    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    elif args.format == "fragment":
        print(item["style_fragment"])
    else:
        print(render_style(item))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
