---
name: html-guide
description: >
  将任何内容（对话回答、笔记、代码、项目讲解、主题、URL）自动生成一份
  自包含（单文件、零外部依赖）、可交互、可打印、现代化视觉的 HTML 指导文档
  ——教程、指南、讲解页、操作手册、学习路径皆可，页面结构根据内容自适应。
  Always use this skill when the user wants content turned into a visual HTML
  guide page. Triggers: "做成HTML"、"HTML指南"、"可视化文档"、"网页教程"、
  "把这段内容整理成网页"、"页面化"、"生成一个好看的教学页面"、"
  make an HTML guide"、"render this as HTML"、"visualize content as HTML page"、
  "create an interactive tutorial page"。Whenever the user has explained something
  (a concept, a project, a piece of code) and then asks to see it as a polished
  HTML document, this skill should fire — even if they don't say "skill".
---

# HTML Guide Maker

把任意内容变成一份**单文件、可离线打开、美观、可交互**的 HTML 指导文档。

**核心流程**：`接收内容 → 判定文档类型 → 联网核实补充 → 按设计体系撰写 HTML → 自检 → 交付`

> [!IMPORTANT]
> ## 三条不可违背的硬规则
> 1. **单文件自包含**：最终产物必须是一个 `.html` 文件，CSS/JS/图标全部内联，
>    不得引用任何外部 CDN、字体、图片、样式表。双击即可离线打开。这是用户的核心诉求。
> 2. **联网核实**：涉及事实、数据、命令、版本、配置、概念定义时，必须先联网搜索核实，
>    不得凭记忆直接写死。核实的来源要收集起来放进页面的「参考来源」区。
> 3. **先判断再写**：动手前先判定内容属于哪种文档类型（见 structure-guide.md），
>    选择匹配的页面结构与组件，而不是套用固定模板。类型决定结构。

## 工作流程

### Step 1：接收与归一化内容

🚧 **GATE**：拿到用户给的内容。任何形式都可以：

| 用户给的内容 | 处理方式 |
|---|---|
| 对话中的回答 / 讲解 / 想法（当前上下文） | 直接采用，视为正文素材 |
| 粘贴的文字 / Markdown / 笔记 | 直接采用 |
| 本地文件（.md/.txt/.html/代码文件） | `Read` 读取 |
| 网页 URL | 用 `WebFetch`（或 curl 走代理）抓取正文，标注来源 |
| 只有一个主题 / 标题 | 视为「内容空缺」，正文主要由 Step 3 搜索补齐 |

先在心里（或草稿）梳理一遍：这份内容的**核心目标读者**是谁、要教会/说明**什么**、
有没有明显缺失的环节。缺的信息记下来，交给 Step 3。

**✅ 检查点：内容已归一化为可用正文，可判定文档类型。**

### Step 2：判定文档类型（自适应结构）

🚧 **GATE**：Step 1 完成。

按 signals 判定内容属于哪种 archetype，然后选择匹配的结构。**判定信号与每种类型的
推荐章节结构、组件清单都在 `references/structure-guide.md`**。判定规则：

- 内容包含**步骤/流程/命令序列** → `procedure`（操作教程）
- 内容在**解释一个概念/机制/原理** → `explainer`（知识讲解）
- 内容在**帮读者做选择/比较方案** → `decision`（决策指南）
- 内容是**知识点汇总/速查** → `reference`（参考手册）
- 内容包含**大量代码/配置文件** → `code-guide`（代码指南，可与其他类型叠加）
- 混合内容 → 识别主体类型，再叠加次要类型的局部组件（如讲解中嵌一段操作步骤）

**先读 `references/structure-guide.md` 对应章节再动手**，不要凭感觉编结构。

**✅ 检查点：文档类型已判定，页面骨架（章节顺序）已确定。**

### Step 3：联网核实与补充（必做）

🚧 **GATE**：Step 2 完成；已列出需要核实/补充的信息点。

> 你的环境有一个本地代理 **`127.0.0.1:7896`（Clash）**。系统代理已指向它，
> `WebSearch` / `WebFetch` 工具默认走系统代理即可正常工作。具体配置与降级方案见
> `references/search-guide.md`。

