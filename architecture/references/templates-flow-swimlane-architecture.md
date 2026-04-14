# Flow, Swimlane, and Architecture Templates

## 5.1 Flowchart

Flowcharts use ellipses for start/end nodes, rounded rectangles for processing steps, and diamonds for decision nodes.

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

Key points:

| Element | Shape Style | Color Scheme |
|------|----------|------|
| Start/End | `ellipse;whiteSpace=wrap;html=1;` | `fillColor=#6C8EBF;fontColor=#FFFFFF;` |
| Processing | `rounded=1;whiteSpace=wrap;html=1;` | `fillColor=#DAE8FC;strokeColor=#6C8EBF;` |
| Decision | `rhombus;whiteSpace=wrap;html=1;` | `fillColor=#FFE6CC;strokeColor=#D6B656;` |
| Error | `rounded=1;whiteSpace=wrap;html=1;` | `fillColor=#F8CECC;strokeColor=#B85450;` |

## 5.2 Swimlane Diagram

Swimlane diagrams use `swimlane` style containers with `startSize` for the title bar height. Child elements use relative coordinates.

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

Key points:
- Swimlane container: `swimlane;startSize=30;container=1;`
- Child `parent` set to owning swimlane ID
- Relative coordinates within swimlane
- Cross-swimlane edges: `parent="1"`

## 5.8 Architecture Diagram

Architecture diagrams use rounded rectangles for services, cylinders for databases, cloud shapes for external systems, with layer containers.

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
        <mxCell id="arch-edge-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="arch-cdn" target="arch-nginx">
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
        <mxCell id="arch-edge-7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="arch-biz" target="arch-cache">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="arch-edge-8" value="Async" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;dashed=1;" edge="1" parent="1" source="arch-biz" target="arch-mq">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Key points:
- Layer containers: `container=1;pointerEvents=0;fillColor=none;dashed=1;`
- Frontend (blue), Service (green), Data (orange) layers
- Database: `shape=cylinder3;boundedLbl=1;size=15;`
- Async connections: `dashed=1;`
- Data flow labels in edge `value` attribute