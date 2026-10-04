# 运行时

## 目录

```text
~/.perpetuum/
├── activation.yaml
├── runner/
│   ├── state.json
│   ├── events.log
│   └── runs/<run-id>/
│       ├── dispatch.json
│       └── receipt.json
└── projects/<project-id>/
    ├── project.yaml
    ├── schedule.yaml
    ├── goal.md
    ├── team.md
    ├── stories/
    │   └── S-*.md
    ├── history.md
    ├── inbox.md
    ├── questions.md
    ├── escalations.md
    └── runtime/
        ├── state.json
        └── events.log
```

`activation.yaml` 只保存全局服务和项目注册；`project.yaml` 保存项目目录与 Agent 类型；`team.md` 保存用户确认的角色编排；`schedule.yaml` 保存该项目自己的运行计划；`runner/runs/` 是一次顶层调用的临时交接目录，完成后清理。

## 项目运行计划

每个项目的 `schedule.yaml` 使用：

```yaml
version: 1
timezone: Asia/Shanghai
enabled: true
paused: false
force_run: false
cron:
  - "*/5 0-5 * * *"
```

只支持标准五字段 cron：

```text
分钟 小时 日 月 星期
```

前端提供“易读设置”和“Cron 表达式”两种编辑方式。易读设置覆盖每天固定时间、每天在一个时间窗口内按间隔启动等常见计划；复杂计划继续使用 Cron。两种方式最终都只写入 `schedule.yaml` 的 `cron`，不会维护第二套配置。项目列表和项目页会根据项目时区显示人类可读计划与预计下次启动时间；暂停或停用时不显示虚假的启动时间。

Runner 常驻运行并在进程内解释这些表达式，不调用 Linux cron、Windows Task Scheduler 或 systemd timer 启动每个 Project Supervisor。相同项目在同一个 cron 分钟只触发一次；已有活动 Project Supervisor 时不创建第二个，也不向原 TUI 追加启动 Prompt。

`force_run` 由“立即运行”控制写入，Runner 消费后自动恢复为 `false`。`paused` 阻止新激活；它不结束已经运行的 Story。

`schedule.yaml` 是这些可变运行控制的唯一当前事实来源。Goal、History 和 `team.md` 可以记录默认策略、授权边界和过去决定，但不要复制一个会过期的“当前 paused/enabled 值”。Runner 已经创建本轮 Project Supervisor 后再暂停项目，只阻止后续激活，不撤销当前工作链已经获得的业务授权。

## 一次项目激活

cron 匹配或收到立即运行请求后：

1. Runner 创建新的 tmux 和交互式 Codex 或 Claude Code TUI；
2. Runner 生成 `dispatch.json` 和 `receipt.json` 路径；
3. Runner 向 Project Supervisor 发送一次中文启动 Prompt；
4. Project Supervisor 读取 Harness 和 `team.md`，选择至多一张 Story，并通过 cc-use 启动 Story Supervisor；
5. Story 达到完成、等待、管控阻塞或本轮正常 Idle 后，Project Supervisor 关闭直属 session、更新状态并原子写入回执；
6. Runner 看到回执后回收 Project Supervisor TUI 并清理临时运行目录。

当 `team.md` 配置了空看板 Explorer 时，Project Supervisor 可以在步骤 4 内先让 Explorer 创建当前已到期的 `ready` Story，再在同一次激活中选择它；Runner 不需要为这张新卡额外触发第二次 cron。

cron 只限制新的激活开始。已经启动的 Story 可以跨出匹配时间继续完成，不设置固定 Story 时长。

## 项目状态

- `idle`：当前没有 Story session 在运行；
- `working`：正在执行或验证一张 Story；
- `waiting_human`：当前 Story 已保存现场并关闭 session，等待人类业务决定；
- `control_blocked`：当前 Story 已保存现场并关闭 session，等待环境或运行机制恢复；
- `paused`：人类已暂停该项目开始新 Story。

`runtime/state.json` 使用：

```json
{
  "version": 1,
  "status": "idle",
  "current_story": null,
  "story_phase": null,
  "active_sessions": [],
  "last_activity_at": "...",
  "last_result": "..."
}
```

`story_phase` 可以是 `executing`、`validating` 或 `exploring`；未启用对应可选角色时不会进入其阶段。`active_sessions` 是各层尽力记录，不是 cc-use 或 tmux 的全局权威清单，也不授予关闭权限。每个父 Supervisor 仍须在创建直属角色时保存 `start` 返回的精确名称，并在关闭时把 `finish` 的结构化结果追加到 `runtime/events.log`；列表中不存在只能说明当前不可见，不能证明曾经 graceful 关闭。

