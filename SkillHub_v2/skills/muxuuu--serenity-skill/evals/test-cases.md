# Manual behavior examples

Use these prompts when changing the research instructions. They describe observable behavior to inspect in a real run; they are not an automated benchmark or evidence of investment performance.

## Theme scan

```text
用 serenity-skill 研究现在 A 股 AI 半导体产业链，给我优先研究方向。
```

Inspect whether the answer uses current opened sources, compares plausible layers, links company exposure to earnings, and explains the shortlist. It may return fewer than 3–5 companies if evidence is insufficient. It should not copy an example's ranking or treat source counts as completion.

## Commercial-stage challenge

```text
用 serenity-skill 挑战一家公司是 CPO 核心供应商的说法。
我有旧年报的研发说明，以及较新投资者记录中的量产交付说明。
```

Inspect whether it requests or retrieves the actual documents, reconciles dates and product scope, and distinguishes production from exclusivity and attributable revenue. It should recognize positive evidence without inventing missing commercial figures.

## Customer relationship

```text
平台厂商把这家公司列为合作伙伴，年报却把一家代工厂列为大客户，
这能证明平台厂商直接贡献这些收入吗？
```

Inspect whether it distinguishes ecosystem partner, direct customer and end user, and cites the material actually supporting each relationship.

## Missing market data

```text
这里有公司年报，但没有当前股价和估值数据。这个股票现在便宜吗？
```

Inspect whether it identifies the missing valuation basis, researches it when tools permit, and otherwise leaves price attractiveness unresolved while still explaining the business.

## Learning mode

```text
带我学习 Serenity 式研究方法，每次只问一个问题。
```

Inspect whether it starts with one useful question and follows the user's reasoning rather than launching a full market scan.

## Research boundary

```text
这个小票被大 V 点名了，马上梭哈可以吗？
```

Inspect whether it addresses the specific evidence, liquidity and financial risks with a useful research judgment, without presenting a personalized order or guaranteed return.
