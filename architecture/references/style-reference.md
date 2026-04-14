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

| Attribute | Value Type | Default | Description |
|------|--------|--------|------|
| `html` | `1` | — | Enable HTML label rendering, **must be included in all nodes** |
| `whiteSpace` | `wrap` | — | Auto text wrapping, **must be included in all vertex nodes containing text** |
| `rounded` | `0` / `1` | `0` | Rounded rectangle |
| `fillColor` | Color value | `#FFFFFF` | Fill color |
| `strokeColor` | Color value | `#000000` | Border color |
| `fontColor` | Color value | `#000000` | Text color |
| `fontSize` | Number | `12` | Font size (pixels) |
| `fontStyle` | Number | `0` | `0` normal, `1` bold, `2` italic, `3` bold italic, `4` underline |
| `align` | `left` / `center` / `right` | `center` | Horizontal alignment |
| `verticalAlign` | `top` / `middle` / `bottom` | `middle` | Vertical alignment |

### 4.3 Shape Type Reference

#### Basic Shapes

| Shape | Style String | Recommended Size | Typical Use |
|------|-----------|----------|----------|
| Rectangle | `rounded=0;whiteSpace=wrap;html=1;` | 120×60 | General nodes |
| Rounded Rectangle | `rounded=1;whiteSpace=wrap;html=1;` | 120×60 | Flowchart steps, services |
| Ellipse | `ellipse;whiteSpace=wrap;html=1;` | 120×60 | Start/end nodes |
| Diamond | `rhombus;whiteSpace=wrap;html=1;` | 120×80 | Decision nodes |
| Cloud | `ellipse;shape=cloud;whiteSpace=wrap;html=1;` | 120×80 | Cloud services |
| Cylinder | `shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;size=15;` | 60×80 | Databases |

#### Container & Grouping Shapes

| Shape | Style String |
|------|-----------|
| Swimlane | `swimlane;startSize=30;whiteSpace=wrap;html=1;container=1;` |
| Grouping Container | `rounded=1;whiteSpace=wrap;html=1;container=1;pointerEvents=0;fillColor=none;dashed=1;` |

#### UML-Specific Shapes

| Shape | Style String |
|------|-----------|
| UML Class | `swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;` |
| UML Divider | `line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;` |
| Lifeline | `shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;` |
| Initial State | `ellipse;html=1;shape=mxgraph.flowchart.start_2;fontSize=12;fillColor=#000000;fontColor=#FFFFFF;whiteSpace=wrap;` |
| Final State | `ellipse;html=1;shape=doubleCircle;whiteSpace=wrap;aspect=fixed;fillColor=#000000;fontColor=#FFFFFF;` |

#### ER Diagram-Specific Shapes

| Shape | Style String |
|------|-----------|
| Entity | `swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;` |
| PK Row | `text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontStyle=4;` |
| FK Row | `text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontStyle=2;` |
| ER Relationship (1:N) | `edgeStyle=entityRelationEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;` |

### 4.4 Edge/Connection Line Style Attributes

#### Standard Edge Style Strings

```
Default orthogonal edge:
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;

Dashed edge:
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;

No-arrow bidirectional:
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;startArrow=none;

UML inheritance:
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;

ER one-to-many:
edgeStyle=entityRelationEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;
```

### 4.5 Color Scheme Guidelines

| Color Series | fillColor | strokeColor | Use |
|------|-----------|-----------|------|
| Blue | `#DAE8FC` | `#6C8EBF` | Primary elements |
| Green | `#D5E8D4` | `#82B366` | Success / Data storage |
| Orange | `#FFE6CC` | `#D6B656` | Warnings / Processing |
| Red | `#F8CECC` | `#B85450` | Errors / Critical |
| Purple | `#E1D5E7` | `#9673A6` | External systems |
| Gray | `#F5F5F5` | `#666666` | Auxiliary elements |
| Dark Fill | `#6C8EBF` | `#6C8EBF` | Start/end emphasis (fontColor=#FFFFFF) |

### 4.6 whiteSpace=wrap Auto-Wrap Rule

> **CRITICAL**: All vertex type mxCells containing text (non-empty `value`) **must** include `whiteSpace=wrap` in their style string.

---
