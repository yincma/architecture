## 6. Cloud Architecture Icon Reference

Cloud architecture diagrams use draw.io's stencil library to reference cloud service icons. Icons are specified through the `shape=mxgraph.<provider>.<service>` style attribute, with each cloud provider having its own namespace.

### General Rules

- Recommended cloud icon size: **60×60** (standard) or **78×78** (large icon), keep `aspect=fixed` to prevent icon distortion
- All cloud icon nodes must include `whiteSpace=wrap;html=1;`
- Icon labels are typically placed below the icon, using `verticalLabelPosition=bottom;verticalAlign=top;align=center;`
- Each service category has a corresponding official brand color (`fillColor`), services in the same category use the same fill color
- `strokeColor` uniformly uses `#ffffff` (white border)

### Cloud Icon mxCell Template

```xml
<mxCell id="{id}" value="{service-name}" 
        style="shape=mxgraph.{provider}.{service};whiteSpace=wrap;html=1;fillColor={category-color};strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;aspect=fixed;" 
        vertex="1" parent="{parent-id}">
  <mxGeometry x="{x}" y="{y}" width="60" height="60" as="geometry"/>
</mxCell>
```
