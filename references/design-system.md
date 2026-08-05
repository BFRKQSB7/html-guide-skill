# 视觉设计体系

本文件定义 html-guide 输出页面的视觉语言：设计令牌、排版、组件库。所有页面都必须
以 `assets/skeleton.html` 为起点，这里解释了每个令牌和组件的**语义与用法**，帮助你
判断什么时候该用什么，而不是照抄。

> 核心目标：一份**专业、清晰、有呼吸感**的文档页面，读者能扫读、能跳转、能复制，
> 打印和转 PDF 后依然可读。克制比华丽更重要 —— 页面是内容的容器，不是炫技场。

---

## 1. 设计令牌（design tokens）

页面用 CSS 自定义属性定义令牌，`skeleton.html` 已内置 `:root`（浅色）与
`@media (prefers-color-scheme: dark)`（深色）两套。以下是语义，改值时两套要一起改，
并保证对比度（正文/背景 ≥ 4.5:1，大字号 ≥ 3:1）。

### 颜色

| 令牌 | 浅色 | 深色 | 用途 |
|---|---|---|---|
| `--bg` | `#f7f5f2`（暖纸色，非纯白） | `#0b1220` | 页面底色 |
| `--bg-soft` | `#efece7` | `#0f172a` | 区块底色（表格条纹、次要容器） |
| `--surface` | `#ffffff` | `#111a2e` | 卡片 / 提示块 / 代码块底色 |
| `--surface-2` | `#eae6e0` | `#1e293b` | 悬浮项、次级卡片 |
| `--border` | `#e5e1da` | `#2b3a52` | 边框、分隔线 |
| `--text` | `#1e293b` | `#e2e8f0` | 正文 |
| `--text-2` | `#475569` | `#94a3b8` | 次级文字 |
| `--text-3` | `#64748b` | `#64748b` | 弱化文字（注、元信息） |
| `--accent` | `#4f46e5` | `#818cf8` | 主色：标题强调、链接、高亮 |
| `--accent-2` | `#0d9488` | `#2dd4bf` | 次强调色：第二视觉焦点、标签、图表 |
| `--accent-soft` | `#eef2ff` | `rgba(129,140,248,.14)` | 主色浅底（强调文字背景） |
| `--link` | `#4338ca` | `#a5b4fc` | 链接 |
| `--code-bg` | `#0f172a` | `#050a14` | 代码块背景（深浅一致，保证对比） |
| `--code-ink` | `#e2e8f0` | `#e2e8f0` | 代码块文字 |

### 语义色（callout / 状态用）

| 语义 | 主色（浅/深） | 浅底 `*-bg` | 用途 |
|---|---|---|---|
| info | `#0284c7` / `#38bdf8` | `#f0f9ff` | 补充信息、说明 |
| tip | `#059669` / `#34d399` | `#ecfdf5` | 建议、技巧、最佳实践 |
| warning | `#d97706` / `#fbbf24` | `#fffbeb` | 注意、坑、易错点 |
| danger | `#dc2626` / `#f87171` | `#fef2f2` | 警告、禁止、高风险 |
| ok | `#047857` / `#34d399` | `#d1fae5` | 支持/通过（表格 `tag-ok`） |
| no | `#b91c1c` / `#f87171` | `#fee2e2` | 不支持/失败（表格 `tag-no`） |

### 其他

- **圆角**：`--radius-sm: 6px`（小控件）、`--radius: 10px`（卡片、代码块）、
  `--radius-lg: 14px`（hero、大容器）
- **间距基准**：8px 网格。正文段落间距 1em；区块间 `--space: clamp(2.5rem, 6vw, 4rem)`
- **阴影**：卡片默认 `0 1px 2px rgba(15,23,42,.06)`；悬浮 `0 4px 16px rgba(15,23,42,.10)`
- **内容列宽**：正文容器 `max-width: 46rem`（约 740px），留出呼吸感；代码块可更宽