Runner 的 `state.json` 使用 `active_projects` 按项目记录顶层 Project Supervisor，因此不同项目可以并行。顶层 tmux session 只是本次激活的 carrier；完成回执才是整条 ownership chain 正常结束的权威信号。

顶层 carrier 消失但回执尚未出现时，Runner 在对应的 `active_projects` 记录中按需持久化：

```json
{
  "carrier_missing_since": "...",
  "top_session_orphaned_at": "...",
  "chain_settled_since": "..."
}
```

首次发现 carrier 消失时，Runner 记录 `carrier_missing_since` 和 `top_session_missing`，继续保留项目活动锁与本次运行目录。五分钟后仍没有回执时记录 `top_session_orphaned`，但下层 Story Supervisor、Executor 或其他直属角色仍可能继续运行，因此不会仅凭 carrier 消失释放项目。

Runner 只在项目 `runtime/state.json` 提供了 carrier 消失之后的新证据时开始认定 ownership chain 已经稳定：`last_activity_at` 严格晚于 `carrier_missing_since`、`current_story` 为空、`active_sessions` 为空，并且 `status` 是 `idle`、`waiting_human` 或 `control_blocked`。满足这些条件后记录 `chain_settled_since`；条件中途不再满足时清除该时间并重新等待。稳定状态连续保持五分钟且仍无回执时，Runner 写入 control escalation、释放项目活动锁，并保留完整运行目录作为调查证据。旧的 idle 状态、`working` 状态、仍有 `current_story` 或 `active_sessions` 的状态都不能触发自动释放。

回执检查始终先于这些丢失状态。即使 carrier 已经 orphaned 或 ownership chain 已进入稳定等待，延迟到达的回执仍会正常完成本次激活并清理运行目录。carrier 在释放前恢复时，Runner 清除 `carrier_missing_since`、`top_session_orphaned_at` 和 `chain_settled_since`，继续按正常活动 session 管理。

## 等待时关闭

Story 需要等待人类、管控处理或长期外部条件时：

1. 更新 Story 正文的当前进展、证据、等待原因和恢复上下文；
2. front matter 改为 `status: waiting`，并写入 `waiting_on`；
3. 业务问题写入 `questions.md`，管控异常写入 `escalations.md`；
4. 关闭本轮实际创建的 Executor、可选角色和 Story Supervisor session；
5. 清空 `current_story`、`story_phase` 和 `active_sessions`；
6. Project 后续可以执行其他 `ready` Story。

人类回答或条件恢复后，把原 Story 改回 `ready`，下一次使用新的物理 session 恢复同一个 Story。已启用 Validator 的普通退回不属于等待，继续使用原 Executor 和原 Validator。

## Prompt 和回执

Runner 的启动 Prompt 是确定性的最小信封，提供项目、Harness、触发原因、Playbook、承载 session、dispatch 和回执路径。它不指定必须选择哪张 Story，不包含 cc-use 的具体命令，也不按时间重复发送。

Project Supervisor 的业务调度是软性的：根据 Playbook、Story 看板、人类输入和真实结果决定选择、Idle、等待和下级 Prompt。写回执前必须关闭并复核自己创建的全部直属 session。Runner 不通过屏幕文本判断业务完成。

## 常用入口

```bash
<skill-directory>/scripts/perpetuum init
<skill-directory>/scripts/perpetuum start
<skill-directory>/scripts/perpetuum status
<skill-directory>/scripts/perpetuum project list
<skill-directory>/scripts/perpetuum project schedule <project-id> "*/5 0-5 * * *" --timezone Asia/Shanghai
<skill-directory>/scripts/perpetuum story list <project-id> --json
<skill-directory>/scripts/perpetuum stop
```

`start` 发现同一 home 的前端已经运行时直接复用；发现不同 home 或其他服务占用端口时明确报错，不自动换端口或结束其他服务。

前端默认只监听 `127.0.0.1:8765`。从另一台电脑查看远程 Linux 机器时使用 SSH 端口转发：

```bash
ssh -L 8765:127.0.0.1:8765 <server>
```

然后在本地打开 `http://127.0.0.1:8765`。默认不要把前端直接监听到公网地址。
