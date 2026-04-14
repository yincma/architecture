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
| PK Attribute Row | `text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontStyle=4;` | Primary key field (underline) |
| FK Attribute Row | `text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontStyle=2;` | Foreign key field (italic) |
| Attribute Row | `text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;` | Regular field rows of entities |
| Divider | `line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;` | Separator between PK area and regular fields |
| ER Relationship (1:N) | `edgeStyle=entityRelationEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;` | One-to-many relationship line |
| ER Relationship (M:N) | `edgeStyle=entityRelationEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmany;startFill=0;endArrow=ERmany;endFill=0;` | Many-to-many relationship line |
| ER Relationship (1:1) | `edgeStyle=entityRelationEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmandOne;endFill=0;` | One-to-one relationship line |

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
| Entity 1 (e.g., User) | `fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;` |
| Entity 2 (e.g., Order) | `fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;` |
| Entity 3 (e.g., Product) | `fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;` |
| Entity 4 (optional) | `fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;` |
| Attribute row | `strokeColor=none;fillColor=none;fontColor=#333333;` |
| PK row | `strokeColor=none;fillColor=none;fontColor=#333333;fontStyle=4;` (underline) |
| FK row | `strokeColor=none;fillColor=none;fontColor=#333333;fontStyle=2;` (italic) |
| Relationship line (1:N) | `strokeColor=#6C8EBF;` with `startArrow=ERmandOne;endArrow=ERmany;` |
| Relationship line (M:N) | `strokeColor=#9673A6;` with `startArrow=ERmany;endArrow=ERmany;` |

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

