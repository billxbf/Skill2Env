# HappyHorse Prompt Studio

> [中文版 / Chinese →](README.zh.md)

Interactive prompt studio for **HappyHorse 1.0** video generation — a guided conversation that turns "I want to make a video" into a production-ready prompt.

Covers 4 scenario flavors + free-form mode:

| Flavor | Description | Duration |
|--------|-------------|----------|
| **A · Voiced Manga Drama** | Multi-character dialogue with voice & lip-sync | 15–30s |
| **B · Character Voice PV** | Single character self-introduction with voice | 8–10s |
| **C · Manga Panel Motion** | Animate a static manga panel (hair, eyes, wind) | 5–10s |
| **D · Virtual Idol MV** | Stage performance with singing & choreography | 30s |

Supports JP / CN / EN prompts with native phrasing and proper lip-sync brackets.

## How it works

```
Phase 1 · Inspiration Menu    →  "Here's what HappyHorse can do"
Phase 2 · Discovery           →  "What do YOU want to make?"
Phase 3 · Prompt Assembly     →  "Let me build it for you"
Phase 4 · Quality Check       →  "Here's your prompt — want to tweak?"
```

The skill follows the **HappyHorse Formula**:

```
Scene + Subject + Motion + Audio + Quality
```

And outputs a prompt ready to paste into `bl video generate` or the HappyHorse web UI, with:
- Character consistency constraints (`キャラの顔・髪・衣装が変わらない`)
- R2V reference syntax (`@「Image n」`) for multi-image inputs
- Native-language voice type descriptors
- Cost estimates (720P: ¥0.9/sec, 1080P: ¥1.6/sec)

## Quick start

Install the skill, then tell your agent:

```
I want to make a HappyHorse video of my manga character introducing herself.
She's a cheerful schoolgirl with pink hair, on a rooftop at lunch.
```

The skill will guide you through discovery and assemble a prompt like:

```
昼休みの学校の屋上、青空と白い雲、風が心地よい。
桜色のロングヘアの少女がフェンスに寄りかかり、こちらを見て笑っている。

少女が手を振り、カメラがゆっくり寄る。
[少女、ネイティブな日本語、明るく元気な若い女性声、嬉しそう] 言う：
「ねえ！来てくれたんだ！」

背景に風の音、遠くで校庭のざわめき、明るいピアノの BGM。
映画級質感、キャラの顔・髪・制服が変わらない。
```

## Prerequisites

This skill requires Alibaba Cloud Model Studio CLI (`bl`). Before using this skill, check if `bl` is installed:

```bash
bl --version
```

If not installed or the command is not found, follow the install guide:

> https://bailian.aliyun.com/cli/install.md

A DashScope API key is also required for video generation.

## Run the prompt directly

```bash
# Image-to-video (one character reference)
bl video generate --image ./char.png --prompt "[PROMPT]" --download output.mp4

# Reference-to-video (multiple references for consistency)
bl video generate --image ./char1.png --image ./char2.png --prompt "[PROMPT]" --download output.mp4
```

## License

Apache-2.0