---

## 1.5 反 AI 味（重要）

评测反馈：默认风格"AI 味"很浓，用户能一眼认出。**AI 味 = 千篇一律**：每个区块都是
同款圆角卡片+浅阴影、通篇一个主色、排版没有节奏变化、出现"这是 X 的指南，能帮你……"
式的套话。要消除它，写页面时做这几件事：

- **节奏有起伏**：不是所有内容都是卡片。纯文本段落、代码、表格、卡片、流程图穿插，
  阅读节奏像真人写的文章，而不是一屏卡片雨。能用表格表达就别强行套卡片。
- **颜色有目的**：主色用于强调，`--accent-2`（次强调色）用于第二视觉焦点（标签、
  图表、高亮项）。表格、流程图、进度条不要清一色同一种蓝——用语义色区分状态。
- **避免模板腔**：不要写"在本指南中，你将学会……"这类套话开场。直接给结论或场景。
  标题要具体（"安装 Scrapy"优于"开始"），别用"快速上手""高级技巧"这种万能标题。
- **细节见人味**：留一个与内容强相关的具体例子、一句人话的比喻、一个真实的坑。
  这些是"写给人看"的证据。
- **交互服务于内容**：每个交互元素都要有明确用途。炫技型交互（意义不明的折叠、
  动画）会被用户质疑——"页面设计是要为内容服务的"。用之前问：没有它读者会损失什么？
- **别让教程看起来像产品首页**：教程/讲解页的核心是"带读者走一遍"的叙事感，
  不是卖点陈列。避免一上来就是大标题 + 几个营销式卡片；开场直接给结论或场景更对。
- **别让 hero 像"付费课程/骗子网站"的营销横幅**：满屏 emoji、刺眼亮色渐变、超大
  "限时优惠式"标题会劝退。hero 克制：标题 + 一句副标题 + 元信息即可（评测反馈点名）。
- **少量 emoji 点缀可接受**：在元信息（📅 日期、🕐 阅读时长）或列表用少量 emoji
  缓解单调，但正文不要滥用。
- **交工前确认关键 JS 真的生效**：高亮、目录、复制、小测这些骨架功能，若被改写很可能
  悄悄失效。生成后跑一次静态校验，能 headless 渲染就验证一下（见 SKILL Step 5）。

## 2. 排版

- 字体栈（skeleton 已内置，中文优先）：
  - 正文：`-apple-system, "Segoe UI", "Microsoft YaHei", "PingFang SC", "Noto Sans SC", "Helvetica Neue", Arial, sans-serif`
  - 代码：`"JetBrains Mono", "Cascadia Code", Consolas, "Liberation Mono", "Courier New", monospace`
- **字号**：正文 `16px`，行高 `1.7`（CJK 需要更宽的行高才易读）。
  `h1` 约 `2rem`+，`h2` `1.5rem`，`h3` `1.2rem`。h2/h3 上方留足间距，与上节区分。
- 标题层级要**真实反映内容层级**：不要跳级，不要为样式用 h1 装 h3。
- 段落别太长，一段一个观点。长内容拆成带小标题的子节，方便扫读。
- **链接默认带下划线**（WCAG 1.4.1 禁止仅靠颜色区分链接，NN/g 实测也如此）：正文里的
  链接一律有下划线；目录/跳转按钮/卡片/上标引用内的链接已由骨架去下划线——写正文时不用管。
- **中文强调用着重号 `.em`**（`text-emphasis: dot`，W3C CLREQ §5.3.1 规范），
  不要用粗体/斜体去给中文字"加粗当强调"：`这是<span class="em">重点</span>内容`。
  西文和代码里仍正常用 `<strong>`。

---

## 3. 页面骨架结构

按这个顺序组织（skeleton 已搭好，可微调）：

