# Draw.io Diagram Generation Skill

## 1. Overview & Activation

### Purpose

This Skill provides AI agents with professional capabilities for draw.io diagram generation and modification. Once activated, the AI agent can:

- Automatically generate `.drawio` files conforming to draw.io XML specifications based on the user's natural language descriptions
- Read and modify existing `.drawio` files, performing add/delete/update operations while preserving existing content
- Use official architecture icons from AWS, Azure, GCP and other cloud services to generate professional cloud architecture diagrams

### Activation

When a user requests generation or modification of a draw.io diagram, activate this Skill as follows:

```
discloseContext("drawio-diagram")
```

Once activated, the full content of this document is loaded into the AI agent's context, providing knowledge on XML format specifications, style references, diagram templates, and cloud icon libraries.

### Supported Diagram Types

This Skill supports the following 10 common diagram types:

| Diagram Type | Description | Typical Use Cases |
|----------|------|----------|
| Flowchart | Uses rounded rectangles, diamond decisions, ellipse start/end nodes | Business processes, approval workflows, algorithm logic |
| Architecture Diagram | System components and their interactions | System design, microservice architecture |
| UML Class Diagram | Rectangles with dividers (class name, attributes, methods) | Object-oriented design, domain models |
| UML Sequence Diagram | Lifelines, messages, activation boxes | Interface interactions, message passing flows |
| UML State Diagram | State nodes, transitions, initial/final states | State machine design, lifecycle management |
| ER Diagram | Entity rectangles, PK/FK annotations, relationship lines with cardinality | Database design, data modeling |
| Network Topology Diagram | Network devices and their connections | Network architecture, infrastructure planning |
| Mind Map | Tree structure radiating outward from a central topic | Brainstorming, knowledge organization |
| Organization Chart | Hierarchical organizational structure | Team structure, reporting relationships |
| Swimlane Diagram | Uses swimlane containers to divide responsibility areas | Cross-department processes, responsibility allocation |

### Core Capabilities

1. **Natural Language Understanding**: Analyzes user descriptions, automatically identifies diagram types, and extracts nodes, relationships, and layout information
2. **XML Generation**: Generates uncompressed plain-text XML conforming to draw.io official specifications, directly openable in the draw.io editor
3. **Cloud Architecture Icons**: Built-in style references for commonly used service icons from AWS (`mxgraph.aws4.*`), Azure (`mxgraph.azure.*`), and GCP (`mxgraph.gcp2.*`)
4. **Diagram Modification**: Reads existing `.drawio` files and performs precise add/delete/update operations while preserving unmodified parts
5. **Style Consistency**: Uses consistent color schemes for elements of the same type, supports dark mode adaptation (`adaptiveColors="auto"`)
6. **Layout Standards**: Nodes aligned to a grid of multiples of 10, maintains proper spacing, connection lines use orthogonal routing

### Tool Usage

The AI agent uses the following Kiro tools to operate on files under the guidance of this Skill:

| Operation | Tool | Description |
|------|------|------|
| Read existing diagram | `readFile` | Read the XML content of a `.drawio` file |
| Write new diagram | `fsWrite` | Write generated XML to a `.drawio` file |
| Partially modify diagram | `strReplace` | Perform precise partial replacements on existing XML |
| Check if file exists | `fileSearch` / `listDirectory` | Avoid accidentally overwriting existing files |

## 2. Workflows (Create / Modify)

### 2.1 Create New Diagram Workflow

When a user requests creation of a new draw.io diagram, follow these steps:

**Step 1: Parse User Intent**
- Analyze the user's natural language description and extract key information:
  - Diagram type (flowchart, architecture diagram, UML class diagram, sequence diagram, ER diagram, etc.)
  - Nodes/entities and their names
  - Relationships and connection directions between nodes
  - Layout preferences (horizontal/vertical, hierarchical structure, etc.)
- If the description is vague or unclear, ask the user to clarify the diagram type, elements, and relationships

**Step 2: Select Diagram Type & Template**
- Based on the parsed results, select the corresponding template from Section 5 "Diagram Type Templates" as a reference skeleton
- If the user's description involves cloud service components, also refer to Section 6 "Cloud Architecture Icon Reference" to select the correct icon styles

**Step 3: Generate XML Content**
- Using the template as a base, populate specific nodes, edges, and styles according to the user's description:
  - Create a `vertex` type `mxCell` for each node, selecting semantically correct shapes
  - Create an `edge` type `mxCell` for each connection line, setting `source` and `target`
  - Assign unique IDs to all elements (use meaningful prefix + incremental number, e.g., `node-1`, `edge-1`)
  - Set styles and coordinates according to Section 4 "Style Attribute Reference" and Section 8 "Edge Routing & Layout Guidelines"
- Ensure diagram label language matches the user's input language

**Step 4: Perform XML Self-Check**
- Before output, verify the generated XML item by item against the Section 3 "XML Compliance Checklist":
  1. Root element is `<mxfile>`
  2. Contains `<mxCell id="0"/>` and `<mxCell id="1" parent="0"/>`
  3. All IDs are unique
  4. Every edge mxCell contains `<mxGeometry relative="1" as="geometry"/>`
  5. vertex and edge attributes are mutually exclusive
  6. No XML comments
  7. Special characters are escaped (`&amp;`, `&lt;`, `&gt;`, `&quot;`)
  8. Coordinates are aligned to multiples of 10
  9. `mxGraphModel` contains `adaptiveColors="auto"`
  10. Nodes containing text have `whiteSpace=wrap`
  11. Containers have the `container=1` attribute
  12. Child elements use coordinates relative to the parent container
- If issues are found, fix them immediately before output

**Step 5: Determine File Name**
- If the user specified a file name, use the user-specified file name
- If the user did not specify a file name, automatically generate a meaningful file name based on diagram content:
  - Use **kebab-case** format (all lowercase, words separated by hyphens)
  - File extension is `.drawio`
  - Examples: `auth-flow.drawio`, `system-architecture.drawio`, `user-service-class-diagram.drawio`

**Step 6: Write File**
- Use `fileSearch` or `listDirectory` to check if the target file already exists
- **If the target file already exists and the user has not explicitly requested overwriting**: Prompt the user to confirm whether to overwrite, and wait for user confirmation before writing
- Use `fsWrite` to write the generated XML to the `.drawio` file

### 2.2 Modify Existing Diagram Workflow

When a user requests modification of an existing `.drawio` file, follow these steps:

**Step 1: Read File**
- The user specifies the `.drawio` file path and modification instructions
- Use `readFile` to read the complete XML content of the file
- If the file does not exist or has an abnormal format, inform the user of the file issue, attempt to repair, or suggest manual inspection

**Step 2: Parse Existing XML Structure**
- Parse the XML structure in the file to understand the current diagram's:
  - All nodes (vertex mxCells) and their positions, styles
  - All connection lines (edge mxCells) and their source/target relationships
  - Container and grouping relationships (parent attribute)
  - Existing ID assignment patterns

**Step 3: Execute Modification Operations**
- Execute add/delete/update operations based on the user's modification instructions:
  - **Add elements**: Create new mxCells, assign unique IDs that do not conflict with existing IDs
  - **Delete elements**: Remove specified mxCells, and also clean up associated edges (edges whose source or target points to the deleted node)
  - **Modify elements**: Update the value, style, or mxGeometry attributes of specified mxCells
  - **Adjust layout**: Re-adjust coordinates of related nodes and connection line routing based on modified elements

**Step 4: Preserve Unmodified Parts**
- **Key principle**: All elements not involved in the modification instructions must remain unchanged
  - Preserve original element IDs, values, and style attributes unchanged
  - Preserve original element mxGeometry (position, dimensions) unchanged
  - Preserve original connection line routing and waypoints unchanged
  - Preserve original container hierarchy unchanged

**Step 5: Perform XML Self-Check**
- Verify the modified complete XML against the same 12-item checklist as the new diagram workflow
- Pay special attention to:
  - New element IDs do not conflict with existing IDs
  - After deleting elements, no dangling edges point to deleted nodes
  - The overall XML structure remains complete and valid after modification

**Step 6: Write Back File**
- By default, use `fsWrite` to write the modified XML back to the original file
- If the user specified a new file path, write to the user-specified new file
- If writing to a new file and the target file already exists, also prompt the user to confirm whether to overwrite

### 2.3 File Naming Rules

| Rule | Description |
|------|------|
| Format | `{descriptive-name}.drawio` |
| Naming Style | **kebab-case** (all lowercase, words separated by `-`) |
| Language | File names use English, even if diagram content is in another language |
| Descriptiveness | File names should reflect diagram content for easy identification |

Examples:

```
auth-flow.drawio              # Authentication flowchart
system-architecture.drawio     # System architecture diagram
user-service-class-diagram.drawio  # User service class diagram
order-process-swimlane.drawio  # Order processing swimlane diagram
aws-vpc-topology.drawio        # AWS VPC network topology diagram
```

### 2.4 File Overwrite Confirmation Logic

```
Before writing a file:
  1. Check if a file already exists at the target path
  2. IF file exists AND user has not explicitly requested overwriting:
     → Prompt user: "Target file {filename} already exists. Overwrite?"
     → Wait for user confirmation
  3. IF user confirms overwrite OR file does not exist OR user explicitly requested overwriting:
     → Execute fsWrite to write the file
  4. IF user declines overwrite:
     → Suggest the user provide a new file name
```

### 2.5 Architecture Comparison & Benchmark Workflow

When a user requests comparing multiple architecture approaches (triggered by keywords like "compare", "benchmark", "evaluate", "pros and cons", "trade-offs", or "which is better"), follow this workflow:

**Step 1: Clarify Requirements & Identify Candidate Architectures**
- Parse the user's description to understand the system requirements (scale, budget, team size, performance needs, etc.)
- Propose 3 distinct architecture approaches. Common combinations include:
  - Monolithic / Microservices / Serverless
  - Self-hosted / Managed services / Hybrid
  - Synchronous / Event-driven / CQRS
  - Single-region / Multi-region / Edge-based
- Confirm the 3 candidates with the user before proceeding

**Step 2: Generate Architecture Diagrams**
- Generate one `.drawio` file per architecture approach
- File naming: `{project}-option-a-{style}.drawio`, `{project}-option-b-{style}.drawio`, `{project}-option-c-{style}.drawio`
  - Example: `order-system-option-a-monolith.drawio`, `order-system-option-b-microservices.drawio`, `order-system-option-c-serverless.drawio`
- Each diagram must follow all XML compliance rules from Section 3
- Use consistent component naming across diagrams for easy comparison

**Step 3: Generate Benchmark Report**
- Output a Markdown file named `{project}-architecture-benchmark.md`
- The report must include:

```markdown
# Architecture Benchmark: {Project Name}

## Overview
Brief description of the system requirements and constraints.

## Candidate Architectures

### Option A: {Architecture Name}
- **Diagram**: `{filename}.drawio`
- **Summary**: 1-2 sentence description

### Option B: {Architecture Name}
- **Diagram**: `{filename}.drawio`
- **Summary**: 1-2 sentence description

### Option C: {Architecture Name}
- **Diagram**: `{filename}.drawio`
- **Summary**: 1-2 sentence description

## Comparison Matrix

| Dimension          | Option A | Option B | Option C |
|--------------------|----------|----------|----------|
| Development Cost   | ⭐⭐⭐⭐⭐  | ⭐⭐⭐      | ⭐⭐⭐⭐    |
| Operational Cost   | ⭐⭐⭐⭐    | ⭐⭐        | ⭐⭐⭐⭐⭐  |
| Scalability        | ⭐⭐       | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐⭐  |
| Performance        | ⭐⭐⭐⭐    | ⭐⭐⭐⭐    | ⭐⭐⭐      |
| Ops Complexity     | ⭐⭐⭐⭐⭐  | ⭐⭐        | ⭐⭐⭐⭐    |
| Team Skill Req.    | ⭐⭐⭐⭐⭐  | ⭐⭐        | ⭐⭐⭐      |
| Time to Market     | ⭐⭐⭐⭐⭐  | ⭐⭐        | ⭐⭐⭐⭐    |
| Fault Isolation    | ⭐⭐       | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐    |

> ⭐ scale: ⭐ = poor, ⭐⭐⭐ = average, ⭐⭐⭐⭐⭐ = excellent

## Detailed Analysis

### Development Cost
{Explain why each option scores as it does}

### Scalability
{Explain scaling characteristics of each option}

... (repeat for each dimension)

## Recommendation
Based on the requirements, **Option X** is recommended because...

### When to Choose Each Option
- **Option A**: Best when {conditions}
- **Option B**: Best when {conditions}
- **Option C**: Best when {conditions}
```

**Step 4: Evaluation Dimensions**
- Use the following default dimensions (can be customized per user request):
  - Development Cost — initial build effort and complexity
  - Operational Cost — ongoing infrastructure and maintenance costs
  - Scalability — ability to handle growth in traffic/data
  - Performance — latency, throughput under normal load
  - Ops Complexity — deployment, monitoring, debugging difficulty
  - Team Skill Requirements — expertise needed to build and maintain
  - Time to Market — speed from design to production
  - Fault Isolation — blast radius when a component fails
- Score each dimension on a 1-5 star scale with justification
- Provide a clear recommendation with reasoning

**Step 5: Output All Files**
- Write all 3 `.drawio` files and 1 `.md` benchmark file
- Summarize the output to the user: list the generated files and the recommended option

## 3. Draw.io XML Format Specification

### 3.1 File Structure

Generated `.drawio` files must use uncompressed plain-text XML format. The use of deflate compression or Base64 encoding is prohibited.

The complete file structure is as follows:

```xml
<mxfile>
  <diagram id="{unique-id}" name="{page-name}">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- Add diagram elements here (comments are prohibited in actual output) -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Hierarchy description:

| Level | Element | Description |
|------|------|------|
| 1 | `<mxfile>` | Root element, must be the outermost element of the XML |
| 2 | `<diagram>` | Diagram page, `id` attribute must be unique, `name` is the page display name |
| 3 | `<mxGraphModel>` | Diagram model, contains canvas configuration attributes, must include `adaptiveColors="auto"` to support dark mode |
| 4 | `<root>` | Container for all graphical elements |
| 5 | `<mxCell>` | Specific graphical elements (nodes or edges) |

`<root>` must contain two structural mxCells:

- `<mxCell id="0"/>` — Root layer, the topmost parent of all elements
- `<mxCell id="1" parent="0"/>` — Default layer, the direct parent of regular graphical elements

### 3.2 mxCell Rules

#### Vertex

Vertices represent shape nodes (rectangles, ellipses, diamonds, etc.). They must include the `vertex="1"` attribute and an `<mxGeometry>` child element:

```xml
<mxCell id="{unique-id}" value="{label}" 
        style="{style-string}" 
        vertex="1" parent="{parent-id}">
  <mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>
</mxCell>
```

Attribute requirements:

| Attribute | Required | Description |
|------|------|------|
| `id` | Yes | Unique identifier, must not be duplicated within the same diagram |
| `value` | Yes | Display text (can be an empty string) |
| `style` | Yes | Style string, `key=value;` format |
| `vertex` | Yes | Must be `"1"` |
| `parent` | Yes | Parent element ID, usually `"1"` (default layer) or a container ID |

`<mxGeometry>` attribute requirements:

| Attribute | Required | Description |
|------|------|------|
| `x` | Yes | X coordinate, must be a multiple of 10 |
| `y` | Yes | Y coordinate, must be a multiple of 10 |
| `width` | Yes | Width (pixels) |
| `height` | Yes | Height (pixels) |
| `as` | Yes | Must be `"geometry"` |

#### Edge

Edges represent connection lines. They must include the `edge="1"` attribute.

> **CRITICAL**: Every edge mxCell must contain a `<mxGeometry relative="1" as="geometry"/>` child element. Self-closing edge elements (without an mxGeometry child element) are invalid in draw.io and will cause connection lines to render incorrectly.

```xml
<mxCell id="{unique-id}" value="{label}" 
        style="{style-string}" 
        edge="1" parent="{parent-id}" 
        source="{source-id}" target="{target-id}">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

Attribute requirements:

| Attribute | Required | Description |
|------|------|------|
| `id` | Yes | Unique identifier, must not be duplicated within the same diagram |
| `value` | No | Label text on the connection line |
| `style` | Yes | Style string, should include `edgeStyle=orthogonalEdgeStyle` |
| `edge` | Yes | Must be `"1"` |
| `parent` | Yes | Parent element ID, usually `"1"` |
| `source` | Recommended | Source node ID |
| `target` | Recommended | Target node ID |

The edge's `<mxGeometry>` must include the `relative="1"` attribute. To add path control points, nest `<Array as="points">` and `<mxPoint>` elements inside `<mxGeometry>`.

#### vertex and edge Are Mutually Exclusive

The `vertex="1"` and `edge="1"` attributes are mutually exclusive; a single mxCell cannot have both attributes simultaneously.

#### ID Uniqueness

All mxCell (including `object` or `UserObject` wrappers) `id` attribute values must be unique within the same `<diagram>`. A meaningful prefix + incremental number naming convention is recommended:

- Nodes: `node-1`, `node-2`, `node-3`
- Edges: `edge-1`, `edge-2`, `edge-3`
- Containers: `container-1`, `container-2`
- Swimlanes: `lane-1`, `lane-2`

### 3.3 Prohibited Rules

#### No XML Comments

Generated XML must not contain any XML comments (`<!-- -->`). draw.io may handle comments inconsistently during parsing; to ensure compatibility, comments are universally prohibited.

#### No Compression or Base64 Encoding

Generated `.drawio` files must use uncompressed plain-text XML. The following formats are prohibited:

- deflate-compressed content
- Base64-encoded content
- Any form of encoding or compression wrapping

The `<diagram>` element's content must directly be an `<mxGraphModel>` child element, not an encoded string.

### 3.4 Special Character Escaping

In the `value` attribute and other text attributes of mxCell, the following special characters must be XML-escaped:

| Original Character | Escaped Form | Description |
|----------|----------|------|
| `&` | `&amp;` | Ampersand |
| `<` | `&lt;` | Less-than sign |
| `>` | `&gt;` | Greater-than sign |
| `"` | `&quot;` | Double quote |

Examples:

- Label text `Input & Output` → `value="Input &amp; Output"`
- Label text `x < 10` → `value="x &lt; 10"`
- Label text `"Hello"` → `value="&quot;Hello&quot;"`

### 3.5 Dark Mode Support

The `<mxGraphModel>` element must include the `adaptiveColors="auto"` attribute to support draw.io's adaptive dark mode. This attribute ensures the diagram displays correctly in both light and dark themes.

```xml
<mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
              tooltips="1" connect="1" arrows="1" fold="1"
              page="1" pageScale="1" pageWidth="850" pageHeight="1100"
              math="0" shadow="0" adaptiveColors="auto">
```

### 3.6 XML Compliance Self-Check Checklist

The AI agent must check the following 12 items before outputting XML:

| # | Check Item | Description |
|---|--------|------|
| 1 | Root element is `<mxfile>` | The outermost XML element must be `<mxfile>` |
| 2 | Contains structural mxCells | `<root>` must contain `<mxCell id="0"/>` and `<mxCell id="1" parent="0"/>` |
| 3 | All IDs are unique | All mxCell `id` attribute values within the same `<diagram>` must not be duplicated |
| 4 | **CRITICAL** Edges contain mxGeometry | Every `edge="1"` mxCell must contain a `<mxGeometry relative="1" as="geometry"/>` child element |
| 5 | vertex and edge are mutually exclusive | A single mxCell cannot have both `vertex="1"` and `edge="1"` |
| 6 | No XML comments | Output must not contain `<!-- -->` comments |
| 7 | Special characters are escaped | `&`, `<`, `>`, `"` in `value` attributes must be escaped to `&amp;`, `&lt;`, `&gt;`, `&quot;` |
| 8 | Coordinates aligned to grid | Vertex `x` and `y` coordinates must be multiples of 10 |
| 9 | `adaptiveColors="auto"` | `<mxGraphModel>` must include this attribute to support dark mode |
| 10 | Text nodes have `whiteSpace=wrap` | All vertex mxCells with non-empty `value` must include `whiteSpace=wrap` in their style |
| 11 | Containers have `container=1` | mxCells acting as parent containers must include `container=1` in their style |
| 12 | Child elements use relative coordinates | Child elements inside containers use coordinates relative to the parent container's top-left corner, not the canvas origin |

## 4. Style Attribute Reference

### 4.1 Style String Format

draw.io style strings use the `key=value;` format, with multiple attributes separated by semicolons. The style string is the value of the `mxCell`'s `style` attribute:

```
rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=14;
```

Rules:
- Each key-value pair ends with a semicolon `;`
- Shape type names (e.g., `ellipse`, `rhombus`) are placed directly as the first value in the style string, without `key=value` format
- Boolean attributes use `1` (enabled) and `0` (disabled)

### 4.2 Common Style Attributes

The following attributes apply to all vertex type mxCells:

| Attribute | Value Type | Default | Description |
|------|--------|--------|------|
| `html` | `1` | — | Enable HTML label rendering, **must be included in all nodes** |
| `whiteSpace` | `wrap` | — | Auto text wrapping, **must be included in all vertex nodes containing text** |
| `rounded` | `0` / `1` | `0` | Rounded rectangle, `1` enables rounded corners |
| `fillColor` | Color value | `#FFFFFF` | Fill color, e.g., `#DAE8FC`, `#D5E8D4` |
| `strokeColor` | Color value | `#000000` | Border color, e.g., `#6C8EBF`, `#82B366` |
| `fontColor` | Color value | `#000000` | Text color, e.g., `#333333` |
| `fontSize` | Number | `12` | Font size (pixels) |
| `fontStyle` | Number | `0` | Font style: `0` normal, `1` bold, `2` italic, `3` bold italic, `4` underline |
| `align` | `left` / `center` / `right` | `center` | Horizontal alignment |
| `verticalAlign` | `top` / `middle` / `bottom` | `middle` | Vertical alignment |
| `overflow` | `hidden` / `fill` / `visible` | `hidden` | Text overflow handling |
| `shadow` | `0` / `1` | `0` | Shadow effect |
| `glass` | `0` / `1` | `0` | Glass effect |
| `sketch` | `0` / `1` | `0` | Hand-drawn style |
| `opacity` | `0`–`100` | `100` | Opacity |
| `arcSize` | Number | `10` | Corner radius (only effective when `rounded=1`) |
| `spacing` | Number | `2` | Padding between text and border |
| `spacingTop` | Number | `0` | Additional top padding |
| `spacingBottom` | Number | `0` | Additional bottom padding |
| `spacingLeft` | Number | `0` | Additional left padding |
| `spacingRight` | Number | `0` | Additional right padding |

> **CRITICAL**: `whiteSpace=wrap` is a **required attribute** for all vertex nodes containing text (non-empty `value`). Missing this attribute will cause long text to overflow node boundaries, affecting diagram readability.

### 4.3 Shape Type Reference

Shape types are specified through style strings. The default shape is a rectangle; other shapes need to be declared in the style string.

#### Basic Shapes

| Shape | Style String | Recommended Size | Typical Use |
|------|-----------|----------|----------|
| Rectangle (default) | `rounded=0;whiteSpace=wrap;html=1;` | 120×60 | General nodes, processing steps |
| Rounded Rectangle | `rounded=1;whiteSpace=wrap;html=1;` | 120×60 | Flowchart steps, service components |
| Ellipse | `ellipse;whiteSpace=wrap;html=1;` | 120×60 | Flowchart start/end nodes |
| Diamond | `rhombus;whiteSpace=wrap;html=1;` | 120×80 | Decision nodes, conditional branching |
| Circle | `ellipse;whiteSpace=wrap;html=1;aspect=fixed;` | 60×60 | State nodes, connection points |
| Triangle | `triangle;whiteSpace=wrap;html=1;` | 60×80 | Direction indicators |
| Hexagon | `shape=hexagon;whiteSpace=wrap;html=1;perimeter=hexagonPerimeter2;` | 120×80 | Preparation steps |
| Parallelogram | `shape=parallelogram;whiteSpace=wrap;html=1;perimeter=parallelogramPerimeter;` | 120×60 | Input/Output |
| Cloud | `ellipse;shape=cloud;whiteSpace=wrap;html=1;` | 120×80 | Cloud services, external systems |
| Cylinder | `shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;size=15;` | 60×80 | Databases, storage |
| Document | `shape=mxgraph.flowchart.document;whiteSpace=wrap;html=1;` | 120×80 | Documents, reports |

#### Container & Grouping Shapes

| Shape | Style String | Typical Use |
|------|-----------|----------|
| Swimlane | `swimlane;startSize=30;whiteSpace=wrap;html=1;container=1;` | Swimlane diagram responsibility areas |
| Horizontal Swimlane | `swimlane;horizontal=0;startSize=30;whiteSpace=wrap;html=1;container=1;` | Horizontal direction swimlanes |
| Grouping Container | `rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;dashed=1;` | Logical grouping (VPC, subnets, etc.) |

#### UML-Specific Shapes

| Shape | Style String | Typical Use |
|------|-----------|----------|
| UML Class | `swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;` | Classes in UML class diagrams |
| UML Divider | `line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;` | Divider between attributes and methods in class diagrams |
| UML Attribute/Method Row | `text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;` | Attribute or method text in class diagrams |
| Lifeline | `shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;` | Sequence diagram lifelines |
| Activation Box | `html=1;points=[];perimeter=orthogonalPerimeter;outlineConnect=0;targetShapes=umlLifeline;portConstraint=eastwest;newEdgeStyle={"curved":0,"rounded":0};` | Sequence diagram activation boxes |
| Initial State | `ellipse;html=1;shape=mxgraph.flowchart.start_2;fontSize=12;fillColor=#000000;fontColor=#FFFFFF;whiteSpace=wrap;` | State diagram initial state (filled circle) |
| Final State | `ellipse;html=1;shape=doubleCircle;whiteSpace=wrap;aspect=fixed;fillColor=#000000;fontColor=#FFFFFF;` | State diagram final state (double circle) |

#### ER Diagram-Specific Shapes

| Shape | Style String | Typical Use |
|------|-----------|----------|
| Entity | `swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;` | Entity tables in ER diagrams |
| Attribute Row | `text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;` | Field rows of entities |

### 4.4 Edge/Connection Line Style Attributes

The following attributes apply to edge type mxCells:

#### Routing Styles

| Attribute | Value | Description |
|------|-----|------|
| `edgeStyle` | `orthogonalEdgeStyle` | **Default routing style**, uses orthogonal (right-angle bend) paths |
| `edgeStyle` | `entityRelationEdgeStyle` | ER diagram relationship line routing |
| `edgeStyle` | `elbowEdgeStyle` | Elbow routing (single bend) |
| `curved` | `0` / `1` | Curved routing, `1` enables smooth curves |
| `rounded` | `0` / `1` | Rounded bends, `1` enables rounded corners at bends |

#### Connection Point Control

Connection point attributes control where an edge exits the source node and enters the target node. Values range from `0` to `1`, representing relative positions on the node boundary:

