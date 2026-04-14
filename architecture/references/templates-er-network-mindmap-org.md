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