```
<button class="theme-toggle">  🌓 深浅色切换按钮（skeleton 内置，无需手写）
<header class="hero">      页面头部：主标题、一句话副标题、元信息（📅日期/🕐时长/难度徽标）
<div class="layout">
  <nav id="toc">           侧边目录（悬浮）。由 JS 从 <main> 的 h2/h3 自动生成
                           ——h2/h3 缺 id 也会自动补，无需手写；小屏折叠成标签条
  <main>
    <section> 章节（每个以 <h2> 开头）
      <h3>/<h4> 小节
    </section>
    ...
    <section id="sources"> 参考来源列表（Step 3 收集的链接）
  </main>
</div>
<footer>                   版权/生成说明/许可
```

> ⚠️ **标题 id 与目录**：骨架的 JS 会自动给缺失 id 的 h2/h3 补 id 并生成两级目录。
> 你**不需要**手写目录，但**正文里的 h2/h3 要保持真实层级**（别跳级），
> 这样自动目录才是对的。需要锚点跳转时，引用该标题的 id 即可。
>
> **目录层级与当前位置**：骨架 CSS 已让一级（h2）更深更粗、二级（.lvl2）缩进更浅更小，
> 当前所在章节有主色左侧强调条——读者一眼看出"我读到哪了"。
> 写标题时**别给正文手动加序号却又漏掉一部分**，目录文字来自标题，会原样出现编号断层。

**页面头部（hero）**是读者对这份文档的第一印象：
- 主标题：内容主题，一句话说清「这份文档教你/讲什么」
- 副标题：1 句话说明适用对象与前提（如「适合：接触过 Python 基础语法的读者」）
- 元信息行：日期、难度徽标、类别 `badge`、技术 `chips`。**阅读时长不用手写**——
  hero 里的 `<span id="readTime">` 由 JS 按正文长度自动估算（约 350 字/分）
- 前置要求 / 适用对象：适合进 hero 时用 chips，也可以放正文首个「开始之前」callout
- 背景可用主色的径向渐变 + 微弱网格，保持克制

---

## 4. 组件库

所有组件的类名与骨架 CSS 一一对应。**选择组件的依据是内容，不是样式花哨程度。**

### 4.1 Callout 提示块

一句话要点、警示、技巧。用于「强调」，不用于「装正文」。

```html
<div class="callout tip">
  <div class="callout-head"><span class="icon">…</span><strong>建议</strong></div>
  <p>具体内容。</p>
</div>
```
- 类名取语义：`info` / `tip` / `warning` / `danger`，对应语义色与浅底
- 标题用词可随语言变化（建议 / 注意 / 警告 / 说明），但类别别乱用
- 一个页面的 callout 别超过 5~6 个，多了就失去强调作用

### 4.2 步骤卡片（procedure 类型核心）

```html
<ol class="steps">
  <li class="step">
    <div class="step-head"><span class="step-num">1</span><h3>步骤标题</h3></div>
    <p>说明。</p>
    <pre><code>命令或代码</code></pre>
    <div class="step-result">做完这步应该看到什么（预期结果，与步骤同框）</div>
  </li>
</ol>
```
- **序号由 CSS 自动递增**——必须用 `.steps > .step` 结构才会显示圆圈序号，别用普通 `<ol>`
- 步骤标题用 h3，正文用 p；代码块紧跟说明
- **每步都要有 `.step-result`（预期结果）**：告诉读者做完这步该看到什么，他才不会走偏。
  预期结果与步骤在同一个框里（评测反馈特别点名要求）

### 4.3 代码块（自动语法高亮）

```html
<pre><code class="lang-bash">git init</code></pre>
```
- **语法高亮自动生效**：骨架 JS 会按 `lang-*` 识别语言并给代码上色
  （Python / Bash / JS / TS / JSON / YAML / SQL / HTML / CSS）。**语言标签必须写对**，
  写错语言高亮就是错的。给代码块的内容保持缩进整洁，高亮才好看
