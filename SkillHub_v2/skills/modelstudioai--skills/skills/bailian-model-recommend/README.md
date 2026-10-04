# bailian-model-recommend

> [中文版 / Chinese →](README.zh.md)

Model selection & recommendation skill for **Alibaba Cloud Model Studio (Bailian)** — analyzes your AI scenario and recommends the best-fit models from the Bailian model marketplace, complete with trade-off comparisons and ready-to-use code samples.

## What it does

Tell your agent what you want to build, and this skill will:

1. **Understand your requirements** — extract modality, capability, budget, and quality preferences from your description
2. **Filter candidates** — search the full Bailian model catalog by modality, capability, context window, and semantic relevance
3. **Recommend 3 models** — best fit, runner-up, and an alternative perspective, each with clear trade-off explanations
4. **Provide code samples** — OpenAI-compatible Python SDK and cURL examples for each recommendation

## When to use

**Explicit model selection:**
- "Recommend a model for X"
- "Which model should I use for Y?"
- "Compare model A vs model B"

**Implicit model selection (you describe a goal, the skill picks the model):**
- "I want to build a customer service chatbot"
- "Help me implement image generation"
- "What AI solution fits my summarization use case?"

**Technical selection:**
- "Which model is best for low-cost / high-throughput / high-accuracy scenarios?"
- "Model A vs Model B — which is better for task Y?"

**Not for this skill:**
- You already know which model to use and just need the API call → use `bailian-cli` directly
- Pure parameter / pricing lookup → use `bailian-docs-llm-wiki`

## Example

```
I want to build a multilingual customer service bot that handles
Chinese + English, needs to support function calling, and I want
to keep costs low.
```

The skill will recommend 3 models with reasoning like:

| # | Strategy | Example rationale |
|---|----------|-------------------|
| **1 — Best fit** | Cost-effective with function calling | "Supports both languages, native tool use, lowest per-token cost in its tier" |
| **2 — Runner-up** | Higher capability, moderate cost | "Stronger reasoning for complex queries, 2× cost but handles edge cases better" |
| **3 — Alternative** | Different trade-off angle | "Open-source option with self-hosting flexibility, no per-call charge at scale" |

Each recommendation includes model name, ID, key specs (context window, pricing), and copy-paste code samples.

## Prerequisites

- [`bailian-docs-llm-wiki`](../bailian-docs-llm-wiki/) skill installed (provides the model data catalog)
  - Auto-installed if missing: `npx skills add modelstudioai/skills --skill bailian-docs-llm-wiki -y`

## How it works under the hood

```
User request
  → Parse requirement (modality, capabilities, budget, quality tier)
  → Filter models.jsonl + group JSONs (modality match, capability match, semantic match)
  → Score & rank candidates (remove snapshots, deduplicate families, cap per-family)
  → Select top 3 with diverse trade-offs
  → Fetch code samples from group files
  → Output natural-language recommendation with specs + code
```

All recommendations are grounded in the actual model catalog data — the skill never recommends from memory.

## License

Apache-2.0
