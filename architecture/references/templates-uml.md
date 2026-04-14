# UML Templates

## 5.3 UML Class Diagram

Class diagrams show classes with attributes/methods and their relationships. Use swimlane-style cells for class boxes and `endArrow=block;endFill=0;` for inheritance.

```xml
<mxfile>
  <diagram id="uml-class-1" name="UML Class Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- Superclass: Animal -->
        <mxCell id="class-1" value="Animal" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="300" y="40" width="200" height="140" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-attrs" value="+ name: String&#xa;+ age: int" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;whiteSpace=wrap;html=1;fontSize=12;" vertex="1" parent="class-1">
          <mxGeometry y="26" width="200" height="54" as="geometry"/>
        </mxCell>
        <mxCell id="class-1-methods" value="+ speak(): String&#xa;+ move(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;whiteSpace=wrap;html=1;fontSize=12;" vertex="1" parent="class-1">
          <mxGeometry y="80" width="200" height="54" as="geometry"/>
        </mxCell>
        <!-- Subclass: Dog -->
        <mxCell id="class-2" value="Dog" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="120" y="280" width="200" height="140" as="geometry"/>
        </mxCell>
        <mxCell id="class-2-attrs" value="+ breed: String" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;whiteSpace=wrap;html=1;fontSize=12;" vertex="1" parent="class-2">
          <mxGeometry y="26" width="200" height="34" as="geometry"/>
        </mxCell>
        <mxCell id="class-2-methods" value="+ speak(): String&#xa;+ fetch(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;whiteSpace=wrap;html=1;fontSize=12;" vertex="1" parent="class-2">
          <mxGeometry y="60" width="200" height="54" as="geometry"/>
        </mxCell>
        <!-- Subclass: Cat -->
        <mxCell id="class-3" value="Cat" style="swimlane;fontStyle=1;align=center;startSize=26;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontColor=#333333;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="480" y="280" width="200" height="140" as="geometry"/>
        </mxCell>
        <mxCell id="class-3-attrs" value="+ indoor: boolean" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;whiteSpace=wrap;html=1;fontSize=12;" vertex="1" parent="class-3">
          <mxGeometry y="26" width="200" height="34" as="geometry"/>
        </mxCell>
        <mxCell id="class-3-methods" value="+ speak(): String&#xa;+ purr(): void" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;whiteSpace=wrap;html=1;fontSize=12;" vertex="1" parent="class-3">
          <mxGeometry y="60" width="200" height="54" as="geometry"/>
        </mxCell>
        <!-- Inheritance edges -->
        <mxCell id="edge-1" style="endArrow=block;endFill=0;html=1;strokeColor=#6C8EBF;fontSize=12;" edge="1" source="class-2" target="class-1" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="edge-2" style="endArrow=block;endFill=0;html=1;strokeColor=#6C8EBF;fontSize=12;" edge="1" source="class-3" target="class-1" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

| Key Point | Detail |
|-----------|--------|
| Class box | `swimlane;fontStyle=1;align=center;startSize=26;` |
| Attributes section | `text;` cell parented to the swimlane, `y` offset = `startSize` |
| Methods section | Another `text;` cell below attributes |
| Inheritance arrow | `endArrow=block;endFill=0;` (hollow triangle) |
| Association arrow | `endArrow=open;endFill=0;` with label for multiplicity |
| Parent-child | Attribute/method cells use `parent="class-N"` |


## 5.4 UML Sequence Diagram

Sequence diagrams show interactions between participants over time. Use thin rectangles for lifelines, narrow rectangles for activation boxes, and horizontal arrows for messages.

```xml
<mxfile>
  <diagram id="uml-seq-1" name="UML Sequence Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- Participant headers -->
        <mxCell id="p1" value="Client" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;fontStyle=1;size=40;" vertex="1" parent="1">
          <mxGeometry x="120" y="40" width="120" height="500" as="geometry"/>
        </mxCell>
        <mxCell id="p2" value="Auth Service" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;fontStyle=1;size=40;" vertex="1" parent="1">
          <mxGeometry x="360" y="40" width="120" height="500" as="geometry"/>
        </mxCell>
        <mxCell id="p3" value="Database" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#FFF2CC;strokeColor=#D6B656;fontColor=#333333;fontSize=14;fontStyle=1;size=40;" vertex="1" parent="1">
          <mxGeometry x="600" y="40" width="120" height="500" as="geometry"/>
        </mxCell>
        <!-- Activation boxes -->
        <mxCell id="act-1" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;fillColor=#DAE8FC;strokeColor=#6C8EBF;" vertex="1" parent="p1">
          <mxGeometry x="55" y="70" width="10" height="200" as="geometry"/>
        </mxCell>
        <mxCell id="act-2" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;fillColor=#D5E8D4;strokeColor=#82B366;" vertex="1" parent="p2">
          <mxGeometry x="55" y="90" width="10" height="140" as="geometry"/>
        </mxCell>
        <mxCell id="act-3" value="" style="html=1;points=[];perimeter=orthogonalPerimeter;fillColor=#FFF2CC;strokeColor=#D6B656;" vertex="1" parent="p3">
          <mxGeometry x="55" y="120" width="10" height="60" as="geometry"/>
        </mxCell>
        <!-- Messages -->
        <mxCell id="msg-1" value="login(user, pass)" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#6C8EBF;fontSize=12;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="180" y="140" as="sourcePoint"/>
            <mxPoint x="420" y="140" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="msg-2" value="queryUser(user)" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#82B366;fontSize=12;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="420" y="180" as="sourcePoint"/>
            <mxPoint x="660" y="180" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="msg-3" value="userData" style="html=1;verticalAlign=bottom;endArrow=open;endFill=0;dashed=1;strokeColor=#D6B656;fontSize=12;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="660" y="220" as="sourcePoint"/>
            <mxPoint x="420" y="220" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="msg-4" value="authToken" style="html=1;verticalAlign=bottom;endArrow=open;endFill=0;dashed=1;strokeColor=#6C8EBF;fontSize=12;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="420" y="270" as="sourcePoint"/>
            <mxPoint x="180" y="270" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <!-- Self-call -->
        <mxCell id="msg-5" value="showDashboard()" style="html=1;verticalAlign=bottom;endArrow=block;endFill=1;strokeColor=#6C8EBF;fontSize=12;curved=1;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="185" y="310" as="sourcePoint"/>
            <mxPoint x="185" y="350" as="targetPoint"/>
            <Array as="points">
              <mxPoint x="240" y="310"/>
              <mxPoint x="240" y="350"/>
            </Array>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

