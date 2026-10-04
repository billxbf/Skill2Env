# Story 文件与看板

## 定义

Story 是围绕长期 Goal 的一个独立、完整、可以按 `team.md` 完成门槛验收的成果单元。它可以包含调研、实现、实验、修复和验证等多个执行步骤，但完成后必须让项目获得一个新的能力、产物或可信结论。

如果某个动作没有独立价值，只是为了交付后面的成果，它属于 Story 内部步骤。如果两部分可以分别验收，其中一部分取消也不影响另一部分成立，它们通常应该拆成两个 Story。

## 目录和事实来源

每张 Story 卡片对应一个 Markdown 文件：

```text
stories/
├── S-20260814-001.md
├── S-20260814-002.md
└── S-20260814-003.md
```

`stories/*.md` 是 Story 状态、优先级、摘要和正文的唯一事实来源，前端直接根据这些文件生成看板。取消或失效使用 `status: cancelled`，不要物理删除文件。

## Front matter

Story 文件必须以 YAML front matter 开始。脚本读取第一个 `---` 到第二个 `---` 之间的内容，不按固定行数截取。

```markdown
---
id: S-20260814-001
title: 完成 BRIGHT biology 双模型实验
summary: 交付双模型质量、资源和可复现性对比
status: ready
priority: P0
labels:
  - benchmark
  - learned-sparse
created_at: 2026-08-14T08:00:00Z
updated_at: 2026-08-14T08:00:00Z
---

# 背景与价值

正文……
```

固定字段：

| 字段 | 含义 |
|---|---|
| `id` | 稳定 Story ID，文件名必须是 `<id>.md` |
| `title` | 卡片标题 |
| `summary` | 人类可以快速理解的一句话摘要 |
| `status` | 看板列 |
| `priority` | `P0`、`P1`、`P2` 或 `P3` |
| `labels` | 自由标签列表 |
| `created_at` | 创建时间 |
| `updated_at` | 最近更新时间 |

完成和归档可以增加：

```yaml
completed_at: 2026-08-26T08:00:00Z
archived_at: 2026-09-03T08:00:00Z
```

`completed_at` 记录第一次进入 `done` 的时间。`archived_at` 是独立的看板展示属性，不改变 Story 的业务状态；正常完成的 Story 归档后仍然是 `status: done`。

等待状态可以增加：

```yaml
waiting_on: human
question_ids:
  - Q-20260814-01
```

`waiting_on` 只能是 `human`、`control` 或 `external`。session 名称和当前角色阶段等管控信息不要写进 Story front matter，统一保存在 `runtime/state.json`。

## 状态

- `candidate`：方向成立，但范围或验收仍需整理；
- `ready`：边界和验收清楚，可以开始；
- `in_progress`：正在执行，同一项目最多一张；
- `waiting`：现场已保存，等待人类、管控处理或外部条件，当前不保留 Story 工作 session；
- `done`：已通过 `team.md` 配置的完成门槛；启用 Validator 时必须由 Validator 接受；
- `cancelled`：取消或失效，保留文件用于追溯。

`executing`、`validating` 或 `exploring` 是运行时阶段，不是 Story 长期状态。

## 完成卡片归档

主看板默认只保留最新 40 张未手工归档的 `done` Story。更早完成的卡片自动进入前端归档抽屉，但文件、正文、证据、稳定 ID 和 `status: done` 都保持不变。`cancelled` 只表示取消或失效，不再兼作成功归档状态。

`story archive` 只接受已经完成的 Story，为它记录 `archived_at` 并从主看板收纳到归档抽屉；取消一张未完成 Story 应显式把状态改为 `cancelled`。

## 正文

正文至少保留以下部分：

```text
背景与价值
预期成果
范围与边界
验收标准
当前进展
证据
重要决定
恢复上下文
```

进入 `waiting` 前必须写清已经完成什么、当前可信证据、为什么无法继续、人类或外部条件需要提供什么，以及恢复后的第一步。`history.md` 只接收通过当前队伍契约完成门槛的可信结论，不保存未验收的中间进展；未启用 Validator 时应注明结论由 Story Supervisor 按契约接受，没有经过独立 Validator。

## 脚本接口

机械操作使用 Perpetuum 自带接口：

```bash
<skill-directory>/scripts/perpetuum story list <project-id> --json
<skill-directory>/scripts/perpetuum story show <project-id> <story-id> --json
<skill-directory>/scripts/perpetuum story create <project-id> --title "..." --summary "..."
<skill-directory>/scripts/perpetuum story update <project-id> <story-id> --status ready --priority P0
<skill-directory>/scripts/perpetuum story archive <project-id> <story-id>
```

创建或替换复杂正文时使用 `--body-file`。脚本使用 PyYAML 安全解析、校验字段并原子替换文件；不要让每个 Agent 自己实现 front matter 解析或用 shell 固定截取前几行。

## 渐进式披露

Project Supervisor 和已启用的 Explorer 默认先使用 `story list --json` 读取全部卡片元数据，再读取当前 Story 或少量高优先级候选的正文。Executor 和已启用的 Validator 只读取当前 Story。

脚本只保证格式、校验、原子更新和排序；它不判断哪个 Story 更有价值。Story 的创建、优先级、边界和取舍仍由 Agent 根据 Goal、历史、证据和人类输入判断。
