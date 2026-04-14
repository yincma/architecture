# ER, Network, Mind Map, and Organization Chart Templates

## 5.6 ER Diagram

ER diagrams use `swimlane` style containers to represent entities, with each internal row representing a field annotated with field name, data type, and PK/FK constraints. Relationships use edges with `entityRelationEdgeStyle` routing and ER-specific arrow markers. Edge `source` and `target` point to specific attribute rows (PK or FK rows) for precise connection.

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
          <mxGeometry x="80" y="120" width="200" height="148" as="geometry"/>
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
          <mxGeometry x="430" y="80" width="200" height="174" as="geometry"/>
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
          <mxGeometry x="780" y="120" width="200" height="148" as="geometry"/>
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

Key points:

| Key Point | Description |
|------|------|
| Entity container | `swimlane;fontStyle=1;startSize=26;container=1;collapsible=0;` |
| Primary key row (PK) | Prefixed with `PK` in `value`, `fontStyle=4;` (underline), `portConstraint=eastwest` |
| Foreign key row (FK) | Prefixed with `FK` in `value`, `fontStyle=2;` (italic), `portConstraint=eastwest` |
| Regular field rows | Display field name and data type, indented with spaces |
| Divider line | `line;strokeColor=inherit;portConstraint=eastwest;` — separates PK area from regular fields |
| Relationship routing | `edgeStyle=entityRelationEdgeStyle;` — ER diagram-specific routing style |
| One-to-many | `startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;` |
| Many-to-many | `startArrow=ERmany;startFill=0;endArrow=ERmany;endFill=0;` |
| One-to-one | `startArrow=ERmandOne;startFill=0;endArrow=ERmandOne;endFill=0;` |
| Connection endpoints | Edge `source` and `target` point to specific attribute rows (PK or FK rows) |
| Entity coloring | Different entities use different color schemes (blue, green, purple) |

## 5.7 Network Topology

Network diagrams show infrastructure components and their connections. Use cloud shapes for external networks, specific shapes for devices, and container rectangles for zones.

