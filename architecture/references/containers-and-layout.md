## 7. Containers & Grouping

Containers are the core mechanism for logical grouping in draw.io. When an mxCell serves as the parent of other mxCells, it must be declared as a container.

### 7.1 Container Core Rules

#### container=1 Attribute (Required)

Any mxCell that serves as a parent element **must** include `container=1` in its style string.

#### pointerEvents=0 Attribute (Required for non-swimlane containers)

For regular containers that do not use the `swimlane` style, include `pointerEvents=0`.

> **Rule summary**:
> - `swimlane` containers: `container=1`
> - Non-swimlane containers: `container=1;pointerEvents=0;`

### 7.2 Child Element Relative Coordinate Rules

> **CRITICAL**: Child elements inside containers use coordinates relative to the parent container's top-left corner, not the canvas origin.

### 7.3 Container Style Reference

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

Containers can be nested. Every layer must include `container=1`, and child container coordinates are relative to their direct parent.

```
Canvas (parent="1")
  └── VPC Container (parent="1", container=1)
        ├── Public Subnet (parent="vpc-1", container=1)
        │     ├── ALB Icon (parent="subnet-pub")
        │     └── NAT Gateway (parent="subnet-pub")
        └── Private Subnet (parent="vpc-1", container=1)
              ├── EC2 Instance (parent="subnet-priv")
              └── RDS Instance (parent="subnet-priv")
```

### 7.5 VPC Architecture Diagram Complete Example

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
        <mxCell id="az-1" value="Availability Zone A"
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
        <mxCell id="edge-alb" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="alb-1" target="ec2-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-ec2-rds" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="ec2-1" target="rds-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## 8. Edge Routing & Layout Guidelines

### 8.1 Default Routing Style

All edges default to orthogonal routing:

```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;
```

### 8.2 Final Straight Segment Length Rule

The final straight segment must be at least **20px** long to ensure the arrow renders cleanly.

### 8.3 Connection Point Distribution Strategy

When multiple edges connect to the same node, use `exitX/Y` and `entryX/Y` to distribute connection points:

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
1. **Single edge**: Use center point (e.g., `exitX=0.5;exitY=1`).
2. **Two edges on same side**: Use `0.25` and `0.75` positions.
3. **Three or more**: Evenly distribute along the side.
4. **Prefer different sides**: Assign edges going different directions to different sides.

Example:
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

### 8.4 Explicit Waypoint Usage Guide

When automatic routing causes overlap, add explicit waypoints:

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

Waypoint rules:
- Coordinates use canvas absolute values (not affected by containers).
- Align to multiples of 10.
- Use minimum number of waypoints.
- For parallel edges, stagger by at least 30px.

### 8.5 Grid Alignment & Spacing Rules

| Rule | Value | Priority |
|------|-----|--------|
| Coordinate alignment | Multiples of 10 | **Required** |
| Minimum spacing | 60px between bounding boxes | **Required** |
| Recommended horizontal spacing | 200px | Recommended |
| Recommended vertical spacing | 120px | Recommended |

Layout calculation example (3×2 grid):
```
Standard node: 120×60, horizontal gap: 200px, vertical gap: 120px

Row 1: (100,100), (420,100), (740,100)
Row 2: (100,280), (420,280), (740,280)
```
