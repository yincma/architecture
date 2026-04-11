# architecture
图表生成 Skill

让 AI 通过自然语言生成 `.drawio` 架构图。支持流程图、UML、ER 图、云架构图等 10 种图表类型。

## 安装

### Kiro IDE

将 `.kiro/skills/drawio-diagram/` 目录复制到你的项目中即可。Kiro 会自动识别该 Skill。

```
your-project/
└── .kiro/
    └── skills/
        └── architecture/
            └── skill.md
```

### Kiro CLI

同上，将 `.kiro/skills/drawio-diagram/` 放入项目根目录。CLI 模式下通过 `discloseContext("drawio-diagram")` 激活。

## 使用示例

在 Kiro 聊天中直接输入：

```
画一个用户登录的流程图
```

```
生成一个包含 EC2、RDS、S3 的 AWS 架构图
```

```
画一个订单系统的 ER 图，包含用户、订单、商品三个实体
```

```
帮我修改 system-architecture.drawio，把 Redis 缓存加到数据库前面
```

AI 会自动生成符合规范的 `.drawio` 文件，可直接用 draw.io 打开。