- **复制按钮 + 右上角语言标签由骨架自动加，无需手写**。复制内容自动**剔除 bash 的
  `$`/`>` 提示符**（装饰性内容不进剪贴板，Prism command-line 的标准做法），并带
  `aria-live` 播报「已复制」（对屏幕阅读器可见）
- 需要**行号**时给 `<pre>` 加 `class="linenos"`；默认不加行号（与顶级文档站一致，
  行号只在需要逐行引用时开，见 4.27）
- 代码块背景统一深色（`--code-bg`），保证浅/深主题下都清晰
- **行内代码 `<code>` 强调**：命令名、变量名、文件名、API 名等出现在正文里的
  代码词，用 `<code>` 包裹，骨架已给主色+粗体（比普通文字醒目，评测反馈要求）

### 4.4 表格

```html
<div class="table-wrap">
  <table>
    <thead><tr><th>列</th><th>列</th></tr></thead>
    <tbody>…</tbody>
  </table>
</div>
```
- 数据对比、配置项、速查用表格最合适 —— 别用卡片硬撑，也别把表格塞进卡片
- `table-wrap` 提供横向滚动，小屏不破版（**兜底**，不是默认依赖）
- 表头用 `--text-2` 加粗，行条纹用 `--bg-soft`
- **表格默认不做横向滚动，读者要一眼看全**（评测反馈：横向拖动很烦）：
  - 列太多（约 >6 列）时优先**精简/合并列**——去掉冗余列、缩写表头、把厂商/版本合并进模型名；或拆成两张小表（参数表 + 亮点表）。横向滚动只留给真正不可删的多列逐项对比
  - **竖向太长（约 >12 行）→ 折叠**，用 `details.fold` 包起来，summary 写清「N 个模型对比」，默认收起、点开看全（打印时骨架自动展开）：
    ```html
    <details class="fold">
      <summary>完整对比表（11 个模型）<span class="badge info">展开</span></summary>
      <div class="fold-body">
        <div class="table-wrap"><table>…</table></div>
      </div>
    </details>
    ```

### 4.5 卡片网格

```html
<div class="cards">
  <article class="card"><h3>标题</h3><p>…</p></article>
  …
</div>
```
- 用于「并列的同构条目」：术语表、方案对比、推荐项、人物/工具简介
- 卡片内部结构一致（都有标题 + 描述），不要一张卡塞三个字段另一张塞五个
- 有主次之分时，用「推荐」角标（`.card .badge`）标出来，别靠底色硬撑

### 4.6 徽标 / 关键词标签（统一两套标签，别混）

**所有页面统一**这两种标签（评测反馈点名）：
- **椭圆/胶囊标签 `.badge` = 文章类别**：教程 / 指南 / 速查 / 讲解 / 选型。
  放 hero 元信息里，一眼告知读者"这是什么类型"。`border-radius:999px`。
- **方形圆角标签 `.chip` = 涉及的技术/关键词**：Python、Scrapy、Docker……
  放正文技术清单（`.chips` 组）、hero 元信息、卡片内。`border-radius:6px`。

```html
<!-- hero 元信息：类别用 .badge（椭圆），技术用 .chip（方形圆角） -->
<span class="badge">教程</span>
<span class="chip t1">Python</span><span class="chip t2">Scrapy</span>
```
- 别拿 `.badge` 装技术、也别拿 `.chip` 装类别——两种形状本身就是语义。
- 颜色用语义色轮换（chip t1/t2/t3、badge info/tip/...），避免清一色。

其余难度/状态徽标（入门/进阶）用 `.badge` 即可。

### 4.7 Tab 切换

```html
<div class="tabs">
  <div class="tab-bar" role="tablist">
    <button class="tab active" role="tab">Windows</button>
    <button class="tab" role="tab">macOS</button>
  </div>
  <div class="tab-panel active" role="tabpanel">…</div>
  <div class="tab-panel" role="tabpanel">…</div>
</div>
```
- 用于「同一内容的平台/版本变体」，如多系统安装、多语言示例
- skeleton.js 已实现切换逻辑；`active` 类控制显隐