```xml
<mxfile>
  <diagram id="network-1" name="Network Topology">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="net-1" value="Internet" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontColor=#333333;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="320" y="20" width="160" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="net-2" value="Firewall" style="shape=mxgraph.cisco.firewalls.firewall;html=1;whiteSpace=wrap;fillColor=#F8CECC;strokeColor=#B85450;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="365" y="150" width="70" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="net-3" value="Core Router" style="shape=mxgraph.cisco.routers.router;html=1;whiteSpace=wrap;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="365" y="270" width="70" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="zone-dmz" value="DMZ" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontColor=#333333;fontSize=14;verticalAlign=top;dashed=1;dashPattern=5 5;container=1;collapsible=0;" vertex="1" parent="1">
          <mxGeometry x="60" y="380" width="280" height="200" as="geometry"/>
        </mxCell>
        <mxCell id="dmz-web1" value="Web Server 1" style="shape=mxgraph.cisco.servers.standard_server;html=1;whiteSpace=wrap;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=11;" vertex="1" parent="zone-dmz">
          <mxGeometry x="30" y="60" width="50" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="dmz-web2" value="Web Server 2" style="shape=mxgraph.cisco.servers.standard_server;html=1;whiteSpace=wrap;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=11;" vertex="1" parent="zone-dmz">
          <mxGeometry x="120" y="60" width="50" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="dmz-lb" value="Load Balancer" style="shape=mxgraph.cisco.routers.router;html=1;whiteSpace=wrap;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;fontSize=11;" vertex="1" parent="zone-dmz">
          <mxGeometry x="200" y="60" width="50" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="zone-lan" value="Internal LAN" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;verticalAlign=top;dashed=1;dashPattern=5 5;container=1;collapsible=0;" vertex="1" parent="1">
          <mxGeometry x="460" y="380" width="280" height="200" as="geometry"/>
        </mxCell>
        <mxCell id="lan-app" value="App Server" style="shape=mxgraph.cisco.servers.standard_server;html=1;whiteSpace=wrap;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=11;" vertex="1" parent="zone-lan">
          <mxGeometry x="30" y="60" width="50" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="lan-db" value="Database" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#FFF2CC;strokeColor=#D6B656;fontColor=#333333;fontSize=11;" vertex="1" parent="zone-lan">
          <mxGeometry x="120" y="55" width="60" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="lan-storage" value="Storage" style="shape=mxgraph.cisco.servers.standard_server;html=1;whiteSpace=wrap;fillColor=#F8CECC;strokeColor=#B85450;fontColor=#333333;fontSize=11;" vertex="1" parent="zone-lan">
          <mxGeometry x="210" y="60" width="50" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="conn-1" style="endArrow=none;html=1;strokeColor=#666666;strokeWidth=2;" edge="1" source="net-1" target="net-2" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="conn-2" style="endArrow=none;html=1;strokeColor=#666666;strokeWidth=2;" edge="1" source="net-2" target="net-3" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="conn-3" style="endArrow=none;html=1;strokeColor=#D6B656;strokeWidth=2;" edge="1" source="net-3" target="zone-dmz" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="conn-4" style="endArrow=none;html=1;strokeColor=#6C8EBF;strokeWidth=2;" edge="1" source="net-3" target="zone-lan" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

| Key Point | Detail |
|-----------|--------|
| Cloud shape | `ellipse;shape=cloud;` |
| Firewall | `shape=mxgraph.cisco.firewalls.firewall;` |
| Router | `shape=mxgraph.cisco.routers.router;` |
| Server | `shape=mxgraph.cisco.servers.standard_server;` |
| Database | `shape=cylinder3;boundedLbl=1;backgroundOutline=1;size=15;` |
| Zone container | `rounded=1;dashed=1;dashPattern=5 5;container=1;collapsible=0;verticalAlign=top;` |
| Network link | `endArrow=none;strokeWidth=2;` (undirected) |

## 5.9 Mind Map

Mind maps radiate from a central topic with branches for main ideas and sub-branches for details. Use ellipses for the center, rounded rectangles for branches, and organic curved edges.

```xml
<mxfile>
  <diagram id="mindmap-1" name="Mind Map">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="center" value="Project&#xa;Management" style="ellipse;whiteSpace=wrap;html=1;fillColor=#6C8EBF;strokeColor=#6C8EBF;fontColor=#FFFFFF;fontSize=16;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="340" y="300" width="160" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="b1" value="Planning" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;fontStyle=1;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="80" y="100" width="140" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="b1-1" value="Scope Definition" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=11;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="-100" y="80" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="b1-2" value="Resource Allocation" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=11;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="-100" y="140" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="b2" value="Execution" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;fontStyle=1;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="620" y="100" width="140" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="b2-1" value="Task Assignment" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=11;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="780" y="80" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="b2-2" value="Development" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=11;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="780" y="140" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="b3" value="Monitoring" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontColor=#333333;fontSize=14;fontStyle=1;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="80" y="520" width="140" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="b3-1" value="KPI Tracking" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontColor=#333333;fontSize=11;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="-100" y="500" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="b3-2" value="Risk Assessment" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontColor=#333333;fontSize=11;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="-100" y="560" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="b4" value="Closing" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;fontSize=14;fontStyle=1;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="620" y="520" width="140" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="b4-1" value="Documentation" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;fontSize=11;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="780" y="500" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="b4-2" value="Lessons Learned" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;fontSize=11;arcSize=40;" vertex="1" parent="1">
          <mxGeometry x="780" y="560" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="e-b1" style="endArrow=none;html=1;strokeColor=#6C8EBF;strokeWidth=3;curved=1;" edge="1" source="center" target="b1" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e-b2" style="endArrow=none;html=1;strokeColor=#82B366;strokeWidth=3;curved=1;" edge="1" source="center" target="b2" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e-b3" style="endArrow=none;html=1;strokeColor=#D6B656;strokeWidth=3;curved=1;" edge="1" source="center" target="b3" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e-b4" style="endArrow=none;html=1;strokeColor=#9673A6;strokeWidth=3;curved=1;" edge="1" source="center" target="b4" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e-b1-1" style="endArrow=none;html=1;strokeColor=#6C8EBF;strokeWidth=2;curved=1;" edge="1" source="b1" target="b1-1" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e-b1-2" style="endArrow=none;html=1;strokeColor=#6C8EBF;strokeWidth=2;curved=1;" edge="1" source="b1" target="b1-2" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e-b2-1" style="endArrow=none;html=1;strokeColor=#82B366;strokeWidth=2;curved=1;" edge="1" source="b2" target="b2-1" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e-b2-2" style="endArrow=none;html=1;strokeColor=#82B366;strokeWidth=2;curved=1;" edge="1" source="b2" target="b2-2" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e-b3-1" style="endArrow=none;html=1;strokeColor=#D6B656;strokeWidth=2;curved=1;" edge="1" source="b3" target="b3-1" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e-b3-2" style="endArrow=none;html=1;strokeColor=#D6B656;strokeWidth=2;curved=1;" edge="1" source="b3" target="b3-2" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e-b4-1" style="endArrow=none;html=1;strokeColor=#9673A6;strokeWidth=2;curved=1;" edge="1" source="b4" target="b4-1" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e-b4-2" style="endArrow=none;html=1;strokeColor=#9673A6;strokeWidth=2;curved=1;" edge="1" source="b4" target="b4-2" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