对以下信息点**逐条**联网核实或补充（代理配置、降级策略、引用规范都在 search-guide.md）：

1. **事实类**：数字、日期、比例、人物、公司、事件 —— 核对数值是否准确
2. **命令/代码/配置**：命令参数、API 用法、配置字段 —— 对照官方文档或权威来源
3. **版本与时效**：软件版本号、是否已过时、当前推荐做法 —— 用当前年份的检索词
4. **概念定义**：对核心概念给一个权威、通俗的表述
5. **内容空缺**：用户只给主题时，正文主体靠这一步补齐

搜索不一定要全覆盖 —— 优先核实那些**写错代价高**的点（命令、数字、版本）。
常识性、无争议的内容不必为搜而搜。

每核实一条，记录「来源 URL + 标题」，最后统一放进页面的 **参考来源** 区。

**✅ 检查点：关键信息已核实，来源清单已就绪。**

### Step 4：撰写 HTML

🚧 **GATE**：Step 3 完成；来源清单就绪。

1. **读参考**：先读 `references/design-system.md`（视觉规范与组件用法），
   再读 `references/structure-guide.md` 对应类型的章节。两个都读，别跳过。
2. **用骨架**：以 `assets/skeleton.html` 为起点 —— 它已包含设计令牌、
   基础 CSS、暗色模式、打印样式、目录/复制/滚动高亮、Ctrl+K 章节跳转、阅读时长估算、
   标题锚点、顶部进度条的 JS。**在骨架的 body 内**按
   Step 2 确定的章节结构撰写正文。骨架是地基，不是不可改 —— 组件都要用
   design-system 里定义的类名，保证风格统一。
3. **撰写原则**：
   - 正文质量第一：内容准确（Step 3 已核实）、组织清晰、详略得当，忠实于用户给的内容，不擅自膨胀
   - 「指导性」体现在：给读者清晰的路径（先做什么、再做什么）、明确的产出预期（步骤用
     `.step-result` 与步骤同框）、常见的坑与对策
   - **页面设计为内容服务**：先想读者读完想带走什么，再选结构；能用表格就不用卡片硬撑。
     同时遵守 `design-system.md §1.5 反 AI 味`——节奏有起伏、颜色有目的、避免模板腔
   - **表格不横向滚动**：列多先精简/合并/拆表（约 ≤6 列）；竖向过长（>12 行）用
     `<details class="fold">` 折叠。读者要能整表一眼看全，横拖是最后的兜底（design-system §4.4）
   - **有真实得分就给图**：对比/横评页收集到基准分（AA 指数、Elo、Benchmark 分）时，
     用 `.barchart` 柱状图 + 得分明细表呈现，别只堆文字；**占比/构成数据**（厂商份额、
     难度分布）用 `.donut` 环形图 + 图例（design-system §4.29 / §4.30）
   - 正文引用写成**可点击上标** `<sup><a href="#src-1">[1]</a></sup>`，来源项带
     `id="src-1"`（点击跳到来源）
   - 骨架内置了深浅色切换、语法高亮、自动目录、代码复制（自动剔除 `$` 提示符）、
     Ctrl+K 章节跳转、阅读时长估算、标题锚点、顶部进度条、跳到正文——**不要删**，
     这些是页面的标准能力
   - 可选组件按需用：`<details class="fold">` 折叠进阶/可选内容、`<pre class="linenos">`
     显示代码行号、`<span class="em">` 中文着重号（用法见 design-system §4.23–4.28）
   - 全部文字用 `<html lang="...">` 与用户语言一致（默认中文）
   - 文中涉及的技术关键词用 chips 标签组呈现，避免清一色
4. **命名与保存**：文件名有意义（如 `python-scrapy-tutorial.html`），
   保存到当前工作目录或用户指明的位置。单个 HTML 文件。

**✅ 检查点：HTML 撰写完成。**

### Step 5：自检与交付

🚧 **GATE**：Step 4 完成；HTML 文件已保存。