### 4.8 决策表 / 对比（decision 类型核心）

用「维度 × 选项」的表格 + 每列一个结论，或卡片网格 + 每条一个「适合谁」。
选型建议必须在结尾给出**明确的推荐**，不能让读者读完还在纠结。

### 4.9 检查清单 / 自测（教程/讲解收尾用）

```html
<ul class="checklist">
  <li><label><input type="checkbox"> 我已理解 X</label></li>
</ul>
```
- 教程末尾放「完成标准」：做完这份指南你应该能 …
- 讲解末尾可放 3~5 道「自测」或「关键点回顾」，让读者确认掌握

### 4.10 参考来源（可点击跳转）

```html
<ol id="sources" class="sources">
  <li id="src-1"><a href="…">标题</a> — 来源站点</li>
</ol>
```
- 每个来源项给 `id="src-N"`；正文引用写成可点击跳转的上标：
  ```html
  正文引用<sup><a href="#src-1">[1]</a></sup>。
  ```
  点击 `[1]` 直接跳到来源项（评测反馈特别点赞这个设计）
- Step 3 收集的每个来源一行；无外部来源（纯个人经验类内容）时可省略

### 4.11 主题切换

骨架内置 `🌓` 悬浮按钮：浅色 / 深色 / 跟随系统三档循环，记忆用户选择。
**无需手写**，只要不删掉骨架里的 `.theme-toggle` 按钮即可。

- 切换时页面颜色带约 0.3s 过渡（`.theme-switching` 类仅在切换瞬间开启，夜间切浅色
  不会"啪"地闪白）；**初始加载不播过渡**，避免开页闪变
- 尊重 `prefers-reduced-motion`（WCAG 2.3.3）：系统关闭「动画效果」时过渡自动禁用，
  主题仍即时切换——这是**预期行为**，不是 bug。要预览过渡时，在 Chrome DevTools 的
  Rendering 面板把 `prefers-reduced-motion` 模拟成 `no-preference` 再刷新
- 代码块背景（深浅一致）与 hero 的渐变底会平滑过渡主色，渐变层的细微跳变可忽略

### 4.12 速查表过滤（reference / 速查表类型）

```html
<div class="sticky-toolbar">
  <input class="search-box" data-filter-target=".card" placeholder="搜索命令…">
</div>
<div class="cards">
  <div class="card">…</div>
</div>
```
- 输入即过滤 `data-filter-target` 指定的元素（`.card` / `tr` / `.cmd-row`）
- **搜索框放进 `.sticky-toolbar` 实现吸顶**：速查表的搜索栏固定在最上方，不随页面滚走
  （评测反馈点名：搜索栏直接放最顶上、固定位置）
- 速查表 / 长清单类型**必须提供**搜索框

### 4.13 关键词标签组（chips）

```html
<div class="chips">
  <span class="chip t1">Python</span>
  <span class="chip t2">Scrapy</span>
  <span class="chip t3">爬虫</span>
</div>
```
- 文中涉及的技术关键词、工具、概念，用 chips 分组呈现，颜色交替（t1/t2/t3）
  避免清一色（评测反馈：技术关键词要有标签）

### 4.14 表格语义标签

```html
<td><span class="tag-ok">支持</span></td>
<td><span class="tag-no">不支持</span></td>
```
- 对比表中"支持/不支持/推荐"用红绿标签（`tag-ok` / `tag-no`），一眼可辨
  （评测反馈点赞"红底不支持、绿底支持"设计）

### 4.15 决策小测（decision 类型）

骨架内置一个**可用**的决策小测组件：用户选完所有题目点"看结果"，自动算出结论。