| Attribute | Value Range | Description |
|------|--------|------|
| `exitX` | `0`–`1` | Source node exit point X coordinate (`0`=left, `0.5`=center, `1`=right) |
| `exitY` | `0`–`1` | Source node exit point Y coordinate (`0`=top, `0.5`=center, `1`=bottom) |
| `exitDx` | Number | Exit point X offset (pixels) |
| `exitDy` | Number | Exit point Y offset (pixels) |
| `entryX` | `0`–`1` | Target node entry point X coordinate (`0`=left, `0.5`=center, `1`=right) |
| `entryY` | `0`–`1` | Target node entry point Y coordinate (`0`=top, `0.5`=center, `1`=bottom) |
| `entryDx` | Number | Entry point X offset (pixels) |
| `entryDy` | Number | Entry point Y offset (pixels) |

Common connection point positions:

```
        exitX=0.5;exitY=0  (top center)
             ┌──────┐
exitX=0;     │      │     exitX=1;
exitY=0.5    │      │     exitY=0.5
(left center)│      │    (right center)
             └──────┘
        exitX=0.5;exitY=1  (bottom center)
```

#### Arrow Styles

| Attribute | Value | Description |
|------|-----|------|
| `endArrow` | `classic` | Classic filled arrow (default) |
| `endArrow` | `block` | Filled triangle arrow |
| `endArrow` | `open` | Open arrow |
| `endArrow` | `diamond` | Diamond arrow (UML aggregation) |
| `endArrow` | `diamondThin` | Thin diamond arrow (UML composition) |
| `endArrow` | `none` | No arrow |
| `endArrow` | `ERone` | ER diagram "one" end marker |
| `endArrow` | `ERmany` | ER diagram "many" end marker |
| `endArrow` | `ERmandOne` | ER diagram "mandatory one" end marker |
| `endArrow` | `ERoneToMany` | ER diagram "one-to-many" end marker |
| `startArrow` | (same as above) | Start-end arrow, values same as `endArrow` |
| `endFill` | `0` / `1` | Whether the end arrow is filled (`0`=open, `1`=filled) |
| `startFill` | `0` / `1` | Whether the start arrow is filled |

#### Line Styles

| Attribute | Value | Description |
|------|-----|------|
| `strokeWidth` | Number | Line width (pixels), default `1` |
| `strokeColor` | Color value | Line color |
| `dashed` | `0` / `1` | Dashed line style, `1` enables dashing |
| `dashPattern` | String | Dash pattern, e.g., `8 8` (8px line + 8px gap) |
| `opacity` | `0`–`100` | Line opacity |

#### Standard Edge Style Strings

```
Default orthogonal edge:
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;

Orthogonal edge with rounded bends:
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;

Dashed edge:
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;

No-arrow bidirectional connection:
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;startArrow=none;

UML inheritance (open triangle arrow):
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;

UML realization (dashed + open triangle arrow):
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;dashed=1;

UML composition (filled diamond):
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=diamondThin;startFill=1;endArrow=open;endFill=0;

UML aggregation (open diamond):
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=diamondThin;startFill=0;endArrow=open;endFill=0;

ER diagram one-to-many relationship:
edgeStyle=entityRelationEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;
```

### 4.5 Color Scheme Guidelines

#### Core Principles

1. **Consistent coloring for same-type elements**: Within the same diagram, elements of the same type must use the same `fillColor` and `strokeColor`
2. **Level differentiation**: Elements at different levels or categories use different fill colors for visual distinction
3. **Contrast**: Ensure sufficient contrast between `fontColor` and `fillColor` to guarantee text readability
4. **Color restraint**: Use no more than 5–7 color varieties in a single diagram to avoid visual clutter

#### Recommended Color Schemes

The following color schemes have been verified for draw.io dark mode compatibility and are suitable for use with `adaptiveColors="auto"` mode:

**Blue Series (Primary elements / Service components)**

```
fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;
```

**Green Series (Success states / Data storage)**

```
fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;
```

**Orange Series (Warnings / Processing steps)**

```
fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;
```

**Red Series (Errors / Critical paths)**

```
fillColor=#F8CECC;strokeColor=#B85450;fontColor=#333333;
```

**Purple Series (External systems / Third-party services)**

```
fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;
```

**Gray Series (Auxiliary elements / Annotations)**

```
fillColor=#F5F5F5;strokeColor=#666666;fontColor=#333333;
```

**Dark Fill (Start/end nodes / Emphasis elements)**

```
fillColor=#6C8EBF;strokeColor=#6C8EBF;fontColor=#FFFFFF;
```

#### Level-Based Coloring Rules

In diagrams with hierarchical structures (e.g., architecture diagrams, organization charts), assign colors to different levels according to the following rules:

| Level | Color Scheme | Example Use |
|------|------|----------|
| Level 1 (Highest) | Blue series `fillColor=#DAE8FC;strokeColor=#6C8EBF;` | System/Platform layer |
| Level 2 | Green series `fillColor=#D5E8D4;strokeColor=#82B366;` | Service/Module layer |
| Level 3 | Orange series `fillColor=#FFE6CC;strokeColor=#D6B656;` | Component/Feature layer |
| Level 4 | Purple series `fillColor=#E1D5E7;strokeColor=#9673A6;` | Sub-component/Tool layer |
| Container/Group | No fill `fillColor=none;strokeColor=#666666;dashed=1;` | VPC, subnets, logical grouping |

#### Diagram Type-Specific Coloring

**Flowchart coloring:**

| Element Type | Color Scheme |
|----------|------|
| Start/End nodes | `fillColor=#6C8EBF;strokeColor=#6C8EBF;fontColor=#FFFFFF;` |
| Processing steps | `fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;` |
| Decision nodes | `fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;` |
| Input/Output | `fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;` |

**UML class diagram coloring:**

| Element Type | Color Scheme |
|----------|------|
| Regular class | `fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;` |
| Abstract class | `fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;` |
| Interface | `fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;` |

**ER diagram coloring:**

| Element Type | Color Scheme |
|----------|------|
| Entity header | `fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;` |
| Attribute row | `fillColor=#FFFFFF;strokeColor=#6C8EBF;fontColor=#333333;` |

### 4.6 whiteSpace=wrap Auto-Wrap Rule

> **CRITICAL**: All vertex type mxCells containing text (non-empty `value` attribute) **must** include `whiteSpace=wrap` in their style string.

#### Rule Description

1. `whiteSpace=wrap` enables text to auto-wrap within the node width, preventing text overflow
2. This attribute must be used together with `html=1` to take effect
3. Even if the text is short and doesn't need wrapping, this attribute must be included for consistency
4. Edge label text does not require this attribute

#### Correct Example

```xml
<mxCell id="node-1" value="User Auth Service" 
        style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;" 
        vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

#### Incorrect Example (missing whiteSpace=wrap)

```xml
<mxCell id="node-1" value="User Auth Service" 
        style="rounded=1;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;" 
        vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

## 5. Diagram Type Templates

### 5.1 Flowchart

Flowcharts use ellipses for start/end nodes, rounded rectangles for processing steps, and diamonds for decision nodes. The following template demonstrates a complete flow with start, processing, decision branching, and end:

```xml
<mxfile>
  <diagram id="flowchart-1" name="Flowchart">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="node-1" value="Start" style="ellipse;whiteSpace=wrap;html=1;fillColor=#6C8EBF;strokeColor=#6C8EBF;fontColor=#FFFFFF;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="340" y="40" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="node-2" value="Receive Request" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="340" y="160" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="node-3" value="Validate Data" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="340" y="280" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="node-4" value="Data Valid?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="330" y="400" width="140" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="node-5" value="Process Business Logic" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="340" y="550" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="node-6" value="Return Error" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontColor=#333333;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="560" y="410" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="node-7" value="End" style="ellipse;whiteSpace=wrap;html=1;fillColor=#6C8EBF;strokeColor=#6C8EBF;fontColor=#FFFFFF;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="340" y="680" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="edge-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="node-1" target="node-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="node-2" target="node-3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="node-3" target="node-4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-4" value="Yes" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="node-4" target="node-5">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-5" value="No" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="node-4" target="node-6">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="node-5" target="node-7">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=1;entryY=0.5;" edge="1" parent="1" source="node-6" target="node-7">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Template key points:

| Element | Shape Style | Color Scheme |
|------|----------|------|
| Start/End nodes | `ellipse;whiteSpace=wrap;html=1;` | Dark blue fill `fillColor=#6C8EBF;fontColor=#FFFFFF;` |
| Processing steps | `rounded=1;whiteSpace=wrap;html=1;` | Light blue fill `fillColor=#DAE8FC;strokeColor=#6C8EBF;` |
| Decision nodes | `rhombus;whiteSpace=wrap;html=1;` | Orange fill `fillColor=#FFE6CC;strokeColor=#D6B656;` |
| Error handling | `rounded=1;whiteSpace=wrap;html=1;` | Red fill `fillColor=#F8CECC;strokeColor=#B85450;` |
| Connection lines | `edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;` | — |
| Decision branch labels | Set `"Yes"` or `"No"` in the edge's `value` attribute | — |

### 5.2 Swimlane Diagram

Swimlane diagrams use the `swimlane` style to create responsibility area containers, with the `startSize` attribute defining the title bar height. Child elements are placed inside the swimlane container using coordinates relative to the container's top-left corner. Cross-swimlane connection lines reference child elements in different swimlanes through `source` and `target`.

