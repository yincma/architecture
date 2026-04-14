# Draw.io 図表生成 Skill

AI が自然言語を使って `.drawio` 図表を生成・修正できるようにします。フローチャート、アーキテクチャ図、UML、ER 図、ネットワークトポロジ図、マインドマップ、組織図、スイムレーン図、およびアーキテクチャ比較ベンチマークの出力に対応しています。

## インストール

### Kiro IDE

`architecture/` ディレクトリをあなたのプロジェクトにコピーしてください。Kiro がこの Skill を自動的に認識します。

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

同様に、`architecture/` をプロジェクトルートの `.kiro/skills/` 配下に配置してください。CLI モードでは `discloseContext("drawio-diagram")` で有効化するか、Kiro のワークフローに従って `architecture/skill.md` を手動で読み込めます。

## 使用例

Kiro のチャットにそのまま入力してください。

```
ユーザーログインのフローチャートを描いて
```

```
ALB、EC2、RDS、S3 を含む AWS アーキテクチャ図を生成して
```

```
ユーザー、注文、商品の 3 つのエンティティを含む注文システムの ER 図を描いて
```

```
system-architecture.drawio を修正して、Redis キャッシュをデータベースの前段に追加して
```

```
モノリス、マイクロサービス、Serverless の 3 種類の注文システムアーキテクチャを比較し、benchmark を出力して
```

AI は必要に応じて `references/` 配下のテンプレートやルールを読み込み、`scripts/validate_drawio_xml.py` を使って生成結果を検証し、`scripts/lookup_cloud_icon.py` を使ってクラウドアイコンのスタイルを参照できます。

## ディレクトリ構成

- `skill.md`: メインエントリ。workflow、ハード制約、reference ルーティングを保持
- `references/`: XML 仕様、スタイル、テンプレート、クラウドアイコン、レイアウトルール
- `scripts/`: XML 検証スクリプトとクラウドアイコン検索スクリプト
- `skill.original.md`: リファクタリング前の完全なベースラインバックアップ