| Key Point | Detail |
|-----------|--------|
| Central topic | `ellipse;fontStyle=1;fontSize=16;` (bold, larger) |
| Main branch | `rounded=1;arcSize=40;fontStyle=1;fontSize=14;` |
| Sub-branch | `rounded=1;arcSize=40;fontSize=11;` (smaller) |
| Branch edge | `endArrow=none;strokeWidth=3;curved=1;` (thick, organic) |
| Sub-branch edge | `endArrow=none;strokeWidth=2;curved=1;` (thinner) |
| Color coding | Each branch family shares the same color scheme |

## 5.10 Organization Chart

Org charts show hierarchical reporting structures. Use rounded rectangles for positions with name and title, and straight vertical/horizontal edges for reporting lines.

```xml
<mxfile>
  <diagram id="orgchart-1" name="Organization Chart">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="org-1" value="&lt;b&gt;Jane Smith&lt;/b&gt;&lt;br&gt;CEO" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#6C8EBF;strokeColor=#6C8EBF;fontColor=#FFFFFF;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="320" y="40" width="160" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="org-2" value="&lt;b&gt;Alice Johnson&lt;/b&gt;&lt;br&gt;VP Engineering" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=13;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="80" y="180" width="180" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="org-3" value="&lt;b&gt;Bob Williams&lt;/b&gt;&lt;br&gt;VP Marketing" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=13;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="320" y="180" width="180" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="org-4" value="&lt;b&gt;Carol Davis&lt;/b&gt;&lt;br&gt;VP Operations" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontColor=#333333;fontSize=13;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="560" y="180" width="180" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="org-5" value="&lt;b&gt;Dave Lee&lt;/b&gt;&lt;br&gt;Sr. Engineer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=12;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="20" y="320" width="150" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="org-6" value="&lt;b&gt;Eve Chen&lt;/b&gt;&lt;br&gt;Engineer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=12;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="190" y="320" width="150" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="org-7" value="&lt;b&gt;Frank Kim&lt;/b&gt;&lt;br&gt;Marketing Lead" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="260" y="320" width="150" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="org-8" value="&lt;b&gt;Grace Park&lt;/b&gt;&lt;br&gt;Content Writer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=12;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="430" y="320" width="150" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="org-9" value="&lt;b&gt;Henry Zhao&lt;/b&gt;&lt;br&gt;Ops Manager" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontColor=#333333;fontSize=12;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="500" y="320" width="150" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="org-10" value="&lt;b&gt;Ivy Nguyen&lt;/b&gt;&lt;br&gt;Logistics" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontColor=#333333;fontSize=12;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="670" y="320" width="150" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="line-1" style="endArrow=none;html=1;strokeColor=#6C8EBF;strokeWidth=2;" edge="1" source="org-1" target="org-2" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="line-2" style="endArrow=none;html=1;strokeColor=#82B366;strokeWidth=2;" edge="1" source="org-1" target="org-3" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="line-3" style="endArrow=none;html=1;strokeColor=#D6B656;strokeWidth=2;" edge="1" source="org-1" target="org-4" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="line-4" style="endArrow=none;html=1;strokeColor=#6C8EBF;strokeWidth=1;" edge="1" source="org-2" target="org-5" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="line-5" style="endArrow=none;html=1;strokeColor=#6C8EBF;strokeWidth=1;" edge="1" source="org-2" target="org-6" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="line-6" style="endArrow=none;html=1;strokeColor=#82B366;strokeWidth=1;" edge="1" source="org-3" target="org-7" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="line-7" style="endArrow=none;html=1;strokeColor=#82B366;strokeWidth=1;" edge="1" source="org-3" target="org-8" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="line-8" style="endArrow=none;html=1;strokeColor=#D6B656;strokeWidth=1;" edge="1" source="org-4" target="org-9" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="line-9" style="endArrow=none;html=1;strokeColor=#D6B656;strokeWidth=1;" edge="1" source="org-4" target="org-10" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

| Key Point | Detail |
|-----------|--------|
| Person box | `rounded=1;arcSize=20;` with `<b>Name</b><br>Title` HTML |
| Level 1 (exec) | Darker fill, white text, `fontSize=14` |
| Level 2 (mgmt) | Light fill, `fontSize=13` |
| Level 3 (team) | Light fill, `fontSize=12`, smaller box |
| Reporting line | `endArrow=none;strokeWidth=2;` (no arrows) |
| Color coding | Each department shares the same color family |
| HTML labels | Use `&lt;b&gt;` for name, `&lt;br&gt;` for line break |
