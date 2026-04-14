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

