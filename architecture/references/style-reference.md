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
| `rounded` | `0` / `1` | `0` | Rounded rectangle, `1` enables rounded corners |
| `fillColor` | Color value | `#FFFFFF` | Fill color, e.g., `#DAE8FC`, `#D5E8D4` |
| `strokeColor` | Color value | `#000000` | Border color, e.g., `#6C8EBF`, `#82B366` |
| `fontColor` | Color value | `#000000` | Text color, e.g., `#333333` |
| `fontSize` | Number | `12` | Font size (pixels) |
| `fontStyle` | Number | `0` | `0` normal, `1` bold, `2` italic, `3` bold italic, `4` underline |
| `align` | `left` / `center` / `right` | `center` | Horizontal alignment |
| `verticalAlign` | `top` / `middle` / `bottom` | `middle` | Vertical alignment |
| `overflow` | `hidden` / `fill` / `visible` | `hidden` | Text overflow handling |
| `shadow` | `0` / `1` | `0` | Shadow effect |
| `opacity` | `0`–`100` | `100` | Opacity |
| `arcSize` | Number | `10` | Corner radius (only effective when `rounded=1`) |
| `spacingTop` | Number | `0` | Additional top padding |
| `spacingBottom` | Number | `0` | Additional bottom padding |
| `spacingLeft` | Number | `0` | Additional left padding |
| `spacingRight` | Number | `0` | Additional right padding |

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

#### Routing Styles

| Attribute | Value | Description |
|------|-----|------|
| `edgeStyle` | `orthogonalEdgeStyle` | **Default routing style**, uses orthogonal (right-angle bend) paths |
| `edgeStyle` | `entityRelationEdgeStyle` | ER diagram relationship line routing |
| `edgeStyle` | `elbowEdgeStyle` | Elbow routing (single bend) |
| `curved` | `0` / `1` | Curved routing, `1` enables smooth curves |
| `rounded` | `0` / `1` | Rounded bends at corners |

#### Connection Point Control

Connection point attributes control where an edge exits the source node and enters the target node. Values range from `0` to `1`, representing relative positions on the node boundary:

| Attribute | Value Range | Description |
|------|--------|------|
| `exitX` | `0`–`1` | Source node exit point X (`0`=left, `0.5`=center, `1`=right) |
| `exitY` | `0`–`1` | Source node exit point Y (`0`=top, `0.5`=center, `1`=bottom) |
| `exitDx` | Number | Exit point X offset (pixels) |
| `exitDy` | Number | Exit point Y offset (pixels) |
| `entryX` | `0`–`1` | Target node entry point X (`0`=left, `0.5`=center, `1`=right) |
| `entryY` | `0`–`1` | Target node entry point Y (`0`=top, `0.5`=center, `1`=bottom) |
| `entryDx` | Number | Entry point X offset (pixels) |
| `entryDy` | Number | Entry point Y offset (pixels) |

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
| `startArrow` | (same as above) | Start-end arrow, values same as `endArrow` |
| `endFill` | `0` / `1` | Whether the end arrow is filled (`0`=open, `1`=filled) |
| `startFill` | `0` / `1` | Whether the start arrow is filled |

#### Line Styles

| Attribute | Value | Description |
|------|-----|------|
| `strokeWidth` | Number | Line width (pixels), default `1` |
| `strokeColor` | Color value | Line color |
| `dashed` | `0` / `1` | Dashed line style |
| `dashPattern` | String | Dash pattern, e.g., `8 8` (8px line + 8px gap) |
| `opacity` | `0`–`100` | Line opacity |

#### Standard Edge Style Strings

```
Default orthogonal edge:
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;

Dashed edge:
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;

No-arrow bidirectional:
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;startArrow=none;

UML inheritance (open triangle arrow):
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;

UML realization (dashed + open triangle):
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;dashed=1;

UML composition (filled diamond):
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=diamondThin;startFill=1;endArrow=open;endFill=0;

UML aggregation (open diamond):
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=diamondThin;startFill=0;endArrow=open;endFill=0;

ER one-to-many:
edgeStyle=entityRelationEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;
```

### 4.5 Color Scheme Guidelines

#### Core Principles

1. **Consistent coloring for same-type elements**: Within the same diagram, elements of the same type must use the same `fillColor` and `strokeColor`
2. **Level differentiation**: Elements at different levels or categories use different fill colors
3. **Contrast**: Ensure sufficient contrast between `fontColor` and `fillColor`
4. **Color restraint**: Use no more than 5–7 color varieties in a single diagram

#### Recommended Color Schemes

| Color Series | fillColor | strokeColor | fontColor | Use |
|------|-----------|-----------|-----------|------|
| Blue | `#DAE8FC` | `#6C8EBF` | `#333333` | Primary elements / Service components |
| Green | `#D5E8D4` | `#82B366` | `#333333` | Success states / Data storage |
| Orange | `#FFE6CC` | `#D6B656` | `#333333` | Warnings / Processing steps |
| Red | `#F8CECC` | `#B85450` | `#333333` | Errors / Critical paths |
| Purple | `#E1D5E7` | `#9673A6` | `#333333` | External systems / Third-party |
| Gray | `#F5F5F5` | `#666666` | `#333333` | Auxiliary elements / Annotations |
| Dark Fill | `#6C8EBF` | `#6C8EBF` | `#FFFFFF` | Start/end nodes / Emphasis elements |

#### Level-Based Coloring Rules

| Level | Color Scheme | Example Use |
|------|------|----------|
| Level 1 (Highest) | Blue `fillColor=#DAE8FC;strokeColor=#6C8EBF;` | System/Platform layer |
| Level 2 | Green `fillColor=#D5E8D4;strokeColor=#82B366;` | Service/Module layer |
| Level 3 | Orange `fillColor=#FFE6CC;strokeColor=#D6B656;` | Component/Feature layer |
| Level 4 | Purple `fillColor=#E1D5E7;strokeColor=#9673A6;` | Sub-component/Tool layer |
| Container/Group | No fill `fillColor=none;strokeColor=#666666;dashed=1;` | VPC, subnets, logical grouping |

#### Diagram Type-Specific Coloring

**Flowchart:**

| Element Type | Color Scheme |
|----------|------|
| Start/End nodes | `fillColor=#6C8EBF;strokeColor=#6C8EBF;fontColor=#FFFFFF;` |
| Processing steps | `fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;` |
| Decision nodes | `fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;` |
| Error handling | `fillColor=#F8CECC;strokeColor=#B85450;fontColor=#333333;` |

**UML class diagram:**

| Element Type | Color Scheme |
|----------|------|
| Regular class | `fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;` |
| Abstract class | `fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;` |
| Interface | `fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;` |

**ER diagram:**

| Element Type | Color Scheme |
|----------|------|
| Entity 1 (e.g., User) | `fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;` |
| Entity 2 (e.g., Order) | `fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;` |
| Entity 3 (e.g., Product) | `fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;` |
| PK row | `strokeColor=none;fillColor=none;fontColor=#333333;fontStyle=4;` (underline) |
| FK row | `strokeColor=none;fillColor=none;fontColor=#333333;fontStyle=2;` (italic) |

### 4.6 whiteSpace=wrap Auto-Wrap Rule

> **CRITICAL**: All vertex type mxCells containing text (non-empty `value`) **must** include `whiteSpace=wrap` in their style string.

---
