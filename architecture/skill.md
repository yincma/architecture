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
4. **MANDATORY**: Read `references/containers-and-layout.md` for any diagram that has more than 3 nodes or any edge connections. This file contains critical edge routing, spacing, and connection point distribution rules that prevent line overlap.
5. Generate uncompressed draw.io XML with unique IDs, matching labels, and appropriate layout. Apply the Layout Quality Rules below during generation.
6. Run `scripts/validate_drawio_xml.py` against the generated file and fix any reported errors before finalizing the output.
7. Determine the output file name.
8. Check whether the target file exists.
9. If the file exists and overwrite was not explicitly requested, ask before writing.

### Modify Existing Diagram

1. Read the existing `.drawio` XML.
2. Parse nodes, edges, parent-child hierarchy, and current ID patterns.
3. Apply only the requested add, delete, update, and layout changes.
4. Preserve all untouched IDs, values, styles, geometry, and hierarchy.
5. **MANDATORY**: Re-apply the Layout Quality Rules below to all affected edges after modification.
6. Run `scripts/validate_drawio_xml.py` against the updated file and fix any reported errors before finalizing the output.
7. Ask before overwriting if writing to an existing new target path.

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

## Layout Quality Rules (MANDATORY — Always Apply)

These rules prevent line overlap, crossing, and visual clutter. They are as important as the structural Hard Constraints above and must be applied during every diagram generation or modification.

### Spacing Rules

- **Minimum spacing**: The gap between bounding boxes of any two sibling vertex nodes must be at least **60px**.
- **Recommended horizontal spacing**: **200px** between horizontally adjacent nodes.
- **Recommended vertical spacing**: **120px** between vertically adjacent nodes.
- All vertex `x` and `y` coordinates must be multiples of 10.

### Connection Point Distribution Strategy

When multiple edges connect to the same node, use `exitX/Y` and `entryX/Y` to distribute connection points across different positions on the node boundary. This is the single most important rule for preventing line overlap.

```
    (0,0)──(0.25,0)──(0.5,0)──(0.75,0)──(1,0)
      │                                    │
   (0,0.25)                            (1,0.25)
      │                                    │
   (0,0.5)          Node Center         (1,0.5)
      │                                    │
   (0,0.75)                            (1,0.75)
      │                                    │
    (0,1)──(0.25,1)──(0.5,1)──(0.75,1)──(1,1)
```

Distribution rules:
1. **Single edge on a side**: Use the center point (e.g., `exitX=0.5;exitY=1`).
2. **Two edges on the same side**: Use `0.25` and `0.75` positions.
3. **Three or more edges on the same side**: Evenly distribute (e.g., `0.2`, `0.5`, `0.8`).
4. **Prefer different sides**: If edges go in different directions, assign them to different sides of the node (top, bottom, left, right).

Example — two edges exiting the right side of Node A:
```xml
<mxCell id="edge-ab" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.25;entryX=0;entryY=0.5;"
        edge="1" parent="1" source="node-a" target="node-b">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="edge-ac" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.75;entryX=0;entryY=0.5;"
        edge="1" parent="1" source="node-a" target="node-c">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Final Straight Segment Rule

The final straight segment of a connection line (between the last bend and the target node) must be at least **20px** long so the arrow renders cleanly without overlapping the node border.

### Explicit Waypoints for Overlap Avoidance

When automatic routing would cause edges to overlap or cross through intermediate nodes, add explicit waypoints:

```xml
<mxCell id="edge-bypass" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;"
        edge="1" parent="1" source="node-a" target="node-b">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="280" y="250"/>
      <mxPoint x="540" y="250"/>
    </Array>
  </mxGeometry>
</mxCell>
```

Waypoint rules:
- Coordinates use canvas absolute values (not affected by containers).
- Align to multiples of 10.
- Use the minimum number of waypoints needed.
- For parallel edges between the same pair of nodes, stagger waypoints by at least 30px vertically or horizontally.

### Self-Check Before Output

After generating all XML, verify these layout items in addition to the structural checklist:
1. No two edges share the same exit point on any node.
2. No two edges share the same entry point on any node.
3. Every node pair has at least 60px gap between bounding boxes.
4. Edges that would cross intermediate nodes use waypoints to route around them.

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
- Containers, routing, spacing, layout (detailed): `references/containers-and-layout.md`
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