```html
<div class="quiz" data-a="Node" data-b="Deno">
  <div class="quiz-q"><p class="quiz-q-text">生态成熟度谁更强？</p>
    <label><input type="radio" name="q1" value="a"> Node 生态更成熟</label>
    <label><input type="radio" name="q1" value="b"> Deno 一体化更强</label>
  </div>
  <button class="quiz-btn" type="button">看结果</button>
  <div class="quiz-result"></div>
</div>
```
- `data-a` / `data-b` 填两个方案的名称，结果会自动显示"推荐 X（X n% / Y m%）"
- **必须能跑通**：题目都要可勾选、点"看结果"必须给结论（评测反馈：选完自动弹结论，
  而不是让用户自己对照）。别手写复杂交互，用这个组件
- 只做单选判断题，3~6 题足够；每题两个选项分别对应方案 A/B

### 4.16 快速跳转按钮（decision 类型 hero）

```html
<div class="jumps">
  <a class="jump" href="#conclusion">直接看结论 →</a>
  <a class="jump ghost" href="#compare">综合对比表</a>
  <a class="jump ghost" href="#quiz">决策小测</a>
</div>
```
- 为"只要答案"的读者提供直达；**所有跳转按钮样式一致**（主跳转实心，次要的 ghost）

### 4.17 打印按钮

骨架内置右上角 🖨️ 按钮（调用 `window.print()`），配合 `@media print` 导出 PDF。
**不要删**——打印/导出是用户明确要的能力。

### 4.18 编号一致性

章节编号要么**全部有**（正文标题文字自带 `4.1` 这类编号）、要么**全部没有**。
目录由标题文字自动生成，正文和目录会完全一致——所以不一致一定是标题文字本身不一致。
正文里给 h3 加序号、却不给 h2 加，就会形成"4.1 有、5 下的小标题没有"的断层，
这是评测反馈反复点名的问题。写标题时统一规则：h2 编号则 h3 必须跟着编号，反之亦然。

### 4.19 Emoji 的用法（用对是点睛，用多是噪音）

评测反馈：页面"不生动"、想让人一眼看出是技术/教程站。适度的 emoji 有用，规则：
- **分类/标签/列表加 emoji**：类别标题如 `📁 文件` `⚙️ 进程` `🌐 网络` `💾 磁盘` `🔒 权限`；
  命令行示例可在行首放 `$` 表示终端提示符
- **元信息**：📅 日期、🕐 阅读时长
- **callout 标题**：建议/注意/警告前可加对应 emoji，但别每个都加
- **正文不要滥用**：连续多个 emoji 或表情当字用是噪音。一个图标 = 一个信息点
- **标题 emoji + 渐变**：`h1.grad`（渐变文字）用了 `background-clip:text; color:transparent`，
  emoji 放里面可能被裁剪/不显示——要加 emoji（如 🖥️ Linux 速查表）就别同时用 `grad`，
  或把 emoji 放渐变标题外的独立元素里

### 4.20 流程图可读性（硬要求）