1. **跑校验脚本**：
   ```bash
   python scripts/check_html.py <输出的.html路径>
   ```
   `error` 必须修复（非自包含、缺 viewport、缺打印样式等）；`warning` 尽量修复。
   修复后重跑直到 0 error。
2. **结构自检**（不打开浏览器）：通读一遍生成的 HTML，核对——目录锚点与章节 id 一一对应、
   代码复制按钮已由骨架 JS 统一处理、暗色模式有 `prefers-color-scheme` 覆盖、callout 用的
   都是语义类名。**表格不横向滚动**（列多→精简/合并/拆表，竖向 >12 行→`details.fold` 折叠，
   且外套 `table-wrap`）。新特性检查：正文链接有下划线、用了 `class="linenos"` 的代码块行号
   与代码行对齐、Ctrl+K 弹层不遮挡正文、折叠的进阶内容在打印时会强制展开、得分柱状图
   `.barchart` 的 `--v` 宽度与数值匹配且标注了量表、环形图 `.donut` 的 `--v` 与多段
   `--a1..--a5` 加总≈100 且配了图例。发现布局隐患当场修复。
3. **无头渲染验证（强烈建议）**：骨架的 JS 功能（语法高亮/目录/复制/Tab/小测）一旦被改写
   很容易悄悄失效（历史教训：`innerText` 依赖布局、`querySelector` 中文 id 会抛错，
   一个 bug 会让整页高亮失灵）。用无头 Chrome 渲染一次并检查关键标记，不弹窗：
   ```bash
   "C:/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu \
     --dump-dom "file:///C:/.../output.html" > %TEMP%/dom_check.txt
   grep -c "tok-keyword" %TEMP%/dom_check.txt   # 语法高亮是否真的渲染出来了（应 >0）
   grep -c 'id="toc"' %TEMP%/dom_check.txt      # 目录存在
   grep -c 'class="plink"' %TEMP%/dom_check.txt # 标题锚点已由 JS 生成（应 >0）
   grep -c 'aria-current="true"' %TEMP%/dom_check.txt  # 目录活动项（应 >0）
   grep -c 'class="ln-gutter"' %TEMP%/dom_check.txt    # 行号 gutter（用了 .linenos 时 >0）
   ```
   没有 Chrome 或 headless 不可用则跳过，但至少用 `scripts/check_html.py` 兜底。
4. **清理临时文件（必做）**：无头验证产生的 `dom*.txt` 等临时文件**只放临时目录**，
   或验证后删除——**输出目录里只保留最终的 .html**。评测反馈点名过临时文件混进成品。
4. **⚠️ 严禁自动弹出浏览器**：你运行在用户的真实桌面会话里，`webbrowser.open` /
   `os.startfile` / `start` / 任何预览服务都会在用户屏幕上弹出窗口，造成干扰，**禁止使用**。
   需要视觉确认时，把文件路径告诉用户，让用户自己选择打开。
5. **交付**：把文件路径告诉用户，一句话说明这份文档的结构与来源数量。如用户需要，
   可再导出 PDF（浏览器打印 → 另存为 PDF）。

**✅ 完成。**

---

## 参考资源

| 资源 | 路径 | 何时读 |
|---|---|---|
| 视觉设计体系（配色/字体/间距/组件） | `references/design-system.md` | 每次写 HTML 前必读 |
| 文档类型→结构映射 | `references/structure-guide.md` | 每次 Step 2 判定后读对应章节 |
| 联网搜索与代理（7896） | `references/search-guide.md` | Step 3 联网前必读 |
| HTML 骨架模板 | `assets/skeleton.html` | 每次 Step 4 作为起点 |
| 校验脚本 | `scripts/check_html.py` | Step 5 自检 |

## Notes

- **Windows**：命令用 `python`（不是 `python3`，python.org 安装版没有 `python3.exe`）。
- **不要把普通问答升级成 HTML**：只有当用户明确要「HTML/网页/页面化」时才触发本 skill；
  否则正常回答即可。
- 若用户之后对生成的页面提出修改（改配色、加章节、改结构），直接改对应 HTML 重新交付，
  不必重跑整个流程。
