# 架构

## 整体结构

```text
Local Runner / Frontend Service
        ├── Project Supervisor A
        │       └── Story Supervisor
        │               ├── Executor（必选）
        │               ├── Validator（按 team.md 可选）
        │               └── Explorer（按 team.md 可选）
        ├── Project Supervisor B
        │       └── Story Supervisor → ...
```

Project 是真实项目目录；Harness 是该项目在 `~/.perpetuum/projects/<project-id>/` 下的长期运行资料。`team.md` 保存用户确认的角色拓扑和完成门槛。一个 Project 在前端对应一个看板页面，一个 Story 文件对应一张卡片。

Runner 不是 Agent。它读取每个项目的 `schedule.yaml`，解释 cron，创建顶层交互式 Agent TUI，并维护完成回执和前端状态。Runner 不读取 Goal 或 Story，不判断项目是否值得工作，也不使用系统 cron 启动每一轮任务。

## 硬边界和软调度

Runner 确定性地完成：

1. 判断某个项目的 cron 是否在当前分钟匹配；
2. 确认该项目没有活动的 Project Supervisor；
3. 创建新的 tmux 和交互式 Codex 或 Claude Code TUI；
4. 发送一次包含项目、Harness、触发原因、Playbook、承载 session 和回执路径的启动 Prompt；
5. 根据回执或 session 消失回收顶层生命周期。

Project Supervisor 收到 Prompt 后，根据 Playbook、`team.md`、Harness 和真实现场决定选择哪张 Story、如何组织下级 Prompt，以及本轮是否应该正常 Idle。Runner 不定时向仍然存活的 TUI 重复发送固定 Prompt。

## 各层职责

- **Project Supervisor**：读取一个项目的 Harness、`team.md` 和 Story 元数据，处理人类输入，选择至多一张已有 Story，并保证项目同一时刻只有一个 Story 在执行。没有可运行 Story 时，只按队伍契约决定是否调用 Explorer。
- **Story Supervisor**：只服务已经选择的一张 Story，是该任务的调度者；按 `team.md` 管理必选 Executor 与可选 Validator、Explorer，并在结束前回收自己创建的 session。
- **Executor**：完成当前 Story。正常情况下一个 Story 只创建一个 Executor session，并允许跨天、多轮持续工作。
- **Validator**：可选的独立验收者。启用时先从 Goal、Story 和用户约束形成自己的风险模型，再检查产物；不把 Executor 的解释、unit test 或 smoke test 结论当作验收结论。
- **Explorer**：可选的未来工作探索者。只在 `team.md` 配置的触发点，根据事实研究差距并维护未来 Story。

## Story 工作链

`team.md` 必须显式给出调用图。默认建议是：

```text
Project Supervisor 从 Story 看板选择一张卡片
        ↓ cc-use
Story Supervisor 启动 Executor
        ↓
Executor 产生可验证结果
        ├── 未启用 Validator：Story Supervisor 按契约完成门槛判断
        └── 已启用 Validator：启动独立 Validator
                                ↓
             Validator 退回 ──→ 原 Executor 修改 ──→ 原 Validator 复验
                                ↓ 接受、等待或管控阻塞
保存 Story 结果和恢复上下文
        ↓
关闭本轮实际创建的 Executor 与 Validator
        ↓
若契约启用且满足触发条件，启动 Explorer 维护后续 Story
        ↓
关闭本轮实际创建的 Explorer 与 Story Supervisor
        ↓
Project Supervisor 写回执并由 Runner 回收
```

Validator 启用时，其多次退回和 Executor 的多次修改属于同一条连续 Story 工作链，不产生新的 Story 或新的执行循环。只有物理 session 丢失、损坏或无法恢复时才允许替换已创建的角色 session。

简单例行任务可以只启用 Executor。例如每日抓取新闻时，`team.md` 应同时约定每次激活的产物、去重与失败处理、本轮完成记录，以及下一轮如何继续，而不是为了凑齐架构固定启动 Validator 或 Explorer。

## 渐进式披露

Story 的 front matter 保存看板元数据，正文保存完整背景、边界、验收、进展和证据。Project Supervisor 和已启用的 Explorer 先通过 Perpetuum 的 Story 接口读取全部元数据，只打开少量候选或当前 Story 的正文。Executor 和已启用的 Validator 只读取当前 Story 及直接相关的 Goal、History 和证据。

脚本和前端统一使用 PyYAML 解析两个 `---` 分隔符之间的内容。完整格式见 [story.md](story.md)。

## 调用和所有权

Runner 直接创建 Project Supervisor 的顶层 TUI，因为 Runner 不是 Agent。Project Supervisor 以下的所有 Agent 上下级调用都使用当前安装的 `cc-use` Skill。Perpetuum 只用自然语言说明要创建、观察或关闭哪一个下级 session，不保存或复制 cc-use 的具体命令和参数。

每个 Supervisor 都运行在上级为它创建的承载 session 中，同时可以为下级创建直属子 session。当前承载 session 不属于它自己管理；每个父节点只管理本次由自己明确创建并保存了精确名称的直属子 session。全局 session 列表和项目状态只能用于观察，不能证明所有权。

父节点创建下级后，立即把 `start` 结构化结果中的精确 session 名称和角色写入项目运行事件及本轮所有权记录，再把名称写入首次 Prompt，并说明该 session 由上级管理。结束时先持久化 `finish` 的结构化 `shutdown`、`exit_code` 和时间，再清除活动记录。调用最终返回前，不根据中间状态、临时空输出或全局列表中已经找不到 session，推断创建、关闭或核验成功。

## 并发和动力

同一 Project 同时最多执行一个 Story。不同 Project 独立解释 cron，可以同时拥有各自的 Project Supervisor，不设置跨项目的全局上限。

1. 初始化根据 Goal、项目证据和人类确认建立第一批 Story。
2. Runner 在项目 cron 匹配时创建 Project Supervisor。
3. Project Supervisor 从 `in_progress` 或 `ready` Story 中选择一张。
4. Executor 和队伍契约中已启用的角色把该 Story 推进到稳定结果。
5. 若 Explorer 已启用且满足触发条件，由它基于结果维护下一轮 Story 池。
6. 下一次 cron 匹配时重复。若空看板 Explorer 按契约创建的是当前已到期的 `ready` Story，Project Supervisor 可以在本次激活中重新读取并立即选择；尚未到期或仅为候选的 Story 留待后续激活。

没有可运行 Story 时，Project Supervisor 只在队伍契约配置了该触发点时调用一次 Explorer；否则项目直接进入 Idle。
