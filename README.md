# Architecture Diagram Skill

一个用于生成、修改、校验和导出 draw.io / diagrams.net 架构图的 AI Skill。

它的核心目标不是“随便拼 XML”，而是让 AI 先做布局规划，再生成可读、可维护、可导出的 `.drawio` 文件。

## 能做什么

- 根据自然语言生成完整的 `.drawio` 文件
- 修改已有 `.drawio` 文件，并尽量保留原有 ID、样式、布局和连线
- 支持常见图类型：架构图、流程图、泳道图、UML Class、UML Sequence、UML State、ER 图、网络拓扑、思维导图、组织架构图
- 支持 AWS、Azure、GCP 和通用架构图样式
- 先规划布局，再生成 XML，减少节点重叠、连线混乱和阅读方向不清的问题
- 可选使用 `tools/validate_drawio.py` 做轻量 XML / draw.io 结构校验
- 可在具备 draw.io Desktop CLI 的环境中导出 PNG、SVG、PDF

## 推荐仓库结构

```text
architecture-diagram-skill/
├── README.md
├── SKILL.md
├── references/
│   ├── xml-spec.md
│   ├── styles.md
│   ├── layout-quality.md
│   ├── containers-layout.md
│   ├── export.md
│   ├── architecture-benchmark.md
│   ├── templates/
│   │   ├── index.md
│   │   ├── architecture.md
│   │   ├── flowchart.md
│   │   ├── swimlane.md
│   │   ├── uml-class.md
│   │   ├── uml-sequence.md
│   │   ├── uml-state.md
│   │   ├── er.md
│   │   ├── network-topology.md
│   │   ├── mind-map.md
│   │   └── organization-chart.md
│   └── cloud-icons/
│       ├── index.md
│       ├── aws.md
│       ├── azure.md
│       └── gcp.md
└── tools/
    └── validate_drawio.py
```

## 哪些文件是必须的

### 运行必须

| 路径 | 作用 |
|---|---|
| `SKILL.md` | Skill 主入口和工作流控制文件 |
| `references/xml-spec.md` | draw.io XML 结构、mxCell、edge、escaping 等硬规则 |
| `references/styles.md` | 节点、边、颜色、文本换行等样式规范 |
| `references/layout-quality.md` | 读图方向、间距、交叉、图例、导出可读性等视觉质量规则 |
| `references/containers-layout.md` | 容器、嵌套、相对坐标、云边界、泳道、边线路由规则 |
| `references/templates/index.md` | 图类型到模板文件的索引 |
| `references/templates/*.md` | 各类图的 XML 示例模板 |
| `references/cloud-icons/index.md` | 云厂商图标索引和加载规则 |
| `references/cloud-icons/aws.md` | AWS 图标规则和常用服务样式 |
| `references/cloud-icons/azure.md` | Azure 图标规则和常用服务样式 |
| `references/cloud-icons/gcp.md` | GCP 图标规则和常用服务样式 |
| `references/export.md` | PNG / SVG / PDF 导出规则 |
| `references/architecture-benchmark.md` | 多方案架构对比和 benchmark 报告规则 |

### 推荐保留，但不是运行硬依赖

| 路径 | 作用 |
|---|---|
| `tools/validate_drawio.py` | 本地轻量校验 `.drawio` 文件，方便 CI 或人工检查 |
| `README.md` | GitHub 仓库首页说明 |

### 不建议上传

这些文件对仓库运行没有必要，已经从精简版中移除：

| 文件 | 原因 |
|---|---|
| `skill.md` | 与 `SKILL.md` 内容重复；正式仓库保留 `SKILL.md` 即可 |
| `VALIDATION-REPORT.md` | 一次性交付检查记录，不属于 skill 运行文件 |
| `VALIDATION_REPORT.txt` | 一次性交付检查记录，不属于 skill 运行文件 |
| `CHANGELOG.md` | 可选维护文件；如果你不打算长期记录版本变更，可以不上传 |
| `references/templates.md` | 旧版兼容跳转文件；模板已经拆到 `references/templates/` |
| `references/cloud-icons.md` | 旧版兼容跳转文件；图标已经拆到 `references/cloud-icons/` |

## 使用方式

把整个目录放到你的 AI agent / IDE 支持的 skills 目录中，例如：

```text
.claude/skills/architecture-diagram/
```

确保主入口文件名为：

```text
SKILL.md
```

然后向 agent 提出类似请求：

```text
帮我画一个用户登录系统的架构图，包含 Web、API Gateway、Auth Service、Redis、PostgreSQL 和外部 OAuth Provider，输出 draw.io 文件。
```

或：

```text
帮我把这个架构图导出成 PNG 和 SVG。
```

## 校验 draw.io 文件

生成 `.drawio` 后，可以运行：

```bash
python tools/validate_drawio.py path/to/diagram.drawio
```

也可以一次校验多个文件：

```bash
python tools/validate_drawio.py diagrams/*.drawio
```

这个校验器主要检查：

- XML 是否能解析
- 是否包含 draw.io 必需的根节点
- `mxCell` ID 是否重复
- edge 是否包含 `mxGeometry relative="1" as="geometry"`
- mxCell 是否同时被错误标记为 vertex 和 edge
- 容器、文本换行、坐标网格等常见问题

## 设计原则

这个 Skill 的生成流程遵循：

```text
理解需求 → 选择图类型 → 规划布局 → 规划节点和边 → 生成 XML → 质量检查 → 校验 / 导出
```

重点规则：

- 不直接从自然语言硬写 XML，必须先做 layout plan
- 优先保证读图方向清楚、节点不重叠、连线少交叉
- 云图标不能猜，找不到精确图标时使用通用形状兜底
- 容器内子元素必须使用相对坐标
- `.drawio` 优先输出未压缩、可读的 XML

## 维护建议

- 如果只维护一个仓库，建议保留当前精简结构即可。
- 如果后续要扩展更多云图标，优先更新 `references/cloud-icons/` 下的 provider 文件。
- 如果要新增图类型，先在 `references/templates/` 新增模板，再更新 `references/templates/index.md`。
- 如果你要让 CI 自动检查示例图，可以把 `tools/validate_drawio.py` 接入 GitHub Actions。
