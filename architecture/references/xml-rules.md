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

#### Edge

Edges represent connection lines. They must include the `edge="1"` attribute.

> **CRITICAL**: Every edge mxCell must contain a `<mxGeometry relative="1" as="geometry"/>` child element.

```xml
<mxCell id="{unique-id}" value="{label}" 
        style="{style-string}" 
        edge="1" parent="{parent-id}" 
        source="{source-id}" target="{target-id}">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

#### vertex and edge Are Mutually Exclusive

The `vertex="1"` and `edge="1"` attributes are mutually exclusive; a single mxCell cannot have both attributes simultaneously.

#### ID Uniqueness

All mxCell `id` attribute values must be unique within the same `<diagram>`. Use meaningful prefix + incremental number naming (e.g., `node-1`, `edge-1`, `container-1`).

### 3.3 Prohibited Rules

- No XML comments (`<!-- -->`)
- No compression or Base64 encoding

### 3.4 Special Character Escaping

| Original Character | Escaped Form |
|----------|----------|
| `&` | `&amp;` |
| `<` | `&lt;` |
| `>` | `&gt;` |
| `"` | `&quot;` |

### 3.5 Dark Mode Support

`<mxGraphModel>` must include `adaptiveColors="auto"`.

### 3.6 XML Compliance Self-Check Checklist

| # | Check Item |
|---|--------|
| 1 | Root element is `<mxfile>` |
| 2 | Contains `<mxCell id="0"/>` and `<mxCell id="1" parent="0"/>` |
| 3 | All IDs are unique |
| 4 | Every edge contains `<mxGeometry relative="1" as="geometry"/>` |
| 5 | vertex and edge are mutually exclusive |
| 6 | No XML comments |
| 7 | Special characters are escaped |
| 8 | Coordinates aligned to multiples of 10 |
| 9 | `adaptiveColors="auto"` present |
| 10 | Text nodes have `whiteSpace=wrap` |
| 11 | Containers have `container=1` |
| 12 | Child elements use relative coordinates |