评测反馈：流程图"字重叠""字太小"是常见扣分点。画 inline SVG 或 CSS 流程时：
- **字号**：流程图内文字 ≥ 12px（正文默认 16px，别小于正文的 3/4）
- **留白**：节点内 padding、节点间距都要留够，文字不与边框/箭头重叠；画完想象实际像素宽度
- **可缩放**：`viewBox` 设好，宽度 100%，避免小屏裁切
- **图例/箭头不挡字**：箭头、标注线经过文字处要让开
- **多节点流程/里程碑条**：节点数多时**绝不要**用"绝对定位圆点悬在线 + `overflow-x:auto` 被 `overflow:visible` 覆盖"这种写法——实测 7 节点会超出容器约 380px 且无法滚动，流程图直接碎掉（教训来源：迭代 4 前端路线图）。正确做法二选一：
  - **网格卡片**（推荐，不溢出、自动换行）：
    ```html
    <div class="rm-grid">
      <div class="rm-card"><span class="rm-num">1</span><div class="rm-name">阶段名</div><div class="rm-sub">要点</div></div>
      …
    </div>
    ```
    ```css
    .rm-grid{display:grid; grid-template-columns:repeat(auto-fit,minmax(10rem,1fr)); gap:.6rem; margin:1.6em 0}
    .rm-card{border:1px solid var(--border); border-radius:var(--radius); padding:.7rem .9rem; background:var(--surface)}
    .rm-num{display:inline-flex; width:1.7rem; height:1.7rem; align-items:center; justify-content:center;
      border-radius:50%; background:var(--accent); color:#fff; font-weight:700; font-size:.85rem; margin-bottom:.35rem}
    ```
  - 若坚持横向条：用 `overflow-x:auto` **且**把圆点放进容器内（不靠负 top 伸出容器外），
    并给小屏一个可横向滚动的提示；**任何情况下不得再用 `overflow:visible` 覆盖滚动**。

### 4.21 回到顶部

骨架内置右下角 ↑ 按钮，滚动超过一屏自动出现。**不要删**——评测反馈几乎每页都要求。

### 4.22 终端徽标（命令行/终端内容用，代替 emoji）

涉及命令行、终端、命令速查的页面，标题里放一个圆角方框 `>_` 代表终端（比 emoji
更贴合、更像终端提示符）：

```html
<h1><span class="term-badge" aria-hidden="true">&gt;_</span>Linux 常用命令速查表</h1>
```
- 深色底 + 等宽 `>_` + 一个闪烁光标（`▍`），骨架内置 `.term-badge`
- 只用于标题/入口强调处，正文不要重复

---

### 4.23 渐进披露折叠（可选步骤 / 进阶内容）

「核心路径优先，可选材料折叠」是文档研究的渐进披露原则（NN/g）。教程里的**可选步骤、
进阶内容、展开讲原理**放进折叠，主线保持干净：

```html
<details class="fold">
  <summary>还想知道为什么吗？<span class="badge info">进阶</span></summary>
  <div class="fold-body">
    <p>深讲的内容，主路径读者可跳过。</p>
  </div>
</details>
```
- 用**原生 `<details>/<summary>`**：零 JS、键盘（Enter/Space）天然可用、无障碍支持好
- `summary` 里可放「可选」/「进阶」badge 提示读者可跳过
- 打印/导出 PDF 时骨架会强制展开所有折叠，内容不会被漏掉
- 折叠用于"补充"，不要用折叠藏住主线步骤——主线必须直接可见

### 4.24 页内快速跳转（Ctrl+K / Cmd+K，自动）

骨架自动内置：按 `Ctrl+K`（Mac 为 `Cmd+K`）弹出章节搜索框，输入即过滤标题，
↑↓ 选择、Enter 跳转、Esc 关闭，焦点自动回收。**无需手写任何标记**。

- 长页面（explainer / reference / 速查）建议在正文开头用一句 callout 提一句「按
  Ctrl+K 快速跳转章节」——多数读者不知道有这个能力
- 打印时弹层自动隐藏

### 4.25 阅读进度条（自动）

骨架自动内置：页面顶部一条主色进度条，随滚动增长。**无需手写**。
装饰性元素（`aria-hidden`），不干扰正文；尊重 `prefers-reduced-motion`。

### 4.26 标题锚点链接（hover ¶，自动）

骨架自动给所有 `h2/h3` 加悬停显示的 `¶` 链接，点击复制/直达该标题。**无需手写**。
方便读者深链到具体小节；键盘 Tab 到标题也能聚焦到 ¶。

> 同页锚点（目录、`¶`、上标引用、hero 跳转按钮等 `href="#…"`）的点击由骨架统一拦截、
> 改用 JS 滚动——因为 `file://` 页面里真实锚点导航会被 Chrome 报
> "Unsafe attempt to load URL" 的 console 错误，部分版本还滚动失效。此逻辑已内置，别删。

