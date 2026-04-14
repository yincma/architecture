# UML Templates

## 5.3 UML Class Diagram

UML class diagrams use `swimlane` style containers to represent classes, with internal divider lines separating the class name, attributes, and methods into three areas. Attribute and method rows use the `text` style with `portConstraint=eastwest`. Relationships between classes are represented by edges with specific arrow styles.

```xml
<mxfile>
  <diagram id="class-diagram-1" name="UML Class Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="class-1" value="Animal" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="280" y="40" width="160" height="140" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-attr-1" value="# name: String" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-1">
          <mxGeometry y="26" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-attr-2" value="# age: int" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-1">
          <mxGeometry y="52" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-sep" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;" vertex="1" parent="class-1">
          <mxGeometry y="78" width="160" height="8" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-method-1" value="+ getName(): String" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-1">
          <mxGeometry y="86" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-method-2" value="+ speak(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-1">
          <mxGeometry y="112" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-2" value="Dog" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="100" y="300" width="160" height="140" as="geometry"/>
        </mxCell>
        <mxCell id="class-2-attr-1" value="- breed: String" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-2">
          <mxGeometry y="26" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-2-sep" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;" vertex="1" parent="class-2">
          <mxGeometry y="52" width="160" height="8" as="geometry"/>
        </mxCell>
        <mxCell id="class-2-method-1" value="+ speak(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-2">
          <mxGeometry y="60" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-2-method-2" value="+ fetch(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-2">
          <mxGeometry y="86" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-3" value="Cat" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;container=1;collapsible=0;whiteSpace=wrap;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="460" y="300" width="160" height="140" as="geometry"/>
        </mxCell>
        <mxCell id="class-3-attr-1" value="- indoor: boolean" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-3">
          <mxGeometry y="26" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-3-sep" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;strokeColor=inherit;html=1;" vertex="1" parent="class-3">
          <mxGeometry y="52" width="160" height="8" as="geometry"/>
        </mxCell>
        <mxCell id="class-3-method-1" value="+ speak(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-3">
          <mxGeometry y="60" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="class-3-method-2" value="+ purr(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="class-3">
          <mxGeometry y="86" width="160" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="edge-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;" edge="1" parent="1" source="class-2" target="class-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=0;" edge="1" parent="1" source="class-3" target="class-1">
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
| Class container | `swimlane;fontStyle=1;startSize=26;container=1;collapsible=0;` — `startSize=26` defines the class name area height |
| Attribute rows | `text;portConstraint=eastwest;` style, `y` coordinate starts from `startSize` (26) and increments by 26 |
| Divider line | `line;strokeColor=inherit;portConstraint=eastwest;` — separates the attribute area from the method area |
| Method rows | Same style as attribute rows, `y` coordinate follows immediately after the divider line |
| Child element `parent` | Attribute rows, divider lines, and method rows have `parent` set to the owning class's `id` |
| Relative coordinates | Child element `y` coordinates are relative to the class container top, `x=0`, `width` matches the class container |
| Inheritance | `endArrow=block;endFill=0;` (open triangle arrow), pointing from subclass to superclass |
| Visibility markers | `+` public, `-` private, `#` protected |


## 5.4 UML Sequence Diagram

UML sequence diagrams use the `shape=umlLifeline` style to represent participant lifelines. A lifeline is a container that can hold activation boxes inside. Messages connect activation boxes on different lifelines via edges.

