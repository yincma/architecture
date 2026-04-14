# Draw.io 图表生成 Skill

让 AI 通过自然语言生成和修改 `.drawio` 图表。支持流程图、架构图、UML、ER 图、网络拓扑图、思维导图、组织架构图、泳道图，以及架构对比基准输出。

## 安装

### Kiro IDE

将 `architecture/` 目录复制到你的项目中即可。Kiro 会自动识别该 Skill。

```
your-project/
└── .kiro/
    └── skills/
        └── architecture/
            ├── skill.md
            ├── references/
            └── scripts/
```

### Kiro CLI

同上，将 `architecture/` 放入项目根目录的 `.kiro/skills/` 下。CLI 模式下可通过 `discloseContext("drawio-diagram")` 激活，或按你的 Kiro 工作流手动加载 `architecture/skill.md`。

## 使用示例

在 Kiro 聊天中直接输入：

```
画一个用户登录的流程图
```

```
生成一个包含 ALB、EC2、RDS、S3 的 AWS 架构图
```

```
画一个订单系统的 ER 图，包含用户、订单、商品三个实体
```

```
帮我修改 system-architecture.drawio，把 Redis 缓存加到数据库前面
```

```
比较单体、微服务、Serverless 三种订单系统架构，并输出 benchmark
```

AI 会按需读取 `references/` 下的模板和规则，并可使用 `scripts/validate_drawio_xml.py` 校验生成结果、使用 `scripts/lookup_cloud_icon.py` 查询云图标样式。

## 目录说明

- `skill.md`：主入口，保留 workflow、硬约束和 reference 路由
- `references/`：XML 规范、样式、模板、云图标、布局规则
- `scripts/`：XML 校验和云图标查询脚本
- `skill.original.md`：重构前的完整基线备份