| Key Point | Detail |
|-----------|--------|
| Lifeline | `shape=umlLifeline;perimeter=lifelinePerimeter;container=1;size=40;` |
| Activation box | Narrow rect (`width=10`) parented to lifeline |
| Sync message | `endArrow=block;endFill=1;` (solid arrowhead) |
| Return message | `endArrow=open;endFill=0;dashed=1;` |
| Self-call | Source and target same lifeline, use `Array as="points"` to create loop |
| Positioning | Use absolute `mxPoint` for `sourcePoint` / `targetPoint` |

## 5.5 UML State Diagram

State diagrams model object lifecycle with states and transitions. Use filled circle for initial state, rounded rectangles for states, and bull's-eye for final state.

```xml
<mxfile>
  <diagram id="uml-state-1" name="UML State Diagram">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="850" pageHeight="1100"
                  math="0" shadow="0" adaptiveColors="auto">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- Initial state -->
        <mxCell id="state-init" value="" style="ellipse;html=1;shape=doubleCircle;whiteSpace=wrap;aspect=fixed;fillColor=#333333;strokeColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="380" y="30" width="40" height="40" as="geometry"/>
        </mxCell>
        <!-- States -->
        <mxCell id="state-1" value="Pending Payment" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="330" y="120" width="140" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="state-2" value="Paid" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="330" y="240" width="140" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="state-3" value="In Delivery" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="330" y="360" width="140" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="state-4" value="Completed" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="330" y="480" width="140" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="state-5" value="Cancelled" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontColor=#333333;fontSize=14;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="580" y="240" width="140" height="60" as="geometry"/>
        </mxCell>
        <!-- Final state -->
        <mxCell id="state-final" value="" style="ellipse;html=1;shape=doubleCircle;whiteSpace=wrap;aspect=fixed;fillColor=#333333;strokeColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="380" y="600" width="40" height="40" as="geometry"/>
        </mxCell>
        <!-- Transitions -->
        <mxCell id="t-0" value="" style="endArrow=block;endFill=1;html=1;strokeColor=#333333;" edge="1" source="state-init" target="state-1" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="t-1" value="pay" style="endArrow=block;endFill=1;html=1;strokeColor=#6C8EBF;fontSize=12;" edge="1" source="state-1" target="state-2" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="t-2" value="ship" style="endArrow=block;endFill=1;html=1;strokeColor=#82B366;fontSize=12;" edge="1" source="state-2" target="state-3" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="t-3" value="deliver" style="endArrow=block;endFill=1;html=1;strokeColor=#D6B656;fontSize=12;" edge="1" source="state-3" target="state-4" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="t-4" value="" style="endArrow=block;endFill=1;html=1;strokeColor=#333333;" edge="1" source="state-4" target="state-final" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="t-5" value="cancel" style="endArrow=block;endFill=1;html=1;strokeColor=#B85450;fontSize=12;" edge="1" source="state-1" target="state-5" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="t-6" value="cancel" style="endArrow=block;endFill=1;html=1;strokeColor=#B85450;fontSize=12;" edge="1" source="state-2" target="state-5" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="t-7" value="" style="endArrow=block;endFill=1;html=1;strokeColor=#333333;" edge="1" source="state-5" target="state-final" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

| Key Point | Detail |
|-----------|--------|
| Initial state | `ellipse;shape=doubleCircle;fillColor=#333333;` (small filled circle) |
| State | `rounded=1;arcSize=20;` (rounded rectangle) |
| Final state | `ellipse;shape=doubleCircle;fillColor=#333333;` (bull's-eye) |
| Transition | `endArrow=block;endFill=1;` with label for trigger |
| Guard condition | Add `[condition]` in edge label |
| Cancel paths | Multiple states can transition to Cancelled |
