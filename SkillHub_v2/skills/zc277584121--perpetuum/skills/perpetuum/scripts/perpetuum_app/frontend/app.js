const state = {
  status: null,
  selectedProjectId: null,
  project: null,
  documents: {},
  selectedDocument: "goal",
  selectedStory: null,
  scheduleMode: "simple",
  scheduleEditorProjectId: null,
  scheduleDirty: false,
};

const storyColumns = [
  {status: "candidate", label: "候选", description: "方向成立，仍需整理边界"},
  {status: "ready", label: "待开始", description: "可以进入工作链"},
  {status: "in_progress", label: "进行中", description: "当前正在推进"},
  {status: "waiting", label: "等待", description: "等待决定或外部条件"},
  {status: "done", label: "已完成", description: "已经通过验证"},
];

const documentDefinitions = {
  goal: {label: "Goal", path: "goal.md", access: "只读"},
  team: {label: "Agent 队伍", path: "team.md", access: "只读"},
  history: {label: "可信历史", path: "history.md", access: "只读"},
  inbox: {label: "Inbox", path: "inbox.md", access: "追加写入"},
  questions: {label: "业务问题", path: "questions.md", access: "追加回复"},
  escalations: {label: "管控异常", path: "escalations.md", access: "追加回复"},
  events: {label: "运行事件", path: "runtime/events.log", access: "只读"},
};

const drawerDefinitions = {
  attention: {kicker: "需要介入", title: "待处理", description: "集中处理业务判断和管控异常。"},
  inbox: {kicker: "业务输入", title: "补充项目方向", description: "新的要求会在 Project Supervisor 下次激活时被读取。"},
  documents: {kicker: "项目资料", title: "资料与历史", description: "按需读取 Goal、历史、通信文件和运行事件。"},
  settings: {kicker: "项目管控", title: "运行设置", description: "调整工作时间并查看 Agent 与 Session 状态。"},
  archive: {kicker: "看板历史", title: "已归档 Story", description: "查看较早完成、手工归档或已经取消的卡片。"},
};

async function request(path, options = {}) {
  const response = await fetch(path, {
    headers: {"Content-Type": "application/json"},
    ...options,
  });
  const body = await response.json();
  if (!response.ok) {
    throw new Error(body.error || "请求失败");
  }
  return body;
}

function showToast(message, error = false) {
  const toast = document.getElementById("toast");
  toast.textContent = message;
  toast.className = `toast visible ${error ? "error" : ""}`;
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => {
    toast.className = "toast";
  }, 3200);
}

function statusLabel(value) {
  const labels = {
    idle: "空闲",
    working: "工作中",
    waiting_human: "等待人类",
    control_blocked: "管控阻塞",
    paused: "已暂停",
    unknown: "未知",
  };
  return labels[value] || value || "未知";
}

function phaseLabel(value) {
  const labels = {
    executing: "执行中",
    validating: "验证中",
    exploring: "整理后续 Story",
  };
  return labels[value] || value || "工作中";
}

function waitingLabel(value) {
  const labels = {
    human: "等待人类",
    control: "等待管控处理",
    external: "等待外部条件",
  };
  return labels[value] || "等待中";
}

function formatTime(value, timezoneOverride = null) {
  if (!value) {
    return "暂无";
  }
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return value;
  }
  const timezone = timezoneOverride || state.status?.activation?.timezone || "Asia/Shanghai";
  try {
    return new Intl.DateTimeFormat("zh-CN", {
      timeZone: timezone,
      month: "numeric",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    }).format(date);
  } catch (_error) {
    return date.toLocaleString("zh-CN");
  }
}

function scheduleDescription(project) {
  return project.schedule_view?.description || "尚未配置运行计划";
}

function nextRunText(project) {
  const schedule = project.schedule || {};
  const view = project.schedule_view || {};
  const nextTime = view.next_run_at
    ? formatTime(view.next_run_at, schedule.timezone)
    : null;
  if (project.project_session) {
    return nextTime ? `当前正在运行 · 下一计划 ${nextTime}` : "当前正在运行";
  }
  if (project.paused || schedule.paused) {
    return "运行计划已暂停";
  }
  if (project.enabled === false || schedule.enabled === false) {
    return "运行计划未启用";
  }
  if (schedule.force_run) {
    return "已请求立即运行";
  }
  return nextTime ? `预计下次启动 ${nextTime}` : "暂无下一次启动";
}