```xml
<mxfile>
  <diagram id="swimlane-1" name="Swimlane Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="1100" pageHeight="850"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="lane-1" value="Customer" style="swimlane;startSize=30;whiteSpace=wrap;html=1;container=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontStyle=1;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="300" height="480" as="geometry"/>
        </mxCell>
        <mxCell id="node-1" value="Submit Order" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;" vertex="1" parent="lane-1">
          <mxGeometry x="90" y="50" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="node-4" value="Confirm Receipt" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;" vertex="1" parent="lane-1">
          <mxGeometry x="90" y="380" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="lane-2" value="System" style="swimlane;startSize=30;whiteSpace=wrap;html=1;container=1;fillColor=#D5E8D4;strokeColor=#82B366;fontStyle=1;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="380" y="40" width="300" height="480" as="geometry"/>
        </mxCell>
        <mxCell id="node-2" value="Review Order" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;" vertex="1" parent="lane-2">
          <mxGeometry x="90" y="50" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="node-5" value="Approved?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;" vertex="1" parent="lane-2">
          <mxGeometry x="80" y="160" width="140" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="node-7" value="Cancel Order" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontColor=#333333;" vertex="1" parent="lane-2">
          <mxGeometry x="90" y="380" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="lane-3" value="Warehouse" style="swimlane;startSize=30;whiteSpace=wrap;html=1;container=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontStyle=1;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="720" y="40" width="300" height="480" as="geometry"/>
        </mxCell>
        <mxCell id="node-3" value="Pick &amp; Pack" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;" vertex="1" parent="lane-3">
          <mxGeometry x="90" y="160" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="node-6" value="Ship" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;" vertex="1" parent="lane-3">
          <mxGeometry x="90" y="280" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="edge-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="node-1" target="node-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="node-2" target="node-5">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-3" value="Yes" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="node-5" target="node-3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-4" value="No" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;" edge="1" parent="1" source="node-5" target="node-7">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="node-3" target="node-6">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="node-6" target="node-4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Template key points:

| Key Point | Description |
|------|------|
| Swimlane container | Uses `swimlane;startSize=30;container=1;` style, `startSize` defines the title bar height (pixels) |
| `container=1` | Swimlane mxCells must include this attribute to allow child elements to be placed inside the container |
| Child element `parent` | Child element's `parent` attribute is set to the owning swimlane's `id` (e.g., `parent="lane-1"`) |
| Relative coordinates | Child element `x`, `y` coordinates are relative to the swimlane container's top-left corner, not the canvas origin |
| Cross-swimlane connections | Edge `parent` is set to `"1"` (default layer), `source` and `target` reference child element IDs in different swimlanes |
| Swimlane coloring | Each swimlane uses a different color scheme for visual distinction of responsibility areas |
| Decision branching | Diamond decision nodes can also be used within swimlanes, branch labels are set via the edge's `value` attribute |

### 5.3 UML Class Diagram

UML class diagrams use `swimlane` style containers to represent classes, with internal divider lines separating the class name, attributes, and methods into three areas. Attribute and method rows use the `text` style with `portConstraint=eastwest`. Relationships between classes are represented by edges with specific arrow styles.

```xml
<mxfile>
  <diagram id="class-diagram-1" name="UML Class Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="class-1" value="Animal" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="280" y="40" width="160" height="140" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-attr-1" value="# name: String" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-1">
          <mxGeometry y="26" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-attr-2" value="# age: int" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-1">
          <mxGeometry y="52" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-sep" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;" vertex="1" parent="class-1">
          <mxGeometry y="78" width="160" height="8" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-method-1" value="+ getName(): String" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-1">
          <mxGeometry y="86" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-method-2" value="+ speak(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-1">
          <mxGeometry y="112" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-2" value="Dog" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="100" y="300" width="160" height="140" as="geometry"/>
        </mxCell>
        <mxCell id="class-2-attr-1" value="- breed: String" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-2">
          <mxGeometry y="26" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-2-sep" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;" vertex="1" parent="class-2">
          <mxGeometry y="52" width="160" height="8" as="geometry"/>
        </mxCell>
        <mxCell id="class-2-method-1" value="+ speak(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-2">
          <mxGeometry y="60" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-2-method-2" value="+ fetch(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-2">
          <mxGeometry y="86" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-3" value="Cat" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="460" y="300" width="160" height="140" as="geometry"/>
        </mxCell>
        <mxCell id="class-3-attr-1" value="- indoor: boolean" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-3">
          <mxGeometry y="26" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-3-sep" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;" vertex="1" parent="class-3">
          <mxGeometry y="52" width="160" height="8" as="geometry"/>
        </mxCell>
        <mxCell id="class-3-method-1" value="+ speak(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-3">
          <mxGeometry y="60" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-3-method-2" value="+ purr(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-3">
          <mxGeometry y="86" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="edge-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;" edge="1" parent="1" source="class-2" target="class-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;" edge="1" parent="1" source="class-3" target="class-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Template key points:

| Key Point | Description |
|------|------|
| Class container | Uses `swimlane;fontStyle=1;startSize=26;container=1;collapsible=0;` style, `startSize=26` defines the class name area height |
| Attribute rows | Uses `text;portConstraint=eastwest;` style, `y` coordinate starts from `startSize` (26) and increments |
| Divider line | Uses `line;strokeColor=inherit;portConstraint=eastwest;` style, separates the attribute area from the method area |
| Method rows | Same style as attribute rows, `y` coordinate follows immediately after the divider line |
| Child element `parent` | Attribute rows, divider lines, and method rows have `parent` set to the owning class's `id` |
| Relative coordinates | Child element `y` coordinates are relative to the class container top, `x` coordinate is `0`, `width` matches the class container |
| Inheritance relationship | Uses `endArrow=block;endFill=0;` style (open triangle arrow), pointing from subclass to superclass |
| Visibility markers | `+` for public, `-` for private, `#` for protected |

### 5.4 UML Sequence Diagram

UML sequence diagrams use the `shape=umlLifeline` style to represent participant lifelines. A lifeline is a container that can hold activation boxes inside. Messages connect activation boxes on different lifelines via edges. The following template demonstrates a user login sequence diagram with 3 participants, multiple messages, and activation boxes:

```xml
<mxfile>
  <diagram id="sequence-diagram-1" name="UML Sequence Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="lifeline-1" value="Client" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="40" width="100" height="500" as="geometry"/>
        </mxCell>
        <mxCell id="activation-1" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;outlineConnect=0;targetShapes=umlLifeline;portConstraint=eastwest;newEdgeStyle={&quot;curved&quot;:0,&quot;rounded&quot;:0};fillColor=#DAE8FC;strokeColor=#6C8EBF;" vertex="1" parent="lifeline-1">
          <mxGeometry x="45" y="80" width="10" height="360" as="geometry"/>
        </mxCell>
        <mxCell id="lifeline-2" value="Auth Service" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="330" y="40" width="100" height="500" as="geometry"/>
        </mxCell>
        <mxCell id="activation-2" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;outlineConnect=0;targetShapes=umlLifeline;portConstraint=eastwest;newEdgeStyle={&quot;curved&quot;:0,&quot;rounded&quot;:0};fillColor=#D5E8D4;strokeColor=#82B366;" vertex="1" parent="lifeline-2">
          <mxGeometry x="45" y="100" width="10" height="200" as="geometry"/>
        </mxCell>
        <mxCell id="lifeline-3" value="Database" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="580" y="40" width="100" height="500" as="geometry"/>
        </mxCell>
        <mxCell id="activation-3" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;outlineConnect=0;targetShapes=umlLifeline;portConstraint=eastwest;newEdgeStyle={&quot;curved&quot;:0,&quot;rounded&quot;:0};fillColor=#E1D5E7;strokeColor=#9673A6;" vertex="1" parent="lifeline-3">
          <mxGeometry x="45" y="160" width="10" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="msg-1" value="1: login(user, pwd)" style="html=1;verticalAlign=bottom;endArrow=block;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;" edge="1" parent="1" source="activation-1" target="activation-2">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="200" y="140" as="sourcePoint"/>
            <mxPoint x="370" y="140" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="msg-2" value="2: queryUser(user)" style="html=1;verticalAlign=bottom;endArrow=block;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;" edge="1" parent="1" source="activation-2" target="activation-3">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="390" y="200" as="sourcePoint"/>
            <mxPoint x="620" y="200" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="msg-3" value="3: userData" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;" edge="1" parent="1" source="activation-3" target="activation-2">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="620" y="260" as="sourcePoint"/>
            <mxPoint x="390" y="260" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="msg-4" value="4: authToken" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;" edge="1" parent="1" source="activation-2" target="activation-1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="370" y="340" as="sourcePoint"/>
            <mxPoint x="140" y="340" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="msg-5" value="5: showDashboard()" style="html=1;verticalAlign=bottom;endArrow=block;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;" edge="1" parent="1" source="activation-1" target="activation-1">
          <mxGeometry x="-0.5" relative="1" as="geometry">
            <mxPoint x="140" y="400" as="sourcePoint"/>
            <mxPoint x="140" y="400" as="targetPoint"/>
            <Array as="points">
              <mxPoint x="200" y="400"/>
            </Array>
            <mxPoint as="offset"/>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Template key points:

| Key Point | Description |
|------|------|
| Lifeline | Uses `shape=umlLifeline;container=1;collapsible=0;recursiveResize=0;` style, height determines lifeline length |
| Activation box | Uses `perimeter=orthogonalPerimeter;portConstraint=eastwest;` style, placed inside the lifeline container |
| Activation box coordinates | `x` is set to `(lifeline width - activation box width) / 2` (centered), `y` represents the time position where activation begins |
| Synchronous message | Uses `endArrow=block;` style (filled arrow), from source activation box to target activation box |
| Return message | Uses `endArrow=open;dashed=1;` style (dashed open arrow), represents asynchronous return |
| Self-call message | `source` and `target` point to the same activation box, uses `<Array as="points">` to add offset points forming a loop |
| Message numbering | Uses `1:`, `2:`, etc. numbering in the edge's `value` to annotate message order |
| Special character escaping | The `newEdgeStyle` JSON value in activation box styles requires `"` to be escaped as `&quot;` |

### 5.5 UML State Diagram

UML state diagrams use filled circles for initial states, rounded rectangles for regular state nodes, and double circles for final states. Transitions between states are represented by labeled edges. The following template demonstrates an order lifecycle state diagram with an initial state, 4 regular states, and a final state:

```xml
<mxfile>
  <diagram id="state-diagram-1" name="UML State Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="state-init" value="" style="ellipse;html=1;shape=mxgraph.flowchart.start_2;fontSize=12;fillColor=#000000;fontColor=#FFFFFF;whiteSpace=wrap;" vertex="1" parent="1">
          <mxGeometry x="370" y="40" width="30" height="30" as="geometry"/>
        </mxCell>
        <mxCell id="state-1" value="Pending Payment" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="320" y="120" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="state-2" value="Paid" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="320" y="240" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="state-3" value="In Delivery" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="320" y="360" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="state-4" value="Completed" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="320" y="480" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="state-cancelled" value="Cancelled" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="570" y="240" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="state-end" value="" style="ellipse;html=1;shape=doubleCircle;whiteSpace=wrap;aspect=fixed;fillColor=#000000;fontColor=#FFFFFF;" vertex="1" parent="1">
          <mxGeometry x="375" y="590" width="30" height="30" as="geometry"/>
        </mxCell>
        <mxCell id="edge-1" value="Create Order" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-init" target="state-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-2" value="Payment Successful" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-1" target="state-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-3" value="Ship" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-2" target="state-3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-4" value="Confirm Receipt" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-3" target="state-4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-4" target="state-end">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-6" value="Cancel Order" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-1" target="state-cancelled">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-7" value="Timeout Cancellation" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-2" target="state-cancelled">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=1;entryY=0.5;" edge="1" parent="1" source="state-cancelled" target="state-end">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Template key points:

| Key Point | Description |
|------|------|
| Initial state | Uses `ellipse;shape=mxgraph.flowchart.start_2;fillColor=#000000;` style, recommended size 30×30 |
| Regular state | Uses `rounded=1;arcSize=20;` rounded rectangle style, different state categories use different color schemes |
| Final state | Uses `ellipse;shape=doubleCircle;fillColor=#000000;aspect=fixed;` style, recommended size 30×30 |
| Transition labels | Set trigger event names in the edge's `value` attribute (e.g., `"Payment Successful"`, `"Ship"`) |
| Initial transition | Edge from initial state to first regular state, `value` can be set to the triggering action |
| Final transition | Edge from last regular state to final state, usually no `value` is set |
| Exception path | Uses red color scheme (`fillColor=#F8CECC;strokeColor=#B85450;`) to identify cancelled/exception states |
| Multiple entry transitions | Multiple states can transition to the same target state (e.g., multiple states can transition to "Cancelled") |


### 5.6 ER Diagram

ER diagrams use `swimlane` style containers to represent entities (in a table format similar to UML class diagrams), with each internal row representing a field, annotated with field name, data type, and primary key (PK) / foreign key (FK) constraints. Relationships between entities use edges with `entityRelationEdgeStyle` routing style, with `startArrow` and `endArrow` ER-specific arrow markers indicating cardinality (one-to-one, one-to-many, many-to-many). The following template demonstrates a database ER diagram with 3 entities (User, Order, Product) and their relationships:

```xml
<mxfile>
  <diagram id="er-diagram-1" name="ER Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="1100" pageHeight="850"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="entity-user" value="User" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="80" y="120" width="200" height="156" as="geometry"/>
        </mxCell>
        <mxCell id="user-attr-1" value="PK  id: INT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontStyle=4;" vertex="1" parent="entity-user">
          <mxGeometry y="26" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="user-sep" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;" vertex="1" parent="entity-user">
          <mxGeometry y="52" width="200" height="8" as="geometry"/>
        </mxCell>
        <mxCell id="user-attr-2" value="    username: VARCHAR(50)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="entity-user">
          <mxGeometry y="60" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="user-attr-3" value="    email: VARCHAR(100)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="entity-user">
          <mxGeometry y="86" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="user-attr-4" value="    created_at: DATETIME" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="entity-user">
          <mxGeometry y="112" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="entity-order" value="Order" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="430" y="80" width="200" height="208" as="geometry"/>
        </mxCell>
        <mxCell id="order-attr-1" value="PK  id: INT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontStyle=4;" vertex="1" parent="entity-order">
          <mxGeometry y="26" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="order-sep" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;" vertex="1" parent="entity-order">
          <mxGeometry y="52" width="200" height="8" as="geometry"/>
        </mxCell>
        <mxCell id="order-attr-2" value="FK  user_id: INT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontStyle=2;" vertex="1" parent="entity-order">
          <mxGeometry y="60" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="order-attr-3" value="    order_date: DATETIME" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="entity-order">
          <mxGeometry y="86" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="order-attr-4" value="    total_amount: DECIMAL" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="entity-order">
          <mxGeometry y="112" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="order-attr-5" value="    status: VARCHAR(20)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="entity-order">
          <mxGeometry y="138" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="entity-product" value="Product" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="780" y="120" width="200" height="182" as="geometry"/>
        </mxCell>
        <mxCell id="product-attr-1" value="PK  id: INT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontStyle=4;" vertex="1" parent="entity-product">
          <mxGeometry y="26" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="product-sep" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;" vertex="1" parent="entity-product">
          <mxGeometry y="52" width="200" height="8" as="geometry"/>
        </mxCell>
        <mxCell id="product-attr-2" value="    name: VARCHAR(100)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="entity-product">
          <mxGeometry y="60" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="product-attr-3" value="    price: DECIMAL" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="entity-product">
          <mxGeometry y="86" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="product-attr-4" value="    stock: INT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="entity-product">
          <mxGeometry y="112" width="200" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="er-edge-1" value="" style="edgeStyle=entityRelationEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;strokeColor=#6C8EBF;" edge="1" parent="1" source="user-attr-1" target="order-attr-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="er-edge-2" value="" style="edgeStyle=entityRelationEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmany;startFill=0;endArrow=ERmany;endFill=0;strokeColor=#9673A6;" edge="1" parent="1" source="order-attr-1" target="product-attr-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Template key points:

| Key Point | Description |
|------|------|
| Entity container | Uses `swimlane;fontStyle=1;startSize=26;container=1;collapsible=0;` style, same table format as UML class diagrams |
| Primary key row (PK) | Prefixed with `PK` in `value`, highlighted with `fontStyle=4;` (underline) |
| Foreign key row (FK) | Prefixed with `FK` in `value`, distinguished with `fontStyle=2;` (italic) |
| Regular field rows | Display field name and data type, aligned with indentation |
| Divider line | Uses `line;strokeColor=inherit;` style, separates the primary key area from the regular field area |
| Relationship line routing | Uses `edgeStyle=entityRelationEdgeStyle;` ER diagram-specific routing style |
| One-to-many relationship | `startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;` (User → Order) |
| Many-to-many relationship | `startArrow=ERmany;startFill=0;endArrow=ERmany;endFill=0;` (Order ↔ Product) |
| Connection endpoints | Edge `source` and `target` point to entity attribute rows (e.g., PK or FK rows), precisely connecting lines to related fields |
| Entity coloring | Different entities use different color schemes for visual distinction (blue, green, purple) |


### 5.7 Network Topology Diagram

Network topology diagrams use specific shapes to represent network devices (routers, switches, firewalls, servers, etc.), with connection lines representing network connections between devices. Containers can be used to logically group network zones (e.g., DMZ, internal network, external network), and subnet/segment information can be labeled on connection lines. The following template demonstrates a typical enterprise network topology with a firewall, router, switch, servers, and clients:

```xml
<mxfile>
  <diagram id="network-topology-1" name="Network Topology Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="1100" pageHeight="850"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="net-cloud" value="Internet" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontColor=#333333;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="420" y="30" width="160" height="90" as="geometry"/>
        </mxCell>
        <mxCell id="net-firewall" value="Firewall" style="shape=mxgraph.cisco.firewalls.firewall;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="460" y="190" width="80" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="net-router" value="Core Router" style="shape=mxgraph.cisco.routers.router;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="455" y="330" width="90" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="net-zone-dmz" value="DMZ Zone" style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;strokeColor=#B85450;dashed=1;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="40" y="280" width="300" height="250" as="geometry"/>
        </mxCell>
        <mxCell id="net-web-server" value="Web Server" style="shape=mxgraph.cisco.servers.standard_server;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;" vertex="1" parent="net-zone-dmz">
          <mxGeometry x="40" y="60" width="50" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="net-mail-server" value="Mail Server" style="shape=mxgraph.cisco.servers.standard_server;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;" vertex="1" parent="net-zone-dmz">
          <mxGeometry x="200" y="60" width="50" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="net-zone-lan" value="Internal Network (10.0.0.0/16)" style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;strokeColor=#6C8EBF;dashed=1;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="660" y="280" width="380" height="250" as="geometry"/>
        </mxCell>
        <mxCell id="net-switch" value="Switch" style="shape=mxgraph.cisco.switches.workgroup_switch;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;fontSize=12;" vertex="1" parent="net-zone-lan">
          <mxGeometry x="150" y="50" width="80" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="net-db-server" value="Database Server" style="shape=mxgraph.cisco.servers.standard_server;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;fontSize=12;" vertex="1" parent="net-zone-lan">
          <mxGeometry x="40" y="150" width="50" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="net-app-server" value="Application Server" style="shape=mxgraph.cisco.servers.standard_server;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;" vertex="1" parent="net-zone-lan">
          <mxGeometry x="160" y="150" width="50" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="net-client" value="Client" style="shape=mxgraph.cisco.computers_and_peripherals.pc;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=12;" vertex="1" parent="net-zone-lan">
          <mxGeometry x="280" y="150" width="50" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="net-edge-1" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;" edge="1" parent="1" source="net-cloud" target="net-firewall">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="net-edge-2" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;" edge="1" parent="1" source="net-firewall" target="net-router">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="net-edge-3" value="172.16.0.0/24" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0;exitY=0.5;entryX=1;entryY=0;strokeWidth=2;" edge="1" parent="1" source="net-router" target="net-zone-dmz">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="net-edge-4" value="10.0.0.0/16" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0;strokeWidth=2;" edge="1" parent="1" source="net-router" target="net-zone-lan">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="net-edge-5" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;startArrow=none;" edge="1" parent="1" source="net-switch" target="net-db-server">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="net-edge-6" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;startArrow=none;" edge="1" parent="1" source="net-switch" target="net-app-server">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="net-edge-7" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;startArrow=none;" edge="1" parent="1" source="net-switch" target="net-client">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Template key points:

| Key Point | Description |
|------|------|
| Internet cloud | Uses `ellipse;shape=cloud;` style to represent external network, gray color scheme |
| Firewall | Uses `shape=mxgraph.cisco.firewalls.firewall;` Cisco icon, red color scheme for security devices |
| Router | Uses `shape=mxgraph.cisco.routers.router;` Cisco icon, blue color scheme |
| Switch | Uses `shape=mxgraph.cisco.switches.workgroup_switch;` Cisco icon, orange color scheme |
| Server | Uses `shape=mxgraph.cisco.servers.standard_server;` Cisco icon, green/purple color scheme |
| Client | Uses `shape=mxgraph.cisco.computers_and_peripherals.pc;` Cisco icon |
| Network zone container | Uses `container=1;pointerEvents=0;fillColor=none;dashed=1;` dashed border container, `verticalAlign=top` displays title at top |
| DMZ zone | Red dashed border (`strokeColor=#B85450;`), contains externally-facing servers |
| Internal network zone | Blue dashed border (`strokeColor=#6C8EBF;`), annotated with subnet address (e.g., `10.0.0.0/16`) |
| Subnet labels | Subnet addresses annotated in the connection line's `value` attribute (e.g., `172.16.0.0/24`) |
| Connection line style | Network connections use `strokeWidth=2;` bold lines, switch-to-endpoint connections use `endArrow=none;startArrow=none;` no-arrow bidirectional connections |
| Child element coordinates | Devices inside zone containers use coordinates relative to the container's top-left corner |


### 5.8 Architecture Diagram

Architecture diagrams use rounded rectangles for system components/services, cylinders for databases, and cloud shapes for external systems, with arrowed connection lines representing data flow and call relationships. Containers can be used to group logical layers (e.g., frontend layer, service layer, data layer). The following template demonstrates a typical 3-tier web application architecture with users, frontend, backend services, cache, database, and message queue:

```xml
<mxfile>
  <diagram id="architecture-1" name="Architecture Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="1100" pageHeight="850"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="arch-user" value="User / Browser" style="shape=mxgraph.cisco.computers_and_peripherals.pc;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="480" y="30" width="60" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="arch-layer-frontend" value="Frontend Layer" style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;strokeColor=#6C8EBF;dashed=1;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="310" y="140" width="400" height="120" as="geometry"/>
        </mxCell>
        <mxCell id="arch-cdn" value="CDN" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=12;" vertex="1" parent="arch-layer-frontend">
          <mxGeometry x="30" y="40" width="100" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="arch-nginx" value="Nginx" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=12;" vertex="1" parent="arch-layer-frontend">
          <mxGeometry x="250" y="40" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="arch-layer-service" value="Service Layer" style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;strokeColor=#82B366;dashed=1;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="200" y="330" width="620" height="120" as="geometry"/>
        </mxCell>
        <mxCell id="arch-api" value="API Gateway" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;" vertex="1" parent="arch-layer-service">
          <mxGeometry x="30" y="40" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="arch-auth" value="Auth Service" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;" vertex="1" parent="arch-layer-service">
          <mxGeometry x="190" y="40" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="arch-biz" value="Business Service" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;" vertex="1" parent="arch-layer-service">
          <mxGeometry x="470" y="40" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="arch-layer-data" value="Data Layer" style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;strokeColor=#D6B656;dashed=1;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="200" y="530" width="620" height="140" as="geometry"/>
        </mxCell>
        <mxCell id="arch-db" value="MySQL" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;size=15;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;fontSize=12;" vertex="1" parent="arch-layer-data">
          <mxGeometry x="50" y="40" width="80" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="arch-cache" value="Redis" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;size=15;fillColor=#F8CECC;strokeColor=#B85450;fontColor=#333333;fontSize=12;" vertex="1" parent="arch-layer-data">
          <mxGeometry x="260" y="40" width="80" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="arch-mq" value="Message Queue" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;fontSize=12;" vertex="1" parent="arch-layer-data">
          <mxGeometry x="470" y="50" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="arch-edge-1" value="HTTPS" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="arch-user" target="arch-cdn">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="arch-edge-2" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="arch-cdn" target="arch-nginx">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="arch-edge-3" value="HTTP" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="arch-nginx" target="arch-api">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="arch-edge-4" value="JWT" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="arch-api" target="arch-auth">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="arch-edge-5" value="gRPC" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="arch-api" target="arch-biz">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="arch-edge-6" value="SQL" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="arch-biz" target="arch-db">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="arch-edge-7" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="arch-biz" target="arch-cache">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="arch-edge-8" value="Async Message" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;" edge="1" parent="1" source="arch-biz" target="arch-mq">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Template key points:

| Key Point | Description |
|------|------|
| User/Client | Uses PC icon or person icon to represent external users |
| Service components | Uses `rounded=1;whiteSpace=wrap;html=1;` rounded rectangles, different layers use different color schemes |
| Database | Uses `shape=cylinder3;boundedLbl=1;size=15;` cylinder style |
| External service/CDN | Uses `ellipse;shape=cloud;` cloud style |
| Message queue | Uses rounded rectangle, purple color scheme for distinction |
| Logical layer containers | Uses `container=1;pointerEvents=0;fillColor=none;dashed=1;` dashed border containers |
| Frontend layer | Blue dashed border (`strokeColor=#6C8EBF;`), contains CDN and reverse proxy |
| Service layer | Green dashed border (`strokeColor=#82B366;`), contains API gateway and microservices |
| Data layer | Orange dashed border (`strokeColor=#D6B656;`), contains database, cache, and message queue |
| Data flow labels | Protocol or data type annotated in the connection line's `value` attribute (e.g., `HTTPS`, `gRPC`, `SQL`) |
| Async connections | Uses `dashed=1;` dashed line style to represent asynchronous message passing |
| Child element coordinates | Components inside layer containers use coordinates relative to the container's top-left corner |

### 5.9 Mind Map

Mind maps have a central topic node as the core, radiating outward into multiple main branches, each of which can further expand into sub-branches. The central node typically uses a larger ellipse or rounded rectangle with bold text, and different branches use different color schemes for visual distinction. Connection lines can use curves (`curved=1`) or orthogonal routing. The following template demonstrates a mind map with "Project Management" as the central topic, 4 main branches, and multiple sub-branches:

```xml
<mxfile>
  <diagram id="mindmap-1" name="Mind Map">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="1100" pageHeight="850"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="mind-center" value="Project Management" style="ellipse;whiteSpace=wrap;html=1;fillColor=#6C8EBF;strokeColor=#6C8EBF;fontColor=#FFFFFF;fontSize=18;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="440" y="340" width="160" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-1" value="Planning Phase" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="140" y="120" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-1-1" value="Requirements Analysis" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="10" y="30" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-1-2" value="Define Milestones" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="10" y="190" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-2" value="Execution Phase" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="740" y="120" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-2-1" value="Task Assignment" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="920" y="30" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-2-2" value="Progress Tracking" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="920" y="100" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-2-3" value="Code Review" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="920" y="170" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-3" value="Monitoring Phase" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="140" y="530" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-3-1" value="Risk Management" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="10" y="480" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-3-2" value="Quality Assurance" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="10" y="570" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-4" value="Closing Phase" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="740" y="530" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-4-1" value="Acceptance Testing" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="920" y="490" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="mind-branch-4-2" value="Document Archiving" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="920" y="560" width="110" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;exitX=0;exitY=0.5;entryX=1;entryY=0.5;strokeColor=#6C8EBF;strokeWidth=2;endArrow=none;" edge="1" parent="1" source="mind-center" target="mind-branch-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;strokeColor=#82B366;strokeWidth=2;endArrow=none;" edge="1" parent="1" source="mind-center" target="mind-branch-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;exitX=0;exitY=0.5;entryX=1;entryY=0.5;strokeColor=#D6B656;strokeWidth=2;endArrow=none;" edge="1" parent="1" source="mind-center" target="mind-branch-3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;strokeColor=#9673A6;strokeWidth=2;endArrow=none;" edge="1" parent="1" source="mind-center" target="mind-branch-4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-1-1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;strokeColor=#6C8EBF;endArrow=none;" edge="1" parent="1" source="mind-branch-1" target="mind-branch-1-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-1-2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;strokeColor=#6C8EBF;endArrow=none;" edge="1" parent="1" source="mind-branch-1" target="mind-branch-1-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-2-1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;strokeColor=#82B366;endArrow=none;" edge="1" parent="1" source="mind-branch-2" target="mind-branch-2-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-2-2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;strokeColor=#82B366;endArrow=none;" edge="1" parent="1" source="mind-branch-2" target="mind-branch-2-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-2-3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;strokeColor=#82B366;endArrow=none;" edge="1" parent="1" source="mind-branch-2" target="mind-branch-2-3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-3-1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;strokeColor=#D6B656;endArrow=none;" edge="1" parent="1" source="mind-branch-3" target="mind-branch-3-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-3-2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;strokeColor=#D6B656;endArrow=none;" edge="1" parent="1" source="mind-branch-3" target="mind-branch-3-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-4-1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;strokeColor=#9673A6;endArrow=none;" edge="1" parent="1" source="mind-branch-4" target="mind-branch-4-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="mind-edge-4-2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;curved=1;strokeColor=#9673A6;endArrow=none;" edge="1" parent="1" source="mind-branch-4" target="mind-branch-4-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Template key points:

| Key Point | Description |
|------|------|
| Central topic | Uses `ellipse;fontSize=18;fontStyle=1;` ellipse style, dark fill (`fillColor=#6C8EBF;fontColor=#FFFFFF;`), larger size (160×80) to highlight the core topic |
| Main branch nodes | Uses `rounded=1;fontSize=14;fontStyle=1;` rounded rectangle style, each branch uses a different color scheme (blue, green, orange, purple) |
| Sub-branch nodes | Uses `rounded=1;fontSize=12;` rounded rectangle style, same color scheme as the parent branch, smaller size (110×40) |
| Branch connection lines | Uses `curved=1;endArrow=none;` curved connections, no arrows, `strokeColor` matches the corresponding branch color |
| Trunk connection lines | Uses `strokeWidth=2;` bold lines connecting the central topic to main branches, visually emphasizing trunk relationships |
| Sub-branch connection lines | Uses default line width connecting main branches to sub-branches, visually lower hierarchy than trunk connections |
| Layout direction | Left-right symmetric distribution: planning and monitoring branches on the left, execution and closing branches on the right |
| Color consistency | All nodes and connection lines under the same branch use the same color scheme for easy visual tracking |


### 5.10 Organization Chart

Organization charts use a hierarchical top-down layout to display organizational structure and reporting relationships. The top level is the highest manager (e.g., CEO/General Manager), expanding downward to department heads and team members. Different levels use different color schemes to distinguish ranks, and connection lines use orthogonal routing from the bottom of the superior node to the top of the subordinate node. The following template demonstrates a three-level organization with a General Manager, 3 department heads, and 6 team members:

```xml
<mxfile>
  <diagram id="org-chart-1" name="Organization Chart">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="1100" pageHeight="850"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="org-ceo" value="Zhang Wei&#xa;General Manager" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#6C8EBF;strokeColor=#6C8EBF;fontColor=#FFFFFF;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="430" y="40" width="160" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="org-dept-1" value="Li Na&#xa;CTO" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="120" y="180" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="org-dept-2" value="Wang Qiang&#xa;VP of Product" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="440" y="180" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="org-dept-3" value="Zhao Min&#xa;VP of Operations" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="760" y="180" width="150" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="org-member-1" value="Chen Lei&#xa;Frontend Engineer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="30" y="340" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="org-member-2" value="Liu Yang&#xa;Backend Engineer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="210" y="340" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="org-member-3" value="Sun Yue&#xa;Product Manager" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="380" y="340" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="org-member-4" value="Zhou Ting&#xa;UI Designer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="550" y="340" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="org-member-5" value="Wu Hao&#xa;Marketing Specialist" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="710" y="340" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="org-member-6" value="Zheng Fang&#xa;Customer Service Lead" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="880" y="340" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="org-edge-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=none;" edge="1" parent="1" source="org-ceo" target="org-dept-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="org-edge-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=none;" edge="1" parent="1" source="org-ceo" target="org-dept-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="org-edge-3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=none;" edge="1" parent="1" source="org-ceo" target="org-dept-3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="org-edge-4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=none;" edge="1" parent="1" source="org-dept-1" target="org-member-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="org-edge-5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=none;" edge="1" parent="1" source="org-dept-1" target="org-member-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="org-edge-6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=none;" edge="1" parent="1" source="org-dept-2" target="org-member-3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="org-edge-7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=none;" edge="1" parent="1" source="org-dept-2" target="org-member-4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="org-edge-8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=none;" edge="1" parent="1" source="org-dept-3" target="org-member-5">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="org-edge-9" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=none;" edge="1" parent="1" source="org-dept-3" target="org-member-6">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Template key points:

| Key Point | Description |
|------|------|
| Top manager | Uses `rounded=1;fontSize=14;fontStyle=1;` style, dark fill (`fillColor=#6C8EBF;fontColor=#FFFFFF;`), centered at the top |
| Department heads | Uses `rounded=1;fontSize=13;fontStyle=1;` style, light fill, each department uses a different color scheme (blue=Technology, green=Product, orange=Operations) |
| Team members | Uses `rounded=1;fontSize=12;` style, same color scheme as their department, slightly smaller than department head nodes |
| Multi-line text | Uses `&#xa;` for line breaks within nodes, first line is the name, second line is the title |
| Hierarchical connection lines | Uses `endArrow=none;` no-arrow style, with `exitX=0.5;exitY=1;entryX=0.5;entryY=0;` ensuring connections from the superior's bottom center to the subordinate's top center |
| Level spacing | Level 1 (y=40) → Level 2 (y=180) → Level 3 (y=340), approximately 100-120px between levels |
| Color hierarchy | Level 1 uses dark fill (emphasis), Level 2 uses light fill (department distinction), Level 3 matches department color (sense of belonging) |
| Horizontal distribution | Same-level nodes are evenly distributed horizontally, maintaining symmetry |

## 6. Cloud Architecture Icon Reference

Cloud architecture diagrams use draw.io's stencil library to reference cloud service icons. Icons are specified through the `shape=mxgraph.<provider>.<service>` style attribute, with each cloud provider having its own namespace.

### General Rules

- Recommended cloud icon size: **60×60** (standard) or **78×78** (large icon), keep `aspect=fixed` to prevent icon distortion
- All cloud icon nodes must include `whiteSpace=wrap;html=1;`
- Icon labels are typically placed below the icon, using `verticalLabelPosition=bottom;verticalAlign=top;align=center;`
- Each service category has a corresponding official brand color (`fillColor`), services in the same category use the same fill color
- `strokeColor` uniformly uses `#ffffff` (white border)

### Cloud Icon mxCell Template

```xml
<mxCell id="{id}" value="{service-name}" 
        style="shape=mxgraph.{provider}.{service};whiteSpace=wrap;html=1;fillColor={category-color};strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;" 
        vertex="1" parent="{parent-id}">
  <mxGeometry x="{x}" y="{y}" width="60" height="60" as="geometry"/>
</mxCell>
```

### 6.1 AWS Icons (`mxgraph.aws4.*`)

AWS icons use the `mxgraph.aws4` namespace. Each service category has a corresponding official brand color.

#### Compute — `fillColor=#ED7100`

| Service | Style String | Description |
|------|-----------|------|
| EC2 | `shape=mxgraph.aws4.ec2;fillColor=#ED7100;strokeColor=#ffffff;` | Elastic compute instances |
| Lambda | `shape=mxgraph.aws4.lambda_function;fillColor=#ED7100;strokeColor=#ffffff;` | Serverless functions |
| ECS | `shape=mxgraph.aws4.ecs;fillColor=#ED7100;strokeColor=#ffffff;` | Container service |
| EKS | `shape=mxgraph.aws4.eks;fillColor=#ED7100;strokeColor=#ffffff;` | Kubernetes service |
| Fargate | `shape=mxgraph.aws4.fargate;fillColor=#ED7100;strokeColor=#ffffff;` | Serverless containers |
| Auto Scaling | `shape=mxgraph.aws4.auto_scaling2;fillColor=#ED7100;strokeColor=#ffffff;` | Auto scaling |
| Elastic Beanstalk | `shape=mxgraph.aws4.elastic_beanstalk;fillColor=#ED7100;strokeColor=#ffffff;` | Application deployment platform |

#### Storage — `fillColor=#3F8624`

| Service | Style String | Description |
|------|-----------|------|
| S3 | `shape=mxgraph.aws4.s3;fillColor=#3F8624;strokeColor=#ffffff;` | Object storage |
| EBS | `shape=mxgraph.aws4.elastic_block_store;fillColor=#3F8624;strokeColor=#ffffff;` | Block storage |
| EFS | `shape=mxgraph.aws4.elastic_file_system;fillColor=#3F8624;strokeColor=#ffffff;` | File storage |
| S3 Glacier | `shape=mxgraph.aws4.glacier;fillColor=#3F8624;strokeColor=#ffffff;` | Archive storage |

#### Database — `fillColor=#C925D1`

| Service | Style String | Description |
|------|-----------|------|
| RDS | `shape=mxgraph.aws4.rds;fillColor=#C925D1;strokeColor=#ffffff;` | Relational database |
| DynamoDB | `shape=mxgraph.aws4.dynamodb;fillColor=#C925D1;strokeColor=#ffffff;` | NoSQL database |
| ElastiCache | `shape=mxgraph.aws4.elasticache;fillColor=#C925D1;strokeColor=#ffffff;` | Cache service |
| Aurora | `shape=mxgraph.aws4.aurora;fillColor=#C925D1;strokeColor=#ffffff;` | High-performance relational database |
| Redshift | `shape=mxgraph.aws4.redshift;fillColor=#C925D1;strokeColor=#ffffff;` | Data warehouse |

#### Networking — `fillColor=#8C4FFF`

| Service | Style String | Description |
|------|-----------|------|
| VPC | `shape=mxgraph.aws4.vpc;fillColor=#8C4FFF;strokeColor=#ffffff;` | Virtual private cloud |
| CloudFront | `shape=mxgraph.aws4.cloudfront;fillColor=#8C4FFF;strokeColor=#ffffff;` | CDN content delivery |
| Route 53 | `shape=mxgraph.aws4.route_53;fillColor=#8C4FFF;strokeColor=#ffffff;` | DNS service |
| API Gateway | `shape=mxgraph.aws4.api_gateway;fillColor=#8C4FFF;strokeColor=#ffffff;` | API gateway |
| ELB | `shape=mxgraph.aws4.elastic_load_balancing;fillColor=#8C4FFF;strokeColor=#ffffff;` | Load balancer |
| ALB | `shape=mxgraph.aws4.application_load_balancer;fillColor=#8C4FFF;strokeColor=#ffffff;` | Application load balancer |
| NLB | `shape=mxgraph.aws4.network_load_balancer;fillColor=#8C4FFF;strokeColor=#ffffff;` | Network load balancer |

#### Security — `fillColor=#DD344C`

| Service | Style String | Description |
|------|-----------|------|
| IAM | `shape=mxgraph.aws4.iam;fillColor=#DD344C;strokeColor=#ffffff;` | Identity and access management |
| Cognito | `shape=mxgraph.aws4.cognito;fillColor=#DD344C;strokeColor=#ffffff;` | User authentication |
| WAF | `shape=mxgraph.aws4.waf;fillColor=#DD344C;strokeColor=#ffffff;` | Web application firewall |
| Shield | `shape=mxgraph.aws4.shield;fillColor=#DD344C;strokeColor=#ffffff;` | DDoS protection |
| KMS | `shape=mxgraph.aws4.key_management_service;fillColor=#DD344C;strokeColor=#ffffff;` | Key management |
| Secrets Manager | `shape=mxgraph.aws4.secrets_manager;fillColor=#DD344C;strokeColor=#ffffff;` | Secrets management |

#### Application Integration — `fillColor=#E7157B`

| Service | Style String | Description |
|------|-----------|------|
| SQS | `shape=mxgraph.aws4.sqs;fillColor=#E7157B;strokeColor=#ffffff;` | Message queue |
| SNS | `shape=mxgraph.aws4.sns;fillColor=#E7157B;strokeColor=#ffffff;` | Notification service |
| Step Functions | `shape=mxgraph.aws4.step_functions;fillColor=#E7157B;strokeColor=#ffffff;` | Workflow orchestration |
| EventBridge | `shape=mxgraph.aws4.eventbridge;fillColor=#E7157B;strokeColor=#ffffff;` | Event bus |

#### Management & Monitoring — `fillColor=#E7157B`

| Service | Style String | Description |
|------|-----------|------|
| CloudWatch | `shape=mxgraph.aws4.cloudwatch;fillColor=#E7157B;strokeColor=#ffffff;` | Monitoring service |
| CloudFormation | `shape=mxgraph.aws4.cloudformation;fillColor=#E7157B;strokeColor=#ffffff;` | Infrastructure as code |

#### AI / ML — `fillColor=#01A88D`

> **IMPORTANT**: Bedrock, SageMaker, OpenSearch and other AI/ML services use the `resourceIcon` + `resIcon` two-part style. The `shape=mxgraph.aws4.resourceIcon` sets the icon container, and `resIcon=mxgraph.aws4.{service}` specifies the actual service icon.

| Service | Style String | Description |
|------|-----------|------|
| Bedrock | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.bedrock;fillColor=#01A88D;strokeColor=#ffffff;` | Foundation model service |
| Bedrock Knowledge Bases | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.bedrock;fillColor=#01A88D;strokeColor=#ffffff;` | RAG knowledge base (use Bedrock icon) |
| SageMaker | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sagemaker;fillColor=#01A88D;strokeColor=#ffffff;` | ML platform |
| OpenSearch Service | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticsearch_service;fillColor=#01A88D;strokeColor=#ffffff;` | Search & vector database |
| Comprehend | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.comprehend;fillColor=#01A88D;strokeColor=#ffffff;` | NLP service |
| Rekognition | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rekognition;fillColor=#01A88D;strokeColor=#ffffff;` | Image/video analysis |
| Textract | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.textract;fillColor=#01A88D;strokeColor=#ffffff;` | Document text extraction |
| Kendra | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.kendra;fillColor=#01A88D;strokeColor=#ffffff;` | Intelligent search |
| Lex | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lex;fillColor=#01A88D;strokeColor=#ffffff;` | Conversational AI |
| Polly | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.polly;fillColor=#01A88D;strokeColor=#ffffff;` | Text-to-speech |
| Transcribe | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.transcribe;fillColor=#01A88D;strokeColor=#ffffff;` | Speech-to-text |
| Translate | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.translate;fillColor=#01A88D;strokeColor=#ffffff;` | Language translation |

**Full style string for AI/ML icons (copy-paste template):**

```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.bedrock;whiteSpace=wrap;html=1;fillColor=#01A88D;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;
```

### 6.2 Azure Icons (`mxgraph.azure.*`)

Azure icons use the `mxgraph.azure` namespace. Azure services uniformly use brand blue `#0078D4` as the primary color, with some service categories having independent coloring.

#### Compute — `fillColor=#0078D4`

| Service | Style String | Description |
|------|-----------|------|
| Virtual Machine | `shape=mxgraph.azure.virtual_machine;fillColor=#0078D4;strokeColor=#ffffff;` | Virtual machine |
| App Service | `shape=mxgraph.azure.app_service;fillColor=#0078D4;strokeColor=#ffffff;` | Web app hosting |
| Functions | `shape=mxgraph.azure.function_apps;fillColor=#0078D4;strokeColor=#ffffff;` | Serverless functions |
| AKS | `shape=mxgraph.azure.kubernetes_services;fillColor=#0078D4;strokeColor=#ffffff;` | Kubernetes service |
| Container Instances | `shape=mxgraph.azure.container_instances;fillColor=#0078D4;strokeColor=#ffffff;` | Container instances |

#### Storage — `fillColor=#0078D4`

| Service | Style String | Description |
|------|-----------|------|
| Blob Storage | `shape=mxgraph.azure.blob_storage;fillColor=#0078D4;strokeColor=#ffffff;` | Object storage |
| Storage Accounts | `shape=mxgraph.azure.storage;fillColor=#0078D4;strokeColor=#ffffff;` | Storage accounts |
| Managed Disks | `shape=mxgraph.azure.managed_disks;fillColor=#0078D4;strokeColor=#ffffff;` | Managed disks |
| File Storage | `shape=mxgraph.azure.file_storage;fillColor=#0078D4;strokeColor=#ffffff;` | File storage |

#### Database — `fillColor=#0078D4`

| Service | Style String | Description |
|------|-----------|------|
| SQL Database | `shape=mxgraph.azure.sql_databases;fillColor=#0078D4;strokeColor=#ffffff;` | SQL database |
| Cosmos DB | `shape=mxgraph.azure.cosmos_db;fillColor=#0078D4;strokeColor=#ffffff;` | Multi-model database |
| Cache for Redis | `shape=mxgraph.azure.cache_for_redis;fillColor=#0078D4;strokeColor=#ffffff;` | Redis cache |
| SQL Data Warehouse | `shape=mxgraph.azure.sql_data_warehouses;fillColor=#0078D4;strokeColor=#ffffff;` | Data warehouse |

#### Networking — `fillColor=#0078D4`

| Service | Style String | Description |
|------|-----------|------|
| Virtual Network | `shape=mxgraph.azure.virtual_networks;fillColor=#0078D4;strokeColor=#ffffff;` | Virtual network |
| Load Balancer | `shape=mxgraph.azure.load_balancers;fillColor=#0078D4;strokeColor=#ffffff;` | Load balancer |
| Application Gateway | `shape=mxgraph.azure.application_gateways;fillColor=#0078D4;strokeColor=#ffffff;` | Application gateway |
| CDN | `shape=mxgraph.azure.content_delivery_network;fillColor=#0078D4;strokeColor=#ffffff;` | Content delivery network |
| DNS Zone | `shape=mxgraph.azure.dns_zones;fillColor=#0078D4;strokeColor=#ffffff;` | DNS zone |
| API Management | `shape=mxgraph.azure.api_management;fillColor=#0078D4;strokeColor=#ffffff;` | API management |

#### Security — `fillColor=#0078D4`

| Service | Style String | Description |
|------|-----------|------|
| Azure AD | `shape=mxgraph.azure.active_directory;fillColor=#0078D4;strokeColor=#ffffff;` | Identity authentication |
| Key Vault | `shape=mxgraph.azure.key_vaults;fillColor=#0078D4;strokeColor=#ffffff;` | Key vault |
| Firewall | `shape=mxgraph.azure.azure_firewall;fillColor=#0078D4;strokeColor=#ffffff;` | Firewall |
| NSG | `shape=mxgraph.azure.network_security_groups;fillColor=#0078D4;strokeColor=#ffffff;` | Network security group |

#### Messaging & Integration — `fillColor=#0078D4`

| Service | Style String | Description |
|------|-----------|------|
| Service Bus | `shape=mxgraph.azure.service_bus;fillColor=#0078D4;strokeColor=#ffffff;` | Message bus |
| Event Hub | `shape=mxgraph.azure.event_hubs;fillColor=#0078D4;strokeColor=#ffffff;` | Event hub |
| Event Grid | `shape=mxgraph.azure.event_grid;fillColor=#0078D4;strokeColor=#ffffff;` | Event grid |

#### Monitoring — `fillColor=#0078D4`

| Service | Style String | Description |
|------|-----------|------|
| Monitor | `shape=mxgraph.azure.azure_monitor;fillColor=#0078D4;strokeColor=#ffffff;` | Monitoring service |
| Application Insights | `shape=mxgraph.azure.application_insights;fillColor=#0078D4;strokeColor=#ffffff;` | Application performance monitoring |

### 6.3 GCP Icons (`mxgraph.gcp2.*`)

GCP icons use the `mxgraph.gcp2` namespace. GCP services uniformly use brand blue `#4285F4` as the primary color.

#### Compute — `fillColor=#4285F4`

| Service | Style String | Description |
|------|-----------|------|
| Compute Engine | `shape=mxgraph.gcp2.compute_engine;fillColor=#4285F4;strokeColor=#ffffff;` | Virtual machine instances |
| Cloud Functions | `shape=mxgraph.gcp2.cloud_functions;fillColor=#4285F4;strokeColor=#ffffff;` | Serverless functions |
| Cloud Run | `shape=mxgraph.gcp2.cloud_run;fillColor=#4285F4;strokeColor=#ffffff;` | Serverless containers |
| GKE | `shape=mxgraph.gcp2.google_kubernetes_engine;fillColor=#4285F4;strokeColor=#ffffff;` | Kubernetes engine |
| App Engine | `shape=mxgraph.gcp2.app_engine;fillColor=#4285F4;strokeColor=#ffffff;` | Application engine |

#### Storage — `fillColor=#4285F4`

| Service | Style String | Description |
|------|-----------|------|
| Cloud Storage | `shape=mxgraph.gcp2.cloud_storage;fillColor=#4285F4;strokeColor=#ffffff;` | Object storage |
| Persistent Disk | `shape=mxgraph.gcp2.persistent_disk;fillColor=#4285F4;strokeColor=#ffffff;` | Persistent disk |
| Filestore | `shape=mxgraph.gcp2.filestore;fillColor=#4285F4;strokeColor=#ffffff;` | File storage |

#### Database — `fillColor=#4285F4`

| Service | Style String | Description |
|------|-----------|------|
| Cloud SQL | `shape=mxgraph.gcp2.cloud_sql;fillColor=#4285F4;strokeColor=#ffffff;` | Relational database |
| Cloud Spanner | `shape=mxgraph.gcp2.cloud_spanner;fillColor=#4285F4;strokeColor=#ffffff;` | Globally distributed database |
| Firestore | `shape=mxgraph.gcp2.cloud_firestore;fillColor=#4285F4;strokeColor=#ffffff;` | NoSQL document database |
| Bigtable | `shape=mxgraph.gcp2.cloud_bigtable;fillColor=#4285F4;strokeColor=#ffffff;` | Wide-column NoSQL database |
| Memorystore | `shape=mxgraph.gcp2.cloud_memorystore;fillColor=#4285F4;strokeColor=#ffffff;` | Cache service |
| BigQuery | `shape=mxgraph.gcp2.bigquery;fillColor=#4285F4;strokeColor=#ffffff;` | Data warehouse and analytics |

#### Networking — `fillColor=#4285F4`

| Service | Style String | Description |
|------|-----------|------|
| VPC Network | `shape=mxgraph.gcp2.virtual_private_cloud;fillColor=#4285F4;strokeColor=#ffffff;` | Virtual private cloud |
| Cloud Load Balancing | `shape=mxgraph.gcp2.cloud_load_balancing;fillColor=#4285F4;strokeColor=#ffffff;` | Load balancing |
| Cloud CDN | `shape=mxgraph.gcp2.cloud_cdn;fillColor=#4285F4;strokeColor=#ffffff;` | Content delivery network |
| Cloud DNS | `shape=mxgraph.gcp2.cloud_dns;fillColor=#4285F4;strokeColor=#ffffff;` | DNS service |
| Cloud Armor | `shape=mxgraph.gcp2.cloud_armor;fillColor=#4285F4;strokeColor=#ffffff;` | Web application protection |

#### Security — `fillColor=#4285F4`

| Service | Style String | Description |
|------|-----------|------|
| IAM | `shape=mxgraph.gcp2.cloud_iam;fillColor=#4285F4;strokeColor=#ffffff;` | Identity and access management |
| KMS | `shape=mxgraph.gcp2.cloud_key_management_service;fillColor=#4285F4;strokeColor=#ffffff;` | Key management |
| Secret Manager | `shape=mxgraph.gcp2.secret_manager;fillColor=#4285F4;strokeColor=#ffffff;` | Secrets management |

#### Messaging & Integration — `fillColor=#4285F4`

| Service | Style String | Description |
|------|-----------|------|
| Pub/Sub | `shape=mxgraph.gcp2.cloud_pubsub;fillColor=#4285F4;strokeColor=#ffffff;` | Message queue |
| Cloud Tasks | `shape=mxgraph.gcp2.cloud_tasks;fillColor=#4285F4;strokeColor=#ffffff;` | Task queue |

#### Monitoring — `fillColor=#4285F4`

| Service | Style String | Description |
|------|-----------|------|
| Cloud Monitoring | `shape=mxgraph.gcp2.cloud_monitoring;fillColor=#4285F4;strokeColor=#ffffff;` | Monitoring service |
| Cloud Logging | `shape=mxgraph.gcp2.cloud_logging;fillColor=#4285F4;strokeColor=#ffffff;` | Logging service |

### 6.4 AWS Service Category Color Quick Reference

AWS service categories use different official brand colors for quick visual distinction of service types in architecture diagrams:

| Service Category | fillColor | Color Description |
|----------|-----------|----------|
| Compute | `#ED7100` | Orange |
| Storage | `#3F8624` | Green |
| Database | `#C925D1` | Purple |
| Networking | `#8C4FFF` | Blue-purple |
| Security | `#DD344C` | Red |
| Application Integration | `#E7157B` | Pink |
| AI / ML | `#01A88D` | Teal |

### 6.5 Cloud Icon Usage Example

The following example demonstrates how to use cloud icons in architecture diagrams:

```xml
<mxCell id="aws-alb" value="ALB" 
        style="shape=mxgraph.aws4.application_load_balancer;whiteSpace=wrap;html=1;fillColor=#8C4FFF;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;" 
        vertex="1" parent="1">
  <mxGeometry x="100" y="200" width="60" height="60" as="geometry"/>
</mxCell>
<mxCell id="aws-ec2" value="Web Server" 
        style="shape=mxgraph.aws4.ec2;whiteSpace=wrap;html=1;fillColor=#ED7100;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;" 
        vertex="1" parent="1">
  <mxGeometry x="300" y="200" width="60" height="60" as="geometry"/>
</mxCell>
<mxCell id="aws-rds" value="MySQL" 
        style="shape=mxgraph.aws4.rds;whiteSpace=wrap;html=1;fillColor=#C925D1;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;" 
        vertex="1" parent="1">
  <mxGeometry x="500" y="200" width="60" height="60" as="geometry"/>
</mxCell>
```

## 7. Containers & Grouping

Containers are the core mechanism for logical grouping in draw.io. When an mxCell serves as the parent of other mxCells, it must be declared as a container. Containers are widely used for logical grouping in cloud architecture diagrams such as VPCs, subnets, and availability zones, as well as for layer division in architecture diagrams.

### 7.1 Container Core Rules

#### container=1 Attribute (Required)

Any mxCell that serves as a parent element (i.e., other mxCells have their `parent` attribute pointing to its `id`) **must** include `container=1` in its style string. Missing this attribute will cause child elements to not correctly follow the container during move and resize operations.

#### pointerEvents=0 Attribute (Required for non-swimlane containers)

For regular containers that do not use the `swimlane` style (e.g., VPC, subnets, logical grouping), the style string **should** include `pointerEvents=0`. This attribute allows mouse clicks to pass through the container background and directly select child elements inside the container.

> **Rule summary**:
> - `swimlane` containers: `container=1` (`pointerEvents=0` not needed, as swimlane has its own title bar interaction)
> - Non-swimlane containers: `container=1;pointerEvents=0;`

#### Correct Example

```xml
<mxCell id="vpc-1" value="VPC (10.0.0.0/16)"
        style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;strokeColor=#6C8EBF;dashed=1;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=10;"
        vertex="1" parent="1">
  <mxGeometry x="40" y="40" width="600" height="400" as="geometry"/>
</mxCell>
```

#### Incorrect Example (missing container=1)

```xml
<mxCell id="vpc-1" value="VPC (10.0.0.0/16)"
        style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#6C8EBF;dashed=1;"
        vertex="1" parent="1">
  <mxGeometry x="40" y="40" width="600" height="400" as="geometry"/>
</mxCell>
```

### 7.2 Child Element Relative Coordinate Rules

> **CRITICAL**: Child elements inside containers use coordinates relative to the parent container's top-left corner, not the canvas origin.

When an mxCell's `parent` attribute points to a container, the `x` and `y` coordinates in that child element's `<mxGeometry>` are offsets relative to the parent container's top-left corner `(0, 0)`.

#### Coordinate Calculation Example

Assuming a container is at canvas coordinates `(100, 200)`, and a child element inside the container needs to be placed at offset `(30, 50)` within the container:

- Container mxGeometry: `x="100" y="200" width="400" height="300"`
- Child element mxGeometry: `x="30" y="50"` (relative to container top-left corner)
- Child element's actual position on canvas: `(100+30, 200+50)` = `(130, 250)`

```xml
<mxCell id="container-1" value="Container"
        style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;dashed=1;strokeColor=#666666;"
        vertex="1" parent="1">
  <mxGeometry x="100" y="200" width="400" height="300" as="geometry"/>
</mxCell>
<mxCell id="child-1" value="Child Element"
        style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"
        vertex="1" parent="container-1">
  <mxGeometry x="30" y="50" width="120" height="60" as="geometry"/>
</mxCell>
```

> **Common mistake**: Using canvas absolute coordinates as child element coordinates. If a child element's `parent` points to a container but coordinates use canvas absolute values, the child element will appear at an incorrect position outside the container.

### 7.3 Container Style Reference

The following are container style templates for different purposes:

#### VPC Container

```
rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;strokeColor=#6C8EBF;dashed=1;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=10;
```

#### Subnet Container

```
rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=#DAE8FC;fillOpacity=20;strokeColor=#6C8EBF;dashed=1;dashPattern=8 4;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=8;
```

#### Availability Zone Container

```
rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=#D5E8D4;fillOpacity=15;strokeColor=#82B366;dashed=1;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=8;
```

#### Logical Grouping Container (General)

```
rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;strokeColor=#666666;dashed=1;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=10;
```

#### Security Group / Firewall Boundary

```
rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;strokeColor=#B85450;dashed=1;dashPattern=12 4;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=8;
```

### 7.4 Container Nesting

Containers can be nested to form multi-level logical groupings. When nesting, every layer of container must include the `container=1` attribute, and child container coordinates are relative to their direct parent container.

#### Nesting Hierarchy Example

```
Canvas (parent="1")
  └── VPC Container (parent="1", container=1)
        ├── Public Subnet Container (parent="vpc-1", container=1)
        │     ├── ALB Icon (parent="subnet-pub")
        │     └── NAT Gateway Icon (parent="subnet-pub")
        └── Private Subnet Container (parent="vpc-1", container=1)
              ├── EC2 Instance (parent="subnet-priv")
              └── RDS Instance (parent="subnet-priv")
```

### 7.5 VPC Architecture Diagram Complete Example

The following example demonstrates a typical AWS VPC architecture with a VPC container, two availability zones, public/private subnets, and internal service icons:

```xml
<mxfile>
  <diagram id="vpc-architecture-1" name="AWS VPC Architecture">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="1100" pageHeight="850"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="vpc-1" value="VPC (10.0.0.0/16)"
                style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;strokeColor=#6C8EBF;dashed=1;fontSize=14;fontStyle=1;verticalAlign=top;spacingTop=10;"
                vertex="1" parent="1">
          <mxGeometry x="40" y="80" width="920" height="600" as="geometry"/>
        </mxCell>
        <mxCell id="az-1" value="Availability Zone A (ap-northeast-1a)"
                style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=#D5E8D4;fillOpacity=15;strokeColor=#82B366;dashed=1;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=8;"
                vertex="1" parent="vpc-1">
          <mxGeometry x="20" y="40" width="420" height="540" as="geometry"/>
        </mxCell>
        <mxCell id="subnet-pub-1" value="Public Subnet (10.0.1.0/24)"
                style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=#DAE8FC;fillOpacity=20;strokeColor=#6C8EBF;dashed=1;dashPattern=8 4;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;"
                vertex="1" parent="az-1">
          <mxGeometry x="20" y="40" width="380" height="200" as="geometry"/>
        </mxCell>
        <mxCell id="alb-1" value="ALB"
                style="shape=mxgraph.aws4.application_load_balancer;whiteSpace=wrap;html=1;fillColor=#8C4FFF;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;"
                vertex="1" parent="subnet-pub-1">
          <mxGeometry x="50" y="60" width="60" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="nat-1" value="NAT GW"
                style="shape=mxgraph.aws4.nat_gateway;whiteSpace=wrap;html=1;fillColor=#8C4FFF;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;"
                vertex="1" parent="subnet-pub-1">
          <mxGeometry x="250" y="60" width="60" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="subnet-priv-1" value="Private Subnet (10.0.2.0/24)"
                style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=#FFE6CC;fillOpacity=20;strokeColor=#D6B656;dashed=1;dashPattern=8 4;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;"
                vertex="1" parent="az-1">
          <mxGeometry x="20" y="280" width="380" height="230" as="geometry"/>
        </mxCell>
        <mxCell id="ec2-1" value="EC2"
                style="shape=mxgraph.aws4.ec2;whiteSpace=wrap;html=1;fillColor=#ED7100;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;"
                vertex="1" parent="subnet-priv-1">
          <mxGeometry x="50" y="60" width="60" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="rds-1" value="RDS"
                style="shape=mxgraph.aws4.rds;whiteSpace=wrap;html=1;fillColor=#C925D1;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;"
                vertex="1" parent="subnet-priv-1">
          <mxGeometry x="250" y="60" width="60" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="az-2" value="Availability Zone B (ap-northeast-1c)"
                style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=#D5E8D4;fillOpacity=15;strokeColor=#82B366;dashed=1;fontSize=12;fontStyle=1;verticalAlign=top;spacingTop=8;"
                vertex="1" parent="vpc-1">
          <mxGeometry x="480" y="40" width="420" height="540" as="geometry"/>
        </mxCell>
        <mxCell id="subnet-pub-2" value="Public Subnet (10.0.3.0/24)"
                style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=#DAE8FC;fillOpacity=20;strokeColor=#6C8EBF;dashed=1;dashPattern=8 4;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;"
                vertex="1" parent="az-2">
          <mxGeometry x="20" y="40" width="380" height="200" as="geometry"/>
        </mxCell>
        <mxCell id="alb-2" value="ALB"
                style="shape=mxgraph.aws4.application_load_balancer;whiteSpace=wrap;html=1;fillColor=#8C4FFF;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;"
                vertex="1" parent="subnet-pub-2">
          <mxGeometry x="160" y="60" width="60" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="subnet-priv-2" value="Private Subnet (10.0.4.0/24)"
                style="rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=#FFE6CC;fillOpacity=20;strokeColor=#D6B656;dashed=1;dashPattern=8 4;fontSize=11;fontStyle=1;verticalAlign=top;spacingTop=8;"
                vertex="1" parent="az-2">
          <mxGeometry x="20" y="280" width="380" height="230" as="geometry"/>
        </mxCell>
        <mxCell id="ec2-2" value="EC2"
                style="shape=mxgraph.aws4.ec2;whiteSpace=wrap;html=1;fillColor=#ED7100;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;"
                vertex="1" parent="subnet-priv-2">
          <mxGeometry x="50" y="60" width="60" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="rds-2" value="RDS (Read Replica)"
                style="shape=mxgraph.aws4.rds;whiteSpace=wrap;html=1;fillColor=#C925D1;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;"
                vertex="1" parent="subnet-priv-2">
          <mxGeometry x="250" y="60" width="60" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="edge-alb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="alb-1" target="ec2-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-ec2-rds" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="ec2-1" target="rds-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-rds-replica" value="Replication" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;" edge="1" parent="1" source="rds-1" target="rds-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Example key points:

| Key Point | Description |
|------|------|
| VPC container | `parent="1"`, outermost container, blue dashed border, annotated with CIDR address |
| Availability zone containers | `parent="vpc-1"`, nested inside VPC, green dashed border, coordinates relative to VPC top-left corner |
| Subnet containers | `parent="az-1"` or `parent="az-2"`, nested inside availability zones, coordinates relative to availability zone top-left corner |
| Service icons | `parent="subnet-pub-1"` etc., nested inside subnets, coordinates relative to subnet top-left corner |
| Cross-container connection lines | Edge `parent="1"` (default layer), `source` and `target` can reference child elements in different containers |
| Container nesting levels | Canvas → VPC → Availability Zone → Subnet → Service Icon (4 levels of nesting) |
| Every level has `container=1` | VPC, availability zone, and subnet container styles all include `container=1;pointerEvents=0;` |
| Relative coordinates calculated per level | Each child element's coordinates are only relative to its direct parent container, no need to consider higher-level container positions |

## 8. Edge Routing & Layout Guidelines

### 8.1 Default Routing Style

All connection lines (edges) default to the orthogonal routing style `edgeStyle=orthogonalEdgeStyle`, meaning connection lines extend only horizontally and vertically, producing right-angle bends when direction changes are needed.

Standard edge style string:

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;
```

Attribute description:

| Attribute | Value | Description |
|------|-----|------|
| `edgeStyle` | `orthogonalEdgeStyle` | Orthogonal routing, connection lines extend only horizontally/vertically with right-angle bends |
| `orthogonalLoop` | `1` | Enable orthogonal loop support (self-connecting edges) |
| `jettySize` | `auto` | Automatically calculate the short straight-line segment length extending from the node |
| `rounded` | `0` or `1` | Whether to use rounded corners at bends, `1` makes bends smoother |

> **Rule**: Unless there are special routing requirements (e.g., ER diagrams using `entityRelationEdgeStyle`, curved connections using `curved=1`), all edges must use `edgeStyle=orthogonalEdgeStyle`.

### 8.2 Final Straight Segment Length Rule

The final straight segment of a connection line (the straight portion between the last bend point and the target node) must be at least 20px long to ensure the arrow can be fully displayed without overlapping the node border.

#### Why 20px Minimum Length Is Needed

- draw.io's default arrow (`endArrow=classic`) occupies approximately 10–14px in length
- If the final straight segment is too short, the arrow will be clipped or overlap with the node border, causing visual confusion
- A 20px minimum length provides sufficient rendering space for the arrow

#### How to Ensure Sufficient Final Straight Segment Length

1. **Reasonable node spacing**: Maintain at least 60px spacing between nodes (see Section 8.5), which naturally satisfies this requirement
2. **Explicit waypoints**: When connection line paths are complex, add waypoints to ensure the last straight segment is long enough
3. **Connection point position selection**: Choose appropriate `entryX/Y` positions so the connection line enters the target node from the correct direction

### 8.3 Connection Point Distribution Strategy

When multiple connection lines connect to the same node, use `exitX/Y` and `entryX/Y` attributes to distribute connection points across different sides of the node, avoiding connection line overlap and crossing.

#### Connection Point Position Reference

Node connection points use a relative coordinate system, where `(0,0)` is the top-left corner and `(1,1)` is the bottom-right corner:

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

#### Distribution Strategy Rules

1. **Single connection line**: Use the center point of the node side (e.g., `exitX=0.5;exitY=1` exits from bottom center)
2. **Two connection lines on the same side**: Distribute connection points to `0.25` and `0.75` positions
3. **Three or more**: Evenly distribute connection points along that side, or distribute across different sides
4. **Prefer different sides**: If connection lines go in different directions, prioritize assigning them to different sides of the node (top, bottom, left, right)

#### Distribution Strategy Example

Scenario: Node A needs to connect rightward to Node B and Node C (B is upper-right, C is lower-right)

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

In this example, both edges exit from the right side of Node A, but use `exitY=0.25` (upper-right) and `exitY=0.75` (lower-right) respectively, avoiding overlap at the exit points.

### 8.4 Explicit Waypoint Usage Guide

When automatic routing cannot produce an ideal connection line path (e.g., needing to avoid other nodes, preventing connection line overlap), explicit waypoints can be added inside `<mxGeometry>` to precisely control the connection line path.

#### Waypoint XML Structure

Waypoints are defined by wrapping a set of `<mxPoint>` elements inside an `<Array as="points">` element:

```xml
<mxCell id="edge-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
        edge="1" parent="1" source="node-a" target="node-b">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="400" y="200"/>
      <mxPoint x="400" y="350"/>
    </Array>
  </mxGeometry>
</mxCell>
```

#### Waypoint Rules

| Rule | Description |
|------|------|
| Position | `<Array as="points">` must be nested inside `<mxGeometry relative="1" as="geometry">` |
| Coordinate system | Waypoint `x`, `y` use canvas absolute coordinates (not affected by containers) |
| Alignment | Waypoint coordinates should be aligned to multiples of 10, consistent with the grid |
| Order | `<mxPoint>` elements are arranged in the order of the connection line path, from source node to target node |
| Quantity | Use the minimum number of waypoints possible, avoiding over-control that leads to unnatural paths |

#### When to Use Waypoints

1. **Avoiding obstacles**: Connection line needs to route around intermediate nodes or containers
2. **Avoiding overlap**: Multiple parallel connection lines need staggered paths
3. **Forcing path direction**: Connection line needs to follow a specific path (e.g., go down first then right)
4. **Complex layouts**: Irregular node distribution where automatic routing produces unattractive paths

#### Complete Waypoint Example

The following example demonstrates a connection line that needs to route around an intermediate node:

```xml
<mxCell id="node-a" value="Service A" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="node-obstacle" value="Intermediate Service" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;" vertex="1" parent="1">
  <mxGeometry x="350" y="100" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="node-b" value="Service B" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;" vertex="1" parent="1">
  <mxGeometry x="600" y="100" width="120" height="60" as="geometry"/>
</mxCell>
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

In this example, the connection line from "Service A" to "Service B" routes downward via two waypoints, bypassing the "Intermediate Service" node.

### 8.5 Grid Alignment & Spacing Rules

#### Grid Alignment

In the `<mxGeometry>` of all vertex type mxCells, the `x` and `y` coordinate values must be multiples of 10. This ensures nodes are precisely aligned to draw.io's grid, keeping the diagram neat and orderly.

| Rule | Description | Correct Examples | Incorrect Examples |
|------|------|----------|----------|
| X coordinate | Must be a multiple of 10 | `x="100"`, `x="250"`, `x="0"` | `x="105"`, `x="237"` |
| Y coordinate | Must be a multiple of 10 | `y="200"`, `y="80"`, `y="0"` | `y="123"`, `y="45"` |
| Width/Height | Recommended to be multiples of 10 | `width="120"`, `height="60"` | `width="115"` |

#### Minimum Spacing

The distance between bounding boxes of any two vertex nodes under the same parent container must be at least 60px. This ensures sufficient space between nodes to accommodate connection lines and label text.

Spacing calculation method:

```
Node A: x=100, y=100, width=120, height=60
  → Right boundary = 100 + 120 = 220
  → Bottom boundary = 100 + 60 = 160

Node B: x=300, y=100, width=120, height=60
  → Left boundary = 300

Horizontal spacing = Node B left boundary - Node A right boundary = 300 - 220 = 80px ✓ (≥ 60px)
```

#### Recommended Spacing

For optimal visual appearance and readability, the following spacing is recommended:

| Direction | Recommended Spacing | Description |
|------|----------|------|
| Horizontal spacing | 200px | Recommended distance between horizontally adjacent nodes |
| Vertical spacing | 120px | Recommended distance between vertically adjacent nodes |

Recommended spacing applies to standard-sized nodes (120×60). For larger nodes or nodes with more text, spacing should be increased accordingly.

#### Layout Calculation Example

The following example demonstrates coordinate calculation for a 3×2 grid layout:

```
Standard node size: 120×60
Horizontal spacing: 200px
Vertical spacing: 120px

Row 1:
  Node (0,0): x=100, y=100
  Node (1,0): x=100+120+200=420, y=100
  Node (2,0): x=420+120+200=740, y=100

Row 2:
  Node (0,1): x=100, y=100+60+120=280
  Node (1,1): x=420, y=280
  Node (2,1): x=740, y=280
```

#### Spacing Rules Summary

| Rule | Value | Priority |
|------|-----|--------|
| Coordinate alignment | Multiples of 10 | **Required** |
| Minimum spacing | 60px | **Required** |
| Recommended horizontal spacing | 200px | Recommended |
| Recommended vertical spacing | 120px | Recommended |