# Architecture Diagram Skill

## 1. Overview & Activation

### Purpose

This Skill gives AI agents professional draw.io diagram generation, modification, validation, and optional export capabilities. Once activated, the AI agent can:

- Generate uncompressed plain-text `.drawio` files from natural language descriptions
- Read and modify existing `.drawio` files while preserving unchanged content
- Produce cleaner diagrams by planning layout before writing XML
- Use listed draw.io cloud stencil styles for AWS, Azure, GCP, and generic architecture diagrams, with safe fallback when an icon is unlisted
- Produce architecture comparison diagrams and benchmark reports when explicitly requested
- Export generated diagrams to PNG, SVG, or PDF when a compatible draw.io CLI is available

### Activation

Activate this Skill when a user requests generation, modification, comparison, validation, or export of draw.io diagrams:

```text
discloseContext("architecture")
```

### Supported Diagram Types

This Skill supports flowcharts, architecture diagrams, UML class diagrams, UML sequence diagrams, UML state diagrams, ER diagrams, network topology diagrams, mind maps, organization charts, and swimlane diagrams.

### Tool Usage

| Operation | Tool | Description |
|---|---|---|
| Read existing diagram | `readFile` or filesystem read | Read complete XML content of a `.drawio` file |
| Write new or updated diagram | `fsWrite` or filesystem write | Write complete validated XML |
| Precise one-off replacement | `strReplace` | Use only when the target XML fragment is unique and the change is local |
| Check file existence | `fileSearch` / `listDirectory` / filesystem check | Avoid accidental overwrite |
| Validate generated output | `python tools/validate_drawio.py <file.drawio>` | Validate XML structure and draw.io compatibility |
| Export optional formats | draw.io Desktop CLI, when available | Export `.drawio` to `.drawio.png`, `.drawio.svg`, or `.drawio.pdf` |

## 2. Progressive References

Keep this file loaded as the workflow controller. Read reference files only when needed.

| Need | Read |
|---|---|
| XML structure, mxCell rules, escaping, dark mode, compliance checklist | `references/xml-spec.md` |
| Shape styles, edge styles, color schemes, text wrapping | `references/styles.md` |
| Layout-first planning, readability checks, audience modes | `references/layout-quality.md` |
| Containers, grouping, child coordinates, edge routing, spacing | `references/containers-layout.md` |
| Diagram type selection and template index | `references/templates/index.md` |
| Specific XML examples | One file under `references/templates/`, such as `architecture.md` or `uml-sequence.md` |
| Cloud icon rules and provider index | `references/cloud-icons/index.md` |
| AWS icon rules and identifiers | `references/cloud-icons/aws.md` |
| Azure icon rules and identifiers | `references/cloud-icons/azure.md` |
| GCP icon rules and identifiers | `references/cloud-icons/gcp.md` |
| Export to PNG/SVG/PDF | `references/export.md` |
| Multi-option architecture comparisons and benchmark reports | `references/architecture-benchmark.md` |

### Reference Loading Rules

1. Always read `references/xml-spec.md`, `references/styles.md`, and `references/layout-quality.md` before generating or modifying XML.
2. Read only the template file for the requested diagram type. Do not load every template by default.
3. For cloud diagrams, read `references/cloud-icons/index.md` and only the provider file that is needed.
4. Never guess cloud icon shape names. If an exact icon is not listed, use a generic rounded rectangle or cloud/service shape with the service name.
5. For diagrams with nested groups, networks, swimlanes, cloud boundaries, or many edges, read `references/containers-layout.md`.

## 3. Core Principles

### Layout First, XML Second

Do not generate XML directly from the user's natural language request. First create an internal layout plan, then generate XML from the plan.

The internal layout plan must include:

1. **Diagram intent** — diagram type, target audience, reading direction, and output format.
2. **Canvas plan** — page size, background, title area, legend area, and main drawing area.
3. **Container hierarchy** — parent ID for each container and node.
4. **Node table** — id, label, semantic role, parent, x, y, width, height, style category, and whether it is a container.
5. **Edge table** — id, source, target, label, flow type, line style, exit/entry points, and waypoints when needed.
6. **Quality pass** — overlap check, spacing check, edge crossing check, label readability check, and export-readiness check.

Generate XML only after the internal layout plan is consistent.

### Ask Only When It Changes the Diagram

If the request is underspecified, ask only for missing decisions that materially change the diagram, such as diagram type, required elements, or key relationships. Otherwise, make reasonable assumptions and state them briefly in the final response.

### Audience-Aware Output

- For technical audiences, use precise service names, protocol labels, and detailed component boundaries.
- For executives or non-technical audiences, use shorter labels, numbered flows, fewer implementation details, and a legend.
- For mixed audiences, keep the diagram clean and provide technical detail in labels only where it helps understanding.

## 4. Workflows

### Create New Diagram

1. Parse the user's intent: diagram type, nodes/entities, relationships, direction, layout preference, audience, target filename, and whether cloud icons or export formats are required.
2. Read the required references from Section 2.
3. Create the internal layout plan described in Section 3.
4. Run the visual quality self-check from Section 6 before writing XML.
5. Generate a complete uncompressed `.drawio` XML document using semantic shapes, consistent colors for same-type elements, orthogonal edges by default, grid-aligned top-level coordinates, and labels in the user's input language.
6. If no filename is provided, generate an English kebab-case `.drawio` filename such as `auth-flow.drawio` or `system-architecture.drawio`.
7. Before writing, check whether the target file exists. If it exists and the user did not explicitly request overwrite, choose a non-conflicting filename such as `system-architecture-v2.drawio` unless the working environment requires explicit confirmation.
8. Write the file, then run the validation workflow in Section 7.
9. If the user requested PNG, SVG, or PDF, follow `references/export.md` after the `.drawio` file validates.