function simpleScheduleFromForm() {
  const kind = document.getElementById("simple-kind").value;
  if (kind === "fixed") {
    return {
      kind,
      time: document.getElementById("simple-fixed-time").value,
    };
  }
  return {
    kind: "window",
    start: document.getElementById("simple-start-time").value,
    end: document.getElementById("simple-end-time").value,
    interval_minutes: Number(document.getElementById("simple-interval").value),
  };
}

function describeSimpleSchedule(schedule) {
  if (schedule.kind === "fixed") {
    return schedule.time ? `每天 ${schedule.time} 启动` : "请选择启动时间";
  }
  if (!schedule.start || !schedule.end || !schedule.interval_minutes) {
    return "请完整设置运行窗口";
  }
  let windowText = `每天 ${schedule.start}–${schedule.end}`;
  if (schedule.start === schedule.end) {
    windowText = `每天全天（从 ${schedule.start} 起）`;
  } else if (schedule.end < schedule.start) {
    windowText = `每天 ${schedule.start}–次日 ${schedule.end}`;
  }
  return `${windowText}，每 ${schedule.interval_minutes} 分钟启动`;
}

function definition(term, description) {
  const wrapper = document.createElement("div");
  const dt = document.createElement("dt");
  const dd = document.createElement("dd");
  dt.textContent = term;
  dd.textContent = description;
  wrapper.append(dt, dd);
  return wrapper;
}

function replaceDefinitions(target, rows) {
  target.replaceChildren(...rows.map(([term, description]) => definition(term, description)));
}

