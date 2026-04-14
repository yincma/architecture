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