### 4.27 代码行号（可选，`<pre class="linenos">`）

默认**不加**行号（与顶级文档站一致）。当内容需要"逐行引用"（如讲某行代码的意思、
代码讲解要按行号定位）时，给 `<pre>` 加类：

```html
<pre class="linenos"><code class="lang-python">print("hi")</code></pre>
```
- 行号 gutter 对屏幕阅读器隐藏（`aria-hidden`）、复制时自动不含行号
- gutter 与代码行高严格对齐，长行横向滚动不破坏对齐

### 4.28 中文着重号 `.em`

中文字强调用着重号而不是加粗（W3C CLREQ §5.3.1）：

```html
这是<span class="em">重点</span>内容。
```
- 文字下方渲染强调点；西文/代码仍用 `<strong>`
- 用途克制：一段里别满屏着重号，一个观点一个

### 4.29 得分柱状图（横向条，纯 CSS）

对比 / 横评页**有真实得分**时，用横向柱状图一眼呈现「谁高谁低」，比表格更直观。
纯 CSS、无 JS、无外部库，深浅色与打印都适配：

```html
<div class="barchart">
  <div class="bc-row"><span class="bc-label"><b>Claude Opus 5</b></span><span class="bc-track"><span class="bc-fill" style="--v:61%"></span></span><span class="bc-val">61</span></div>
  <div class="bc-row"><span class="bc-label"><b>GPT-5.6 Sol</b></span><span class="bc-track"><span class="bc-fill" style="--v:59%"></span></span><span class="bc-val">59</span></div>
</div>
```
- `--v` = 填充宽度百分比（0–100），作者按需计算；非 0–100 的指标（如 Elo ~1600）先按量表换算再填
- 行内 `<b>` 包名称可加粗；轨道浅底、填充主色渐变，同一组图用同一量表
- 图上方/下方配一句说明：指标名 + 量表 + 「越高越好/越低越好」（如「AA 智能指数 v4.1，越高越好」）
- 有得分数据时**图表 + 明细表一起给**：柱状图负责直观，明细表（真实数字 + 缺项 `—` + 厂商自报标注）负责完整可查

---

## 5. 图标

用**内联 SVG**（骨架已内置若干常用：搜索、复制、检查、警告、箭头等；写正文时按需新增
简单 stroke 图标）。规则：

- 统一 `viewBox="0 0 24 24"`、`fill="none"`、`stroke="currentColor"`、`stroke-width="1.8"`
- 尺寸跟随文字（`width: 1em; height: 1em`）
- 图标是**辅助**，去掉图标页面依然要成立。不要用图标替代文字标签

---

## 6. 暗色模式与打印

- 深色由 `prefers-color-scheme` 自动切换，**不需要切换按钮**（尊重系统设置）
- 打印样式（skeleton 已内置）：隐藏侧边目录与交互控件、正文展开、去除背景与阴影、
  保留链接文字、页边距合理。目标：打印/存 PDF 后是一份干净整洁的文档
- 测试时务必两个模式都看一眼，尤其是 callout 与代码块

---

## 7. 可访问性底线

- 语义化标签：`nav` / `main` / `section` / `article` / `footer`，标题层级真实
- 所有图片/图标有 `aria-hidden` 或替代文本；表单控件有 `label`
- 键盘可达：Tab 切换、目录链接、复制按钮都要能 Tab 到并触发；页面第一个可聚焦元素是
  `.skip-link`（跳到正文）；当前章节在目录里带 `aria-current="true"`
- `:focus-visible` 焦点环（键盘用户可见、鼠标点击不显示）+ `prefers-reduced-motion`
  减弱动效（骨架内置，别删）
- 正文链接有下划线（不只靠颜色）；对比度达标（见 §1）