function renderMarkdown(target, source, emptyText = "暂无内容。") {
  target.replaceChildren();
  const text = String(source || "").trim();
  if (!text) {
    const empty = document.createElement("p");
    empty.className = "document-empty";
    empty.textContent = emptyText;
    target.appendChild(empty);
    return;
  }

  const lines = text.replace(/\r\n/g, "\n").split("\n");
  const isBlockStart = line => (
    /^#{1,4}\s+/.test(line)
    || /^```/.test(line)
    || /^\s*[-*]\s+/.test(line)
    || /^\s*\d+\.\s+/.test(line)
    || /^\s*>\s?/.test(line)
    || /^\s*\|/.test(line)
    || /^\s*---+\s*$/.test(line)
  );

  let index = 0;
  while (index < lines.length) {
    const line = lines[index];
    if (!line.trim()) {
      index += 1;
      continue;
    }

    const fence = line.match(/^```\s*(.*)$/);
    if (fence) {
      index += 1;
      const codeLines = [];
      while (index < lines.length && !/^```/.test(lines[index])) {
        codeLines.push(lines[index]);
        index += 1;
      }
      index += 1;
      const pre = document.createElement("pre");
      const code = document.createElement("code");
      code.textContent = codeLines.join("\n");
      pre.appendChild(code);
      target.appendChild(pre);
      continue;
    }

    const heading = line.match(/^(#{1,4})\s+(.+)$/);
    if (heading) {
      const level = Math.min(6, heading[1].length + 2);
      const element = document.createElement(`h${level}`);
      element.textContent = heading[2];
      target.appendChild(element);
      index += 1;
      continue;
    }

    const unordered = line.match(/^\s*[-*]\s+(.+)$/);
    if (unordered) {
      const list = document.createElement("ul");
      while (index < lines.length) {
        const match = lines[index].match(/^\s*[-*]\s+(.+)$/);
        if (!match) {
          break;
        }
        const item = document.createElement("li");
        item.textContent = match[1];
        list.appendChild(item);
        index += 1;
      }
      target.appendChild(list);
      continue;
    }

    const ordered = line.match(/^\s*\d+\.\s+(.+)$/);
    if (ordered) {
      const list = document.createElement("ol");
      while (index < lines.length) {
        const match = lines[index].match(/^\s*\d+\.\s+(.+)$/);
        if (!match) {
          break;
        }
        const item = document.createElement("li");
        item.textContent = match[1];
        list.appendChild(item);
        index += 1;
      }
      target.appendChild(list);
      continue;
    }

    if (/^\s*\|/.test(line)) {
      const tableLines = [];
      while (index < lines.length && /^\s*\|/.test(lines[index])) {
        tableLines.push(lines[index]);
        index += 1;
      }
      const pre = document.createElement("pre");
      pre.className = "markdown-table";
      pre.textContent = tableLines.join("\n");
      target.appendChild(pre);
      continue;
    }

    if (/^\s*>\s?/.test(line)) {
      const quote = document.createElement("blockquote");
      const quoteLines = [];
      while (index < lines.length && /^\s*>\s?/.test(lines[index])) {
        quoteLines.push(lines[index].replace(/^\s*>\s?/, ""));
        index += 1;
      }
      quote.textContent = quoteLines.join(" ");
      target.appendChild(quote);
      continue;
    }

    if (/^\s*---+\s*$/.test(line)) {
      target.appendChild(document.createElement("hr"));
      index += 1;
      continue;
    }

    const paragraphLines = [line.trim()];
    index += 1;
    while (index < lines.length && lines[index].trim() && !isBlockStart(lines[index])) {
      paragraphLines.push(lines[index].trim());
      index += 1;
    }
    const paragraph = document.createElement("p");
    paragraph.textContent = paragraphLines.join(" ");
    target.appendChild(paragraph);
  }
}

function extractSection(markdown, heading) {
  const lines = String(markdown || "").replace(/\r\n/g, "\n").split("\n");
  const start = lines.findIndex(line => line.trim() === `## ${heading}`);
  if (start < 0) {
    return "";
  }
  const result = [];
  for (let index = start + 1; index < lines.length; index += 1) {
    if (/^#{1,2}\s+/.test(lines[index])) {
      break;
    }
    result.push(lines[index]);
  }
  return result.join("\n").trim();
}

function hasPendingContent(content) {
  return content
    .replace(/暂无[。.]?/g, "")
    .replace(/[-*#`\s]/g, "")
    .trim().length > 0;
}

function renderService() {
  const runner = state.status?.runner || {};
  const service = runner.service || {};
  const alive = Boolean(service.alive);
  document.getElementById("service-dot").className = `status-dot ${alive ? "online" : "offline"}`;
  document.getElementById("service-status").textContent = alive ? "Runner 运行中" : "Runner 已停止";
  const active = Object.keys(runner.active_projects || {}).length;
  document.getElementById("service-detail").textContent = active
    ? `${active} 条顶层工作链活跃`
    : `下次检查 ${formatTime(runner.next_schedule_check_at)}`;
}

function renderProjects() {
  const list = document.getElementById("project-list");
  list.replaceChildren();
  for (const project of state.status.projects) {
    const button = document.createElement("button");
    button.className = "project-item";
    button.type = "button";
    if (project.id === state.selectedProjectId) {
      button.classList.add("selected");
    }

    const title = document.createElement("strong");
    title.textContent = project.name;
    const displayStatus = project.paused ? "paused" : project.status;
    const status = document.createElement("span");
    status.className = `project-state state-${displayStatus}`;
    status.textContent = statusLabel(displayStatus);
    const nextRun = document.createElement("span");
    nextRun.className = "project-next-run-line";
    nextRun.textContent = nextRunText(project);
    const schedule = document.createElement("small");
    schedule.className = "project-schedule-line";
    schedule.textContent = scheduleDescription(project);
    button.title = project.path;
    button.append(title, status, nextRun, schedule);
    button.addEventListener("click", () => selectProject(project.id));
    list.appendChild(button);
  }

  if (!state.status.projects.length) {
    const empty = document.createElement("p");
    empty.className = "sidebar-empty";
    empty.textContent = "尚未注册项目";
    list.appendChild(empty);
  }
}

function createStoryCard(story, runtime, archived = false) {
  const card = document.createElement("button");
  card.className = archived ? "archive-card" : "story-card";
  card.type = "button";
  if (runtime.current_story === story.id) {
    card.classList.add("active");
  }

  const top = document.createElement("div");
  top.className = "story-card-top";
  const priority = document.createElement("span");
  priority.className = `story-priority priority-${String(story.priority).toLowerCase()}`;
  priority.textContent = story.priority;
  const id = document.createElement("code");
  id.textContent = story.id;
  top.append(priority, id);

  const title = document.createElement("strong");
  title.textContent = story.title;
  const summary = document.createElement("p");
  summary.textContent = story.summary;

  const labels = document.createElement("div");
  labels.className = "story-labels";
  for (const label of (story.labels || []).slice(0, 4)) {
    const chip = document.createElement("span");
    chip.textContent = label;
    labels.appendChild(chip);
  }

  const footer = document.createElement("div");
  footer.className = "story-card-footer";
  const updated = document.createElement("span");
  updated.textContent = formatTime(story.updated_at);
  footer.appendChild(updated);
  if (archived) {
    const archiveContext = document.createElement("span");
    archiveContext.className = "story-context";
    archiveContext.textContent = story.archive_reason === "cancelled" ? "已取消" : "已归档";
    footer.appendChild(archiveContext);
  }
  if (runtime.current_story === story.id && runtime.story_phase) {
    const phase = document.createElement("span");
    phase.className = "story-context active";
    phase.textContent = phaseLabel(runtime.story_phase);
    footer.appendChild(phase);
  } else if (story.waiting_on) {
    const waiting = document.createElement("span");
    waiting.className = "story-context waiting";
    waiting.textContent = waitingLabel(story.waiting_on);
    footer.appendChild(waiting);
  }

  card.append(top, title, summary, labels, footer);
  card.addEventListener("click", () => openStory(story.id));
  return card;
}

function renderStoryBoard() {
  const board = document.getElementById("story-board");
  board.replaceChildren();
  const stories = Array.isArray(state.project.stories) ? state.project.stories : [];
  const runtime = state.project.runtime || {};

  for (const definition of storyColumns) {
    const column = document.createElement("section");
    column.className = `story-column story-column-${definition.status}`;

    const header = document.createElement("header");
    const heading = document.createElement("div");
    const title = document.createElement("h4");
    title.textContent = definition.label;
    const description = document.createElement("p");
    description.textContent = definition.description;
    heading.append(title, description);
    const columnStories = stories.filter(story => story.status === definition.status);
    const count = document.createElement("span");
    count.textContent = String(columnStories.length);
    header.append(heading, count);

    const cards = document.createElement("div");
    cards.className = "story-cards";
    for (const story of columnStories) {
      cards.appendChild(createStoryCard(story, runtime));
    }
    if (!columnStories.length) {
      const empty = document.createElement("p");
      empty.className = "column-empty";
      empty.textContent = "暂无 Story";
      cards.appendChild(empty);
    }
    column.append(header, cards);
    board.appendChild(column);
  }

  const openCount = stories.filter(story => !["done", "cancelled"].includes(story.status)).length;
  const archivedCount = (state.project.archived_stories || []).length;
  document.getElementById("open-story-count").textContent = String(openCount);
  document.getElementById("archived-story-count").textContent = String(archivedCount);
}

function renderArchive() {
  const list = document.getElementById("archive-list");
  list.replaceChildren();
  const runtime = state.project.runtime || {};
  const stories = state.project.archived_stories || [];
  for (const story of stories) {
    list.appendChild(createStoryCard(story, runtime, true));
  }
  if (!stories.length) {
    const empty = document.createElement("p");
    empty.className = "drawer-empty";
    empty.textContent = "还没有归档或取消的 Story。";
    list.appendChild(empty);
  }
}

function renderScheduleMode() {
  const simpleMode = state.scheduleMode === "simple";
  document.getElementById("schedule-simple-panel").classList.toggle("hidden", !simpleMode);
  document.getElementById("schedule-cron-panel").classList.toggle("hidden", simpleMode);
  for (const button of document.querySelectorAll("[data-schedule-mode]")) {
    button.classList.toggle("selected", button.dataset.scheduleMode === state.scheduleMode);
  }
}

function renderSimpleFields() {
  const fixed = document.getElementById("simple-kind").value === "fixed";
  document.getElementById("simple-fixed-fields").classList.toggle("hidden", !fixed);
  document.getElementById("simple-window-fields").classList.toggle("hidden", fixed);
}

function populateSimpleSchedule(simple) {
  if (!simple) {
    return;
  }
  document.getElementById("simple-kind").value = simple.kind;
  if (simple.kind === "fixed") {
    document.getElementById("simple-fixed-time").value = simple.time || "00:00";
  } else {
    document.getElementById("simple-start-time").value = simple.start || "00:00";
    document.getElementById("simple-end-time").value = simple.end || "06:00";
    document.getElementById("simple-interval").value = String(simple.interval_minutes || 30);
  }
  renderSimpleFields();
}

function renderScheduleSettings(summary) {
  const schedule = summary.schedule || {};
  const view = summary.schedule_view || {};
  const simple = view.simple || null;
  const cronInput = document.getElementById("cron-text");
  const timezoneInput = document.getElementById("schedule-timezone");

  if (!state.scheduleDirty) {
    cronInput.value = (schedule.cron || []).join("\n");
    timezoneInput.value = schedule.timezone || "Asia/Shanghai";
    populateSimpleSchedule(simple);
  }

  document.getElementById("schedule-description").textContent = state.scheduleDirty && state.scheduleMode === "simple"
    ? `将保存为：${describeSimpleSchedule(simpleScheduleFromForm())}`
    : scheduleDescription(summary);
  document.getElementById("schedule-next-run").textContent = nextRunText(summary);
  const note = document.getElementById("simple-mode-note");
  note.textContent = simple
    ? "易读设置与当前 Cron 表达的是同一份计划。"
    : "当前计划较复杂，无法自动还原成易读设置；在这里保存会用新的易读计划替换它。";
  note.classList.toggle("hidden", Boolean(simple));
  renderScheduleMode();
  renderSimpleFields();
}

function renderProject() {
  if (!state.project) {
    return;
  }
  const summary = state.project.summary;
  const runtime = state.project.runtime || {};
  const displayStatus = summary.paused ? "paused" : summary.status;
  const currentStory = (state.project.stories || []).find(story => story.id === summary.current_story);

  document.getElementById("empty-state").classList.add("hidden");
  document.getElementById("project-view").classList.remove("hidden");
  document.getElementById("project-actions").classList.remove("hidden");
  document.getElementById("project-name").textContent = summary.name;
  document.getElementById("project-path").textContent = summary.path;
  document.getElementById("project-updated").textContent = `更新于 ${formatTime(summary.last_activity_at)}`;
  document.getElementById("project-next-run").textContent = nextRunText(summary);

  const stateChip = document.getElementById("project-state-chip");
  stateChip.textContent = statusLabel(displayStatus);
  stateChip.className = `state-chip state-${displayStatus}`;

  const pauseButton = document.getElementById("pause-button");
  pauseButton.textContent = summary.paused ? "恢复" : "暂停";
  pauseButton.dataset.action = summary.paused ? "resume" : "pause";

  const attention = state.project.attention || {};
  const attentionCount = Number(Boolean(attention.questions)) + Number(Boolean(attention.escalations));
  const attentionBadge = document.getElementById("attention-count");
  attentionBadge.textContent = String(attentionCount);
  attentionBadge.classList.toggle("hidden", attentionCount === 0);

  if (currentStory) {
    document.getElementById("board-status-line").textContent = `${phaseLabel(runtime.story_phase)} · ${currentStory.title}`;
  } else if (summary.paused) {
    document.getElementById("board-status-line").textContent = "项目已暂停，不会开始新的 Story。";
  } else {
    document.getElementById("board-status-line").textContent = summary.last_result || "当前没有运行中的 Story。";
  }

  renderScheduleSettings(summary);
  renderStoryBoard();
  renderArchive();
  renderRuntimeDetails();
}

function renderRuntimeDetails() {
  const summary = state.project.summary;
  const runtime = state.project.runtime || {};
  const runner = state.status.runner || {};
  const project = state.project.project || {};
  const schedule = summary.schedule || {};
  const sessions = Array.isArray(runtime.active_sessions) ? runtime.active_sessions : [];
  const sessionSummary = sessions.length
    ? sessions.map(session => session.session || session.name || String(session)).join("，")
    : "无";
  replaceDefinitions(document.getElementById("runtime-details"), [
    ["Runner", runner.service?.alive ? "运行中" : "已停止"],
    ["Agent", project.agent?.kind || "未配置"],
    [
      "运行计划",
      schedule.error
        ? `无效：${schedule.error}`
        : `${summary.schedule_view?.description || "未配置"} · ${schedule.timezone || "未配置"}`,
    ],
    ["启动状态", nextRunText(summary)],
    ["项目状态", statusLabel(summary.paused ? "paused" : summary.status)],
    ["当前 Story", summary.current_story || "无"],
    ["工作阶段", runtime.story_phase ? phaseLabel(runtime.story_phase) : "无"],
    ["Story Session", sessionSummary],
    ["Project Supervisor", summary.project_session || "空闲"],
    ["Runner 下次检查", formatTime(runner.next_schedule_check_at)],
  ]);
}

async function loadDocument(key, force = false) {
  if (!state.selectedProjectId) {
    return {key, path: "", content: ""};
  }
  if (!force && state.documents[key]) {
    return state.documents[key];
  }
  const documentValue = await request(
    `/api/projects/${encodeURIComponent(state.selectedProjectId)}/documents/${encodeURIComponent(key)}`,
  );
  state.documents[key] = documentValue;
  return documentValue;
}

function renderPendingSection({documentValue, heading, cardId, stateId, contentId, formId, emptyText}) {
  const content = extractSection(documentValue.content, heading);
  const pending = hasPendingContent(content);
  document.getElementById(cardId).classList.toggle("needs-attention", pending);
  const badge = document.getElementById(stateId);
  badge.textContent = pending ? "待处理" : "无待办";
  badge.className = `pending-state ${pending ? "pending" : "clear"}`;
  document.getElementById(formId).classList.toggle("hidden", !pending);
  renderMarkdown(document.getElementById(contentId), pending ? content : "", emptyText);
}

async function renderAttentionDrawer() {
  const [questions, escalations] = await Promise.all([
    loadDocument("questions", true),
    loadDocument("escalations", true),
  ]);
  renderPendingSection({
    documentValue: questions,
    heading: "待人类回答",
    cardId: "question-card",
    stateId: "question-state",
    contentId: "question-content",
    formId: "question-response-form",
    emptyText: "当前没有需要你决定的业务问题。",
  });
  renderPendingSection({
    documentValue: escalations,
    heading: "待处理",
    cardId: "escalation-card",
    stateId: "escalation-state",
    contentId: "escalation-content",
    formId: "escalation-response-form",
    emptyText: "当前没有需要你介入的管控异常。",
  });
}

function renderDocumentTabs() {
  const tabs = document.getElementById("document-tabs");
  tabs.replaceChildren();
  for (const [key, definition] of Object.entries(documentDefinitions)) {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = definition.label;
    button.classList.toggle("selected", key === state.selectedDocument);
    button.addEventListener("click", async () => {
      state.selectedDocument = key;
      await renderDocumentsDrawer();
    });
    tabs.appendChild(button);
  }
}

async function renderDocumentsDrawer() {
  renderDocumentTabs();
  const definition = documentDefinitions[state.selectedDocument];
  const documentValue = await loadDocument(state.selectedDocument, true);
  const meta = document.getElementById("document-meta");
  meta.replaceChildren();
  const access = document.createElement("span");
  access.textContent = definition.access;
  const path = document.createElement("code");
  path.textContent = documentValue.path;
  meta.append(access, path);
  renderMarkdown(document.getElementById("document-content"), documentValue.content);
}

function setDrawerView(view) {
  for (const element of document.querySelectorAll(".drawer-view")) {
    element.classList.toggle("hidden", element.id !== `drawer-view-${view}`);
  }
  const definition = drawerDefinitions[view];
  document.getElementById("drawer-kicker").textContent = definition.kicker;
  document.getElementById("drawer-title").textContent = definition.title;
  document.getElementById("drawer-description").textContent = definition.description;
}

async function openProjectDrawer(view) {
  if (!state.selectedProjectId) {
    return;
  }
  closeStoryDrawer();
  closeCreateStoryDrawer();
  setDrawerView(view);
  document.getElementById("project-drawer").classList.remove("hidden");
  document.body.classList.add("drawer-open");
  try {
    if (view === "attention") {
      await renderAttentionDrawer();
    } else if (view === "documents") {
      await renderDocumentsDrawer();
    } else if (view === "settings") {
      renderRuntimeDetails();
    } else if (view === "archive") {
      renderArchive();
    }
  } catch (error) {
    showToast(error.message, true);
  }
}

function closeProjectDrawer() {
  document.getElementById("project-drawer").classList.add("hidden");
  updateDrawerLock();
}

async function openStory(storyId) {
  if (!state.selectedProjectId) {
    return;
  }
  closeProjectDrawer();
  closeCreateStoryDrawer();
  try {
    const story = await request(
      `/api/projects/${encodeURIComponent(state.selectedProjectId)}/stories/${encodeURIComponent(storyId)}`,
    );
    state.selectedStory = story;
    const metadata = story.metadata;
    document.getElementById("story-id").textContent = metadata.id;
    document.getElementById("story-title").textContent = metadata.title;
    document.getElementById("story-summary").textContent = metadata.summary;
    document.getElementById("story-title-input").value = metadata.title;
    document.getElementById("story-summary-input").value = metadata.summary;
    document.getElementById("story-status-select").value = metadata.status;
    document.getElementById("story-priority-select").value = metadata.priority;
    document.getElementById("story-labels-input").value = (metadata.labels || []).join(", ");
    document.getElementById("story-updated").textContent = `最近更新 ${formatTime(metadata.updated_at)}`;
    renderMarkdown(document.getElementById("story-body"), story.body, "Story 正文为空。");
    document.getElementById("story-drawer").classList.remove("hidden");
    document.body.classList.add("drawer-open");
  } catch (error) {
    showToast(error.message, true);
  }
}

function closeStoryDrawer() {
  state.selectedStory = null;
  document.getElementById("story-drawer").classList.add("hidden");
  updateDrawerLock();
}

async function saveStory() {
  if (!state.selectedStory || !state.selectedProjectId) {
    return;
  }
  const labels = document.getElementById("story-labels-input").value
    .split(",")
    .map(value => value.trim())
    .filter(Boolean);
  try {
    await request(
      `/api/projects/${encodeURIComponent(state.selectedProjectId)}/stories/${encodeURIComponent(state.selectedStory.metadata.id)}`,
      {
        method: "POST",
        body: JSON.stringify({
          title: document.getElementById("story-title-input").value,
          summary: document.getElementById("story-summary-input").value,
          status: document.getElementById("story-status-select").value,
          priority: document.getElementById("story-priority-select").value,
          labels,
        }),
      },
    );
    closeStoryDrawer();
    await loadStatus();
    showToast("Story 已更新");
  } catch (error) {
    showToast(error.message, true);
  }
}

function openCreateStoryDrawer() {
  if (!state.selectedProjectId) {
    return;
  }
  closeProjectDrawer();
  closeStoryDrawer();
  document.getElementById("create-story-drawer").classList.remove("hidden");
  document.body.classList.add("drawer-open");
  document.getElementById("create-title").focus();
}

function closeCreateStoryDrawer() {
  document.getElementById("create-story-drawer").classList.add("hidden");
  updateDrawerLock();
}

async function createStory() {
  const title = document.getElementById("create-title").value.trim();
  const summary = document.getElementById("create-summary").value.trim();
  if (!title || !summary) {
    showToast("标题和摘要不能为空", true);
    return;
  }
  const labels = document.getElementById("create-labels").value
    .split(",")
    .map(value => value.trim())
    .filter(Boolean);
  try {
    await request(
      `/api/projects/${encodeURIComponent(state.selectedProjectId)}/stories`,
      {
        method: "POST",
        body: JSON.stringify({
          title,
          summary,
          status: document.getElementById("create-status").value,
          priority: document.getElementById("create-priority").value,
          labels,
        }),
      },
    );
    for (const id of ["create-title", "create-summary", "create-labels"]) {
      document.getElementById(id).value = "";
    }
    document.getElementById("create-status").value = "ready";
    document.getElementById("create-priority").value = "P1";
    closeCreateStoryDrawer();
    await loadStatus();
    showToast("Story 已创建");
  } catch (error) {
    showToast(error.message, true);
  }
}

function updateDrawerLock() {
  const anyOpen = [...document.querySelectorAll(".drawer")]
    .some(element => !element.classList.contains("hidden"));
  document.body.classList.toggle("drawer-open", anyOpen);
}

async function loadProject(projectId) {
  const project = await request(`/api/projects/${encodeURIComponent(projectId)}`);
  if (state.scheduleEditorProjectId !== projectId) {
    state.scheduleEditorProjectId = projectId;
    state.scheduleMode = project.summary.schedule_view?.simple ? "simple" : "cron";
    state.scheduleDirty = false;
  }
  state.project = project;
  renderProject();
}

async function loadStatus(keepSelection = true) {
  try {
    state.status = await request("/api/status");
    if (!keepSelection || !state.status.projects.some(project => project.id === state.selectedProjectId)) {
      state.selectedProjectId = state.status.projects[0]?.id || null;
      state.documents = {};
    }
    renderService();
    renderProjects();
    if (state.selectedProjectId) {
      await loadProject(state.selectedProjectId);
    }
  } catch (error) {
    showToast(error.message, true);
  }
}

async function selectProject(projectId) {
  state.selectedProjectId = projectId;
  state.documents = {};
  state.selectedDocument = "goal";
  closeProjectDrawer();
  closeStoryDrawer();
  closeCreateStoryDrawer();
  renderProjects();
  try {
    await loadProject(projectId);
  } catch (error) {
    showToast(error.message, true);
  }
}

async function postProject(action, body) {
  if (!state.selectedProjectId) {
    return;
  }
  await request(
    `/api/projects/${encodeURIComponent(state.selectedProjectId)}/${action}`,
    {method: "POST", body: JSON.stringify(body)},
  );
  await loadStatus();
}

document.getElementById("refresh-button").addEventListener("click", () => loadStatus());
document.getElementById("new-story-button").addEventListener("click", openCreateStoryDrawer);
document.getElementById("create-story-submit").addEventListener("click", createStory);
document.getElementById("story-save").addEventListener("click", saveStory);

document.getElementById("project-actions").addEventListener("click", async event => {
  const panel = event.target.closest("[data-panel]")?.dataset.panel;
  if (panel) {
    await openProjectDrawer(panel);
    return;
  }
  const action = event.target.closest("[data-action]")?.dataset.action;
  if (!action) {
    return;
  }
  try {
    await postProject("control", {action});
    showToast(action === "run" ? "已请求立即运行" : "项目状态已更新");
  } catch (error) {
    showToast(error.message, true);
  }
});

document.getElementById("archived-button").addEventListener("click", () => openProjectDrawer("archive"));

document.getElementById("send-inbox").addEventListener("click", async () => {
  const input = document.getElementById("inbox-text");
  if (!input.value.trim()) {
    showToast("请输入要补充的内容", true);
    return;
  }
  try {
    await postProject("inbox", {text: input.value});
    state.documents.inbox = null;
    input.value = "";
    closeProjectDrawer();
    showToast("业务输入已写入 Inbox");
  } catch (error) {
    showToast(error.message, true);
  }
});

for (const button of document.querySelectorAll(".response-submit")) {
  button.addEventListener("click", async () => {
    const input = document.getElementById(button.dataset.input);
    if (!input.value.trim()) {
      showToast("请输入回复内容", true);
      return;
    }
    try {
      await postProject("response", {channel: button.dataset.channel, text: input.value});
      state.documents[button.dataset.channel] = null;
      input.value = "";
      await openProjectDrawer("attention");
      showToast("回复已提交");
    } catch (error) {
      showToast(error.message, true);
    }
  });
}

function markScheduleDirty() {
  state.scheduleDirty = true;
  if (state.project) {
    renderScheduleSettings(state.project.summary);
  }
}

for (const button of document.querySelectorAll("[data-schedule-mode]")) {
  button.addEventListener("click", () => {
    state.scheduleMode = button.dataset.scheduleMode;
    renderScheduleSettings(state.project.summary);
  });
}

for (const id of [
  "schedule-timezone",
  "cron-text",
  "simple-kind",
  "simple-fixed-time",
  "simple-start-time",
  "simple-end-time",
  "simple-interval",
]) {
  document.getElementById(id).addEventListener("input", markScheduleDirty);
  document.getElementById(id).addEventListener("change", markScheduleDirty);
}

document.getElementById("save-schedule").addEventListener("click", async () => {
  const crons = document.getElementById("cron-text").value
    .split("\n")
    .map(value => value.trim())
    .filter(Boolean);
  const timezone = document.getElementById("schedule-timezone").value.trim();
  const body = state.scheduleMode === "simple"
    ? {
      action: "schedule",
      mode: "simple",
      timezone,
      simple: simpleScheduleFromForm(),
    }
    : {action: "schedule", mode: "cron", cron: crons, timezone};
  try {
    state.scheduleDirty = false;
    await postProject("control", body);
    await openProjectDrawer("settings");
    showToast("运行计划已更新");
  } catch (error) {
    state.scheduleDirty = true;
    showToast(error.message, true);
  }
});

for (const element of document.querySelectorAll("[data-close-drawer]")) {
  element.addEventListener("click", closeProjectDrawer);
}
for (const element of document.querySelectorAll("[data-close-story]")) {
  element.addEventListener("click", closeStoryDrawer);
}
for (const element of document.querySelectorAll("[data-close-create]")) {
  element.addEventListener("click", closeCreateStoryDrawer);
}

document.addEventListener("keydown", event => {
  if (event.key === "Escape") {
    closeProjectDrawer();
    closeStoryDrawer();
    closeCreateStoryDrawer();
  }
});

loadStatus(false);
window.setInterval(() => loadStatus(), 15000);