```xml
<mxfile>
  <diagram id="sequence-diagram-1" name="UML Sequence Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="lifeline-1" value="Client" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="40" width="100" height="500" as="geometry"/>
        </mxCell>
        <mxCell id="activation-1" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;outlineConnect=0;targetShapes=umlLifeline;portConstraint=eastwest;newEdgeStyle={&quot;curved&quot;:0,&quot;rounded&quot;:0};fillColor=#DAE8FC;strokeColor=#6C8EBF;" vertex="1" parent="lifeline-1">
          <mxGeometry x="45" y="80" width="10" height="360" as="geometry"/>
        </mxCell>
        <mxCell id="lifeline-2" value="Auth Service" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="330" y="40" width="100" height="500" as="geometry"/>
        </mxCell>
        <mxCell id="activation-2" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;outlineConnect=0;targetShapes=umlLifeline;portConstraint=eastwest;newEdgeStyle={&quot;curved&quot;:0,&quot;rounded&quot;:0};fillColor=#D5E8D4;strokeColor=#82B366;" vertex="1" parent="lifeline-2">
          <mxGeometry x="45" y="100" width="10" height="200" as="geometry"/>
        </mxCell>
        <mxCell id="lifeline-3" value="Database" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#E1D5E7;strokeColor=#9673A6;fontColor=#333333;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="580" y="40" width="100" height="500" as="geometry"/>
        </mxCell>
        <mxCell id="activation-3" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;outlineConnect=0;targetShapes=umlLifeline;portConstraint=eastwest;newEdgeStyle={&quot;curved&quot;:0,&quot;rounded&quot;:0};fillColor=#E1D5E7;strokeColor=#9673A6;" vertex="1" parent="lifeline-3">
          <mxGeometry x="45" y="160" width="10" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="msg-1" value="1: login(user, pwd)" style="html=1;verticalAlign=bottom;endArrow=block;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;" edge="1" parent="1" source="activation-1" target="activation-2">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="200" y="140" as="sourcePoint"/>
            <mxPoint x="370" y="140" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="msg-2" value="2: queryUser(user)" style="html=1;verticalAlign=bottom;endArrow=block;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;" edge="1" parent="1" source="activation-2" target="activation-3">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="390" y="200" as="sourcePoint"/>
            <mxPoint x="620" y="200" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="msg-3" value="3: userData" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;" edge="1" parent="1" source="activation-3" target="activation-2">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="620" y="260" as="sourcePoint"/>
            <mxPoint x="390" y="260" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="msg-4" value="4: authToken" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;" edge="1" parent="1" source="activation-2" target="activation-1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="370" y="340" as="sourcePoint"/>
            <mxPoint x="140" y="340" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="msg-5" value="5: showDashboard()" style="html=1;verticalAlign=bottom;endArrow=block;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;" edge="1" parent="1" source="activation-1" target="activation-1">
          <mxGeometry x="-0.5" relative="1" as="geometry">
            <mxPoint x="140" y="400" as="sourcePoint"/>
            <mxPoint x="140" y="400" as="targetPoint"/>
            <Array as="points">
              <mxPoint x="200" y="400"/>
            </Array>
            <mxPoint as="offset"/>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Key points:

| Key Point | Description |
|------|------|
| Lifeline | `shape=umlLifeline;container=1;collapsible=0;recursiveResize=0;` — height determines lifeline length |
| Activation box | `perimeter=orthogonalPerimeter;portConstraint=eastwest;` — placed inside the lifeline container |
| Activation box coordinates | `x` = `(lifeline width - activation box width) / 2` (centered), `y` = time position |
| Synchronous message | `endArrow=block;` (filled arrow), from source activation box to target activation box |
| Return message | `endArrow=open;dashed=1;` (dashed open arrow) |
| Self-call message | `source` and `target` point to the same activation box, uses `Array as="points"` to form a loop |
| Message numbering | Use `1:`, `2:`, etc. in the edge's `value` to annotate message order |
| Special character escaping | The `newEdgeStyle` JSON value in activation box styles requires `"` to be escaped as `&quot;` |


## 5.5 UML State Diagram

UML state diagrams use filled circles for initial states, rounded rectangles for regular state nodes, and double circles for final states. Transitions between states are represented by labeled edges.

```xml
<mxfile>
  <diagram id="state-diagram-1" name="UML State Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="state-init" value="" style="ellipse;html=1;shape=mxgraph.flowchart.start_2;fontSize=12;fillColor=#000000;fontColor=#FFFFFF;whiteSpace=wrap;" vertex="1" parent="1">
          <mxGeometry x="370" y="40" width="30" height="30" as="geometry"/>
        </mxCell>
        <mxCell id="state-1" value="Pending Payment" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="320" y="120" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="state-2" value="Paid" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="320" y="240" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="state-3" value="In Delivery" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D6B656;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="320" y="360" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="state-4" value="Completed" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="320" y="480" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="state-cancelled" value="Cancelled" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="570" y="240" width="130" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="state-end" value="" style="ellipse;html=1;shape=doubleCircle;whiteSpace=wrap;aspect=fixed;fillColor=#000000;fontColor=#FFFFFF;" vertex="1" parent="1">
          <mxGeometry x="375" y="590" width="30" height="30" as="geometry"/>
        </mxCell>
        <mxCell id="edge-1" value="Create Order" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-init" target="state-1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-2" value="Payment Successful" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-1" target="state-2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-3" value="Ship" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-2" target="state-3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-4" value="Confirm Receipt" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-3" target="state-4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-4" target="state-end">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-6" value="Cancel Order" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-1" target="state-cancelled">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-7" value="Timeout Cancellation" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="state-2" target="state-cancelled">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;entryX=1;entryY=0.5;" edge="1" parent="1" source="state-cancelled" target="state-end">
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
| Initial state | `ellipse;shape=mxgraph.flowchart.start_2;fillColor=#000000;` — recommended size 30×30 |
| Regular state | `rounded=1;arcSize=20;` rounded rectangle, different categories use different color schemes |
| Final state | `ellipse;shape=doubleCircle;fillColor=#000000;aspect=fixed;` — recommended size 30×30 |
| Transition labels | Set trigger event names in the edge's `value` attribute |
| Exception path | Red color scheme (`fillColor=#F8CECC;strokeColor=#B85450;`) for cancelled/exception states |
| Multiple entry transitions | Multiple states can transition to the same target (e.g., multiple states → Cancelled) |
