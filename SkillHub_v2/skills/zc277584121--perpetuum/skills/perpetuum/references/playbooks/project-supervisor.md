# Project Supervisor Playbook

Project Supervisor 管理一个项目的业务入口和管控状态，不直接替代 Executor 或 `team.md` 中启用的可选角色。当前一个项目同时最多执行一个 Story。

## 每次启动

1. 读取 Runner dispatch、`project.yaml`、`schedule.yaml`、`goal.md`、`team.md`、`history.md`、`inbox.md`、`questions.md`、`escalations.md` 和 `runtime/state.json`。若 `team.md` 缺失、仍是未确认模板、未启用 Executor 或调用图含糊，记录 Question 并正常停止，不自行补全队伍。
2. 吸收尚未处理的人类指令与回复，并记录它们怎样改变 Story、优先级、资源或边界。
3. 使用 Perpetuum Story 接口只读取全部 Story front matter；不要一开始打开所有正文。
4. 若状态和自己保存的所有权记录证明已有 Story Supervisor 正在运行，优先恢复、观察或记录异常，不启动第二个 Story。全局 session 列表和 `active_sessions` 不能证明所有权。

`schedule.yaml` 是 `enabled`、`paused`、时区和 cron 当前值的唯一事实来源。Goal、History 或 `team.md` 中的初始化状态只说明当时决定，不能覆盖后来的人类 pause/resume 操作。Runner 已经为本轮创建承载 session 时，即使项目随后被暂停，本次已开始的激活仍继续到稳定结果；暂停只阻止未来激活。只有新的明确人类指令撤销本轮业务或外部副作用授权时才停止，并按取消或等待流程保存现场。

## 选择 Story

没有 Story 正在运行时：

1. 有 `in_progress` Story 时优先恢复，并读取其完整正文；
2. 否则从 `ready` Story 中先按优先级筛选，再根据 Goal、最近结果、人类输入、资源和依赖读取少量候选正文，选择一张当前最值得执行的 Story；
3. `candidate`、`waiting`、`done` 和 `cancelled` 不直接开始；
4. 没有 `in_progress` 或 `ready` Story 时，只有 `team.md` 启用 Explorer 且明确配置了空看板触发点，才单独创建一次 Explorer session 刷新看板，再重新读取元数据；
5. 空看板 Explorer 新建了已经到期、边界完整且可立即执行的 `ready` Story 时，在同一次项目激活中继续选择它；Explorer 只产生未来候选、没有创建 Story、发现本周期实例已经存在或仍未产生可运行 Story时，项目正常 Idle。

Project Supervisor 做轻量调度判断，不重复 Explorer 的全面研究，也不机械选择“最新创建”的卡片。

## 启动 Story

为选中的 Story 创建唯一 Story Supervisor session，并在首次 Prompt 中至少说明：

- 项目真实目录、Harness 绝对路径和 Story 文件绝对路径；
- `team.md` 绝对路径，以及本 Story 适用的角色启用策略、职责、调用顺序和完成门槛；
- Story ID、标题、摘要和为什么本次选择它；
- 当前承载 Story Supervisor 的 session 精确名称及上级所有权；
- 长期 Goal、可信 History、已处理的人类输入和当前资源；
- 需要读取的 Story Supervisor Playbook；
- 本次只服务这一张 Story；
- 需要返回最终状态、证据、Questions、Escalations，以及已启用 Explorer 对后续看板的调整；
- 结束前只关闭自己明确创建并保存名称的直属角色 session。
- 最终返回结构化 `direct_sessions`，逐条包含角色、精确名称、创建时间、关闭时间、`finish` 的 `shutdown`/`exit_code` 和是否核验；缺证据时明确返回管控缺口。

不要在 Story 开始前固定调用 Explorer，也不要发送与当前证据无关的“继续”Prompt。只有 Story Supervisor 返回实际结果、请求澄清、人类补充决定或外部条件实质变化时才继续对话。

## 人类回答与恢复

吸收 `questions.md` 或 `escalations.md` 的人类回复后，定位关联 Story，把决定写入 Story 正文。条件已经满足时将 `waiting` 改为 `ready`，清理当前等待字段并保留问题 ID 作为历史关联。恢复仍是同一个 Story，但使用新的 Story Supervisor、Executor 和按 `team.md` 启用的可选角色 session。

## 结束时

关闭并复核本次明确创建且保存了精确名称的直属 Story Supervisor 或按契约创建的 Explorer session，先把每次 `finish` 的结构化结果写入 `runtime/events.log`。更新 `runtime/state.json` 后，再按 Runner dispatch 原子写入完成回执。回执至少包含 `status`、`summary`、`project_id`、`finished_at` 和结构化 `direct_sessions`；下级返回的生命周期缺口必须保留在回执中。写完后等待 Runner 回收当前承载 session；不要自行关闭它，也不要根据全局列表清理来源不明的 session。

无人值守运行期间，不自动更新 Codex、Claude Code、模型或认证配置。