### Modify Existing Diagram

1. Read the full existing `.drawio` file and parse its XML structure: vertices, edges, parents, containers, IDs, styles, geometry, and waypoints.
2. Identify the requested add/delete/update/layout changes.
3. Preserve all unmodified IDs, values, styles, geometry, routes, waypoints, and container hierarchy.
4. If the change affects layout, create an internal update plan that includes before/after positions and affected edges.
5. Prefer parsing and writing the complete XML back. Use `strReplace` only for a single, unique XML fragment where a partial replacement is safer and easier to audit.
6. When deleting a node, also remove edges whose `source` or `target` points to it.
7. Write back to the original file unless the user supplied a new path. For a new target path, apply the same overwrite rule as creation.
8. Run the validation workflow in Section 7.
9. If the user requested export formats, follow `references/export.md`.

### Architecture Comparison

Use the benchmark workflow only when the user explicitly asks to compare architecture approaches, benchmark options, evaluate trade-offs, or choose between multiple solution designs. Read `references/architecture-benchmark.md`, generate one `.drawio` file per option, and create the companion Markdown benchmark report.

### Export Existing or Newly Generated Diagram

Use `references/export.md` when the user asks for PNG, SVG, PDF, or another rendered format. Always validate the `.drawio` file first. If a compatible draw.io CLI is unavailable, provide the `.drawio` file and clearly state that rendered export was not performed.

## 5. Required XML Self-Check

Before outputting or writing any `.drawio` XML, verify all of these requirements:

1. Root element is `<mxfile>`.
2. `<root>` contains `<mxCell id="0"/>` and `<mxCell id="1" parent="0"/>`.
3. All `mxCell`, `object`, and `UserObject` IDs are unique within the same diagram.
4. Every `edge="1"` mxCell contains `<mxGeometry relative="1" as="geometry"/>`.
5. No mxCell has both `vertex="1"` and `edge="1"`.
6. Generated XML contains no XML comments.
7. Special characters in text attributes are escaped: `&amp;`, `&lt;`, `&gt;`, `&quot;`.
8. Top-level and ordinary vertex `x` and `y` coordinates align to multiples of 10. Exception: internal rows inside UML/ER table-like containers, sequence activation boxes, lifeline markers, and other semantic micro-layout elements may use non-10px values when needed for precise visual alignment.
9. `mxGraphModel` includes `adaptiveColors="auto"`.
10. Vertex mxCells with non-empty text include `whiteSpace=wrap` in their style unless the shape is a tiny marker that intentionally has no text wrapping.
11. mxCells acting as parent containers include `container=1`.
12. Child elements inside containers use coordinates relative to the parent container's top-left corner.
13. Cloud icon styles use listed provider references only; unlisted services fall back to generic shapes rather than invented `mxgraph.*` names.

## 6. Diagram Quality Self-Check

Before writing XML, verify the diagram's visual quality:

1. The diagram has a clear reading direction: left-to-right, top-to-bottom, radial, swimlane, or layered.
2. Related components are grouped into containers, zones, layers, swimlanes, or cloud boundaries.
3. No two sibling vertices overlap.
4. Sibling vertices keep at least 60px spacing, except for table rows or compact UML/ER internals.
5. Major edges mostly follow the main reading direction.
6. Edge crossings are minimized; use waypoints when needed.
7. Edges entering the same node use distributed entry points.
8. Important flows have labels; trivial edges may omit labels.
9. The diagram includes a title unless the user requested otherwise or the filename/context makes it redundant.
10. Architecture diagrams include a legend when colors, line styles, numbered flows, or trust boundaries carry meaning.
11. Cloud diagrams use listed or externally verified icon references when available.
12. External actors/systems are visually distinct from internal components.
13. Async, sync, data, and control flows use distinguishable line styles when multiple flow types are present.
14. Long labels are shortened, wrapped, or moved into a companion guide.
15. The output fits the declared page size and remains readable after PNG/SVG/PDF export.

## 7. Post-Generation Validation

After creating or modifying a diagram, validate the file from the repository root when this Skill package's Python validator is available:

```bash
python tools/validate_drawio.py <file.drawio>
```

If validation reports errors, fix the XML and rerun validation before presenting the result. If no automated validator is available, perform the Section 5 and Section 6 self-checks manually and clearly state that automated validation was unavailable.

## 8. File Naming

| Rule | Description |
|---|---|
| Native format | `{descriptive-name}.drawio` |
| Exported PNG | `{descriptive-name}.drawio.png` |
| Exported SVG | `{descriptive-name}.drawio.svg` |
| Exported PDF | `{descriptive-name}.drawio.pdf` |
| Naming style | English kebab-case |
| User-specified name | Use exactly as requested, adding `.drawio` only when appropriate |
| Auto-generated examples | `auth-flow.drawio`, `system-architecture.drawio`, `user-service-class-diagram.drawio`, `order-process-swimlane.drawio`, `aws-vpc-topology.drawio` |
