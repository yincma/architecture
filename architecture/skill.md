---
name: architecture
description: Generate or modify draw.io diagrams from natural language, including flowcharts, architecture diagrams, UML, ER, network topology, mind maps, organization charts, swimlanes, cloud architecture diagrams, and architecture comparison benchmarks.
---

# Architecture Skill

## When To Use

Use this skill when the user asks to create, modify, compare, or benchmark draw.io diagrams, especially for cloud architecture, UML, ER, topology, process flow, or organizational diagrams.

## Core Capabilities

- Generate new `.drawio` files from natural language.
- Modify existing `.drawio` files while preserving untouched content.
- Produce cloud architecture diagrams using AWS, Azure, and GCP icon references.
- Generate architecture comparison outputs: three candidate diagrams plus one benchmark markdown report.

## Supported Diagram Types

- Flowchart
- Architecture Diagram
- UML Class Diagram
- UML Sequence Diagram
- UML State Diagram
- ER Diagram
- Network Topology Diagram
- Mind Map
- Organization Chart
- Swimlane Diagram

## Core Workflow

### Create New Diagram

1. Parse the user's intent, diagram type, nodes, relationships, and layout preferences.
2. If the request is ambiguous, ask for clarification before generating XML.
3. Read the matching template reference only when needed.
4. Generate uncompressed draw.io XML with unique IDs, matching labels, and appropriate layout.
5. Run `scripts/validate_drawio_xml.py` against the generated file and fix any reported errors before finalizing the output.
6. Determine the output file name.
7. Check whether the target file exists.
8. If the file exists and overwrite was not explicitly requested, ask before writing.

### Modify Existing Diagram

1. Read the existing `.drawio` XML.
2. Parse nodes, edges, parent-child hierarchy, and current ID patterns.
3. Apply only the requested add, delete, update, and layout changes.
4. Preserve all untouched IDs, values, styles, geometry, and hierarchy.
5. Run `scripts/validate_drawio_xml.py` against the updated file and fix any reported errors before finalizing the output.
6. Ask before overwriting if writing to an existing new target path.

### Compare Or Benchmark Architectures

1. Clarify system requirements and candidate architecture styles.
2. Confirm three candidate options with the user before producing outputs.
3. Generate one `.drawio` file per option.
4. Generate one benchmark markdown report.
5. Use consistent naming across all options.

## Hard Constraints

These rules must always hold even if no extra references are loaded:

- Output must be uncompressed plain-text draw.io XML.
- The root element must be `<mxfile>`.
- `<root>` must contain `<mxCell id="0"/>` and `<mxCell id="1" parent="0"/>`.
- All IDs must be unique within the diagram.
- Every edge mxCell must include `<mxGeometry relative="1" as="geometry"/>`.
- `vertex="1"` and `edge="1"` are mutually exclusive.
- All vertex nodes with non-empty text must include `whiteSpace=wrap`.
- Containers must include `container=1`.
- Child elements inside containers must use coordinates relative to the parent container.
- `<mxGraphModel>` must include `adaptiveColors="auto"`.
- XML comments are prohibited.
- Special characters in text attributes must be XML-escaped.
- Default routing uses orthogonal edges unless the target diagram type requires another style.
- Coordinates for vertex `x` and `y` must align to multiples of 10.
- If a target file already exists and overwrite was not explicitly requested, confirm before writing.

## Read References As Needed

Load only the references needed for the current task.

- XML rules: `references/xml-rules.md`
- Styles, shapes, edge styles, colors: `references/style-reference.md`
- Flowchart, swimlane, architecture templates: `references/templates-flow-swimlane-architecture.md`
- UML templates: `references/templates-uml.md`
- ER, network topology, mind map, organization chart templates: `references/templates-er-network-mindmap-org.md`
- Cloud icon common rules: `references/cloud-icons-common.md`
- AWS icons: `references/cloud-icons-aws.md`
- Azure icons: `references/cloud-icons-azure.md`
- GCP icons: `references/cloud-icons-gcp.md`
- Containers, routing, spacing, layout: `references/containers-and-layout.md`
- Architecture comparison benchmark details: `references/architecture-benchmark.md`

## Script Helpers

Prefer the bundled scripts when they match the task.

- XML validation: `scripts/validate_drawio_xml.py <file.drawio>`
- Cloud icon lookup: `scripts/lookup_cloud_icon.py <provider> <service name>`
- Prefer `lookup_cloud_icon.py` over manually scanning large provider tables when you only need one concrete service mapping.
- Prefer `validate_drawio_xml.py` after generating or modifying a `.drawio` file so validation is executable rather than purely prompt-based.

## File Naming Rules

- Use `.drawio` for diagram outputs.
- Default naming style is descriptive kebab-case.
- File names use English even if the diagram content is in another language.
- Benchmark report output uses markdown.

## Notes On Migration

- `skill.md` is now the lightweight entry point.
- `skill.original.md` preserves the original full-length source as the baseline backup.
- Detailed templates and specifications now live under `references/`.
- On case-insensitive filesystems, do not rely on both `SKILL.md` and `skill.md` existing separately.
