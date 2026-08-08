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
- **AI slop 四特征自查**：过度居中布局、刺眼的紫色渐变、清一色统一圆角、Inter 字体
  （Anthropic Artifacts Builder 点名的四样 AI 味特征）。写完后通读自查是否踩中——
  尤其 hero 的渐变底与字体栈，别让页面一眼像 AI 生成。
- **生动判据（一句话）**：加任何组件/视觉元素前问「**读者跳过它会损失信息或定位吗？**
  损失 → 留；只好看 → 删」（NN/g 扫读研究 + AI slop 定义的落点）。组件是审校过的决定，
  不是默认堆砌。已点名的 AI 签名：**「圆角卡片 + 一侧厚色条」**（noqta.tn 称其为 AI 生成
  UI 的头号签名）、统一超大圆角、紫→蓝渐变、过量字距——摘要卡等新设计要避开。

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

### 2.1 编辑排版（生动但不俗，零外部字体）

**字体角色固定、对比出层次**（Butterick mixing-fonts / Practical Typography 核实）：
- **标题用中文衬线** `--serif`（`"Songti SC","STSong",SimSun,"Noto Serif CJK SC",Georgia,serif`），
  **正文保持黑体无衬线**——宋体大标题 + 黑体正文 = 编辑/杂志风，一眼不像 AI 模板。骨架已内置
  `h1` 用 `var(--serif)`；`h2/h3` 仍黑体，靠字号分层。**一文档最多两款字体、每款固定角色**，
  别混着用。
- **模块化字号**（ALA 模块化比例）：正文 16px 为基数 → 大标题 2.5–3×（骨架 `h1` 最大 2.8rem）、
  小标题 1.5×（`h2` 1.5rem）、图注/说明 0.85×。`h1` 在 hero 用 clamp 适配。
- **中文行宽 30–40 字/行**（容器 `max-width:46rem` ≈ 上限内）；行高 1.7。
- **留白优先于线条区隔**：标题上方留白 ≥1.5×标题字号；分隔只允许细线，别堆装饰条。
- **一屏 ≤2 个「大声」元素**（大标题 / 大数字 / 拉引 / drop cap），其余安静——视觉锚点多了
  等于没有锚点。
- 强调色保持**仅 1 个**（链接/锚点/大数字），正文近黑灰；深色主题靠 CSS 变量切换，
  打印强制浅色 + 正文纯黑。
- 中文陷阱：屏幕正文别用宋体（SimSun 小字发虚）——宋体只用于大字号标题/拉引/数字。

### 2.2 风格主题（一个骨架，多套观感）

默认 `modern`（不写 `data-style`）。在 `<html>` 上写 `data-style="..."` 切换整页观感；
因为主题是纯 CSS 块，读者用主题切换按钮就能实时看不同风格（同一份文件 = 多套观感）。

| 风格 | `data-style` | 视觉签名 | 适合内容 |
|---|---|---|---|
| 现代（默认） | 不写 | 黑体正文 + 宋体大标题、indigo、卡片组件 | 默认 / 教程 / 速查 |
| 报纸 | `newspaper` | 墨黑白高对比、衬线密排、红仅做点缀、无圆角/阴影、实线规则 | 新闻综述、大事记、时间线型 |
| 杂志 | `magazine` | 暖奶油纸底、**森林绿**强调、kicker + display 衬线大标题、衬线正文、大留白 | 观点长文、深度讲解 |
| 极简 | `minimal` | 薄线、巨留白、近无色、细无衬线、无圆角 | 数据横评、速查（Tufte data-ink） |
| 学术 | `academic` | modern + serif 正文 + 编号标题 + 摘要/参考文献 | 论文 / 规范整理 |
| 粗野 | `brutal` | 粗黑边、硬偏移阴影、高饱和色块、Arial Black 标题 | 声明式 / 海报式 / 大胆主题 |
| 终端 | `terminal` | 深底等宽字体、绿色/青色、box 线框、`$` 提示符 | 命令行 / 开发者教程 |
| 深色科技 | `tech` | 近黑底、单一高饱和 accent、细字重、微发光 | 产品 / API 说明、技术白皮书 |
| 瑞士国际 | `swiss` | 白底无衬线、**瑞士红**（#e30613）、发丝线网格、非对称排版、排版即主视觉（Müller-Brockmann 血统） | 结构化说明、数据面、横评报告 |
| 书卷 | `book` | 暖纸底、宋体正文、两端对齐、**段首缩进两字**、双线/单线克制分隔（Tschichold 版心比例） | 长文讲解、深度阅读、经典书排 |

- 骨架已内置各主题**浅色 + 深色**（深色=纸墨反转）；`--serif` / `--sans` 是字体令牌，主题整体替换
- 结构钩子：`.kicker`（眉题）各主题可用；报纸/杂志建议 hero 标题上方放 kicker + byline 作者行
- **改主题只动 `<html data-style="...">`，正文与组件不变**——生成时先写正文、最后定风格
- 换肤是**软默认**非硬规则：数据页做报纸风会伤可信度，尊重内容体裁（Tufte / Sullivan：
  form follows function）

### 2.3 专业排版原则（跨主题通用）

以下规则来自可查证的职业排版实践（血统在括号里），**所有主题共用**；
它们解释了很多"为什么这么排"，也是自检时的依据。

**正文的四个基本量**（Butterick《Practical Typography》）：
- **字号**：网页 15–25px。骨架正文 16px 在此区间。
- **行高**：正文行高的 120–145%；西文 1.3 即可，**CJK 需更宽**——骨架正文 1.7，
  `book` 主题用到 1.9。别用默认 1.2（太挤）。
- **行长**：每行 45–90 字符（西文）或 **30–40 字**（中文；骨架 `main max-width:46rem` 已约束）。
- **字体**：正文一种、标题一种（见 §2.1），**别默认 Arial / Times 凑合**——职业排版语境里
  它们常是"没设计过"的代名词（Butterick 原话，作为警告而非禁令）。

**段落缩进 vs 段间距：二选一**（Butterick）。用段首缩进（1–4×字号）就不要再加段间距，反之亦然。
骨架默认**段间距**（网页惯例）；`book` / `newspaper` 等书卷感主题用**段首缩进两字**（中文惯例）。

**孤行寡行控制**（widow / orphan）：标题要与紧随的段落同屏/同页；段尾别留单行孤字。
A4 分页与打印时核对——这与"表格整块不切"同一精神，是既有流程的隐性约束。

**两端对齐必配处理**：西文两端对齐要开连字符（hyphenation）；中文两端对齐要用
`text-justify:inter-ideograph`（`book` 主题已内置），否则字距被拉得参差。

**全大写需加字距**：英文全大写一行以内可接受，但须加 5–12% `letter-spacing` 才不闷
（骨架 `.kicker` / `.badge` 已按此处理）。

**图表 data-ink 原则**（Tufte《The Visual Display of Quantitative Information》）：
图/表里每一滴墨都要传递信息。3D 柱、渐变网格、背景装饰、内容无关的图标 = **chartjunk**，删。
骨架 `.barchart` / `.donut` 是干净的 data-ink 实现——别在上面加投影、立体感、多余网格线。

**排版是透明的容器**（Beatrice Warde《The Crystal Goblet》）：
好的排版像水晶杯——读者看到的是酒（内容）而不是杯子。装饰必须有语义目的；
这正是 §1.5 反 AI 味的内在理由：风格服务于内容，不是内容服务于风格。

**每个选择都可辩护**（Vignelli Canon）：字体、颜色、间距、圆角……每个决定要答得上"为什么"。
读者质问时答不出，就是纯装饰。这条也约束"为了好看而堆组件"。

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
- 元信息行：作者（`<span class="author">` 含 GitHub 图标，值读 `user-config.md` 的 `author`）、
  日期、难度徽标、类别 `badge`、技术 `chips`。**阅读时长不用手写**——
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
- 三个图标含义：☀️ 浅色、🌙 深色、🌓 跟随系统（默认）。**悬浮按钮下方会浮现简短说明**
  ——「跟随系统 · 点击切浅色」等（`.btn-tip` tooltip 读 `data-tip`，JS 切换时同步文案与
  `aria-label`）；键盘 Tab 聚焦同样显示，touch 设备不触发 hover（图标本身可点击循环）。加提示的
  判定规则见 §4.31
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

### 4.30 饼图 / 环形图（纯 CSS conic-gradient）

**占比 / 构成**数据（厂商份额、难度分布、测试集占比）用环形图呈现"部分占整体"，比柱状图更贴切。纯 CSS（`conic-gradient`）、无 JS、无外部库，深浅色与打印都适配。

**单指标环**（一个值占整体的百分比，如通过率 73%）：

```html
<div class="donut-chart">
  <div class="donut" style="--v:73">
    <span class="donut-center"><b>73%</b><span>通过率</span></span>
  </div>
  <p>旁注：指标名 + 口径。</p>
</div>
```

- `--v` = 完成百分比（0–100）；`--dc` 可覆盖填充色（默认主色）
- 中心 `.donut-center` 放数值（`<b>`）+ 单位/标签（`<span>`）

**多段环**（若干占比，加总 ≈ 100）+ **图例**：

```html
<div class="donut-chart">
  <div class="donut pie" style="--a1:40; --a2:35; --a3:25">
    <span class="donut-center"><b>100</b><span>模型数</span></span>
  </div>
  <div class="donut-legend">
    <div class="dl-row"><span class="dl-dot" style="background:var(--accent)"></span><span class="dl-name">Claude 系</span><span class="dl-val">40%</span></div>
    <div class="dl-row"><span class="dl-dot" style="background:var(--accent-2)"></span><span class="dl-name">OpenAI 系</span><span class="dl-val">35%</span></div>
    <div class="dl-row"><span class="dl-dot" style="background:#d97706"></span><span class="dl-name">其他</span><span class="dl-val">25%</span></div>
  </div>
</div>
```

- `--a1`..`--a5` = 各段占比（缺省 0，加总 ≈ 100）；`--c1`..`--c5` 可覆盖各段颜色（默认依次为主色 / 次强调 / amber / sky / violet 语义色）
- 图例 `.dl-row` 的色点背景与对应段颜色保持一致；数值用 `.dl-val`
- 环固定 7.5rem；图例在右侧并排、小屏自动换行
- 图上方/下方配一句说明：指标名 + 口径；分布数据同样可用明细表兜底

**打印**：conic-gradient 属于背景，默认不打印——骨架已对 `.donut` 加 `print-color-adjust:exact`，段与轨道都会保留。

选择：环形图服务于**占比/构成**，柱状图（§4.29）服务于**高低排序**——按数据关系选，别混用；占比相加要对得上 100%（或明确标注其余为「其他」）。

### 4.31 图标按钮悬浮说明（.btn-tip）

**规则：只给含义不直观的图标按钮加说明，意义自明的图标不加；文字尽可能简短。**
- **加**：主题切换（🌓/☀️/🌙 三图标含义不直观）、打印（🖨️）
- **不加**：搜索 🔍、复制 📋、回到顶部 ↑（意义自明；回顶按钮明确排除）

```html
<button class="print-btn btn-tip" data-tip="打印 / 导出 PDF">🖨️</button>
```

- `.btn-tip::after` 读 `data-tip`，悬停 / 键盘聚焦时在按钮下方浮现；主题按钮文案由
  JS 切换时同步（§4.11）
- 使用按钮自身需是**定位元素**（fixed/relative），tooltip 才挂在它下方
- 已处理：右对齐按钮右缘防出屏、`width:max-content` 保证单行（不被按钮宽度压成竖排）、
  `max-width` 兜底超长折行
- **不要给图标按钮写 `title` 属性**——CSS tooltip 取代它，避免悬停时双提示

### 4.32 流程图（纯 CSS，`.flow` / `.fc-node`）

线性流程或**带「是/否」判断分支**的流程。**什么时候用**：内容有明确先后顺序 + 判断分叉
（安装分支、决策路径、机制因果链）。纯线性无分支的步骤 → 用编号列表或 `.steps`，别画图。

```html
<div class="flow">
  <div class="fc-node start"><span class="fc-tag">开始</span>Luna 降价 80%</div>
  <div class="fc-arrow"></div>
  <div class="fc-node decide"><span class="fc-tag">判断</span>订阅额度变了吗？</div>
  <div class="fc-branch">
    <div class="fc-col">
      <span class="fc-col-label"><b>否</b> → 额度不动</span>
      <div class="fc-node">号池成本锚定旧流量</div>
      <div class="fc-arrow"></div>
      <div class="fc-node">卖得越多亏得越狠</div>
    </div>
    <div class="fc-col">
      <span class="fc-col-label"><b>是</b> → 跟进降价</span>
      <div class="fc-node">正常跟进低价</div>
    </div>
  </div>
  <div class="fc-arrow"></div>
  <div class="fc-node end"><span class="fc-tag">结果</span>下架 / 禁 / 映射</div>
</div>
```

- 节点 `.fc-node`，状态类三档：`start`（起，主色浅底）/ `decide`（判断，琥珀色）/
  `end`（终，绿色）；`.fc-tag` 放节点顶部的类型小字
- 箭头用空的 `.fc-arrow` div（两节点之间各放一个）；判断后接 `.fc-branch` 双列分支，
  每列 `.fc-col` 内可继续串节点与箭头；小屏自动变单列
- 节点文字 ≥ 正文 3/4（12px+）、内边距留够，箭头不与文字重叠（教训 §4.20）
- 打印友好：连线用 `border`（可打印），节点底色已加 `print-color-adjust:exact`
- 多节点的纯线性流程用 §4.20 的 `rm-grid` 卡片网格更省空间；有分支才用 flowchart

### 4.33 时间线（纯 CSS，`.timeline`）

事件按时间先后展开（版本历史、里程碑、产品沿革）。**什么时候用**：读者需要按时间顺序
理解「谁先谁后」。非时间顺序的内容别硬套。

```html
<ol class="timeline">
  <li>
    <time>2026-07-30</time>
    <h3>OpenAI 下调 Luna API 单价 80%</h3>
    <p>订阅价与 quota 不动。</p>
  </li>
  <li>
    <time>2026-08</time>
    <h3>中转站集体下架 Luna</h3>
    <p>按新价卖、按旧流量成本付，亏本。</p>
  </li>
</ol>
```

- 左侧竖线 + 圆点，末节点圆点用次强调色 = 最新/当前
- 时间用 `<time>`（语义标签）；标题 h3、正文 p、额外信息 `.tl-meta`
- 时间先后排列用 timeline；**任务并行/有依赖/工期**（排期）→ 甘特图，组件库没有，
  复杂场景用 mermaid 预渲染 SVG（见附录）

### 4.34 字符画 / ASCII 点缀（克制使用）

零依赖的趣味点缀，但**只在等宽环境可用**：
- 只能放 `<pre>`（等宽字体）里——正文比例字体会破坏对齐，中文全角/半角混排更碎
- 适合终端 / 复古 / DIY 主题；装饰性分隔（`──── ● ────`）可少量点缀正文外
- **佐料不是主菜**：整页字符画 = 炫技，违背 §1.5 反 AI 味；信息表达主力用 §4.32/§4.33 真实图示
- 纯装饰字符画加 `aria-hidden="true"`；有含义的 `<pre role="img">` + 文字说明

### 4.35 编辑向点缀（dropcap / pullquote / stat / takeaway / tldr / mythfact）

**生动 ≠ 装饰**——这些都是「扫读锚点」（NN/g：79% 用户只扫读），每加一个先过 §1.5 的
生动判据。字号/字重/衬线是首要对比手段，别靠颜色堆。

**首字下沉**（`.dropcap`，全文 ≤1 处，给正文首段）：
```html
<p class="dropcap">正文首段，第一个字会放大成宋体下沉，做视觉锚点。</p>
```
**拉引**（`<blockquote class="pullquote">`，一屏 ≤1 处，提取值得引的关键句）：
```html
<blockquote class="pullquote">降的是 API 单价，不是订阅额度<cite>——本页结论</cite></blockquote>
```
**数字/统计高亮**（`.stat` 大数字，须可溯源 + 标注口径）：
```html
<div class="stats">
  <div class="stat"><b>−80%</b><span class="stat-cap">Luna API 单价降幅</span></div>
  <div class="stat"><b>0</b><span class="stat-cap">订阅价变化</span></div>
</div>
```
**本节要点**（`.takeaway`，长节 >3 屏时收束 1–3 条，只写正文**没有**的新话）：
```html
<div class="takeaway">
  <div class="tk-head">本节要点</div>
  <ul><li>降的是 API 单价，不是订阅额度。</li><li>号池成本锚在 quota。</li></ul>
</div>
```
**TL;DR**（`.tldr`，长文页首结论先行，≤3 条，**不准复述标题**）：
```html
<div class="tldr">
  <span class="tldr-head">TL;DR</span>
  <ul><li>官方只调 API 价，订阅与 quota 不变。</li></ul>
</div>
```
**误区对照**（`.mythfact`，存在普遍误解/新旧方法对照时，红=误区 / 绿=事实）：
```html
<div class="mythfact">
  <div class="mf-row myth"><span class="mf-tag">误区</span><span class="mf-text">Luna 降价 = 月费便宜</span></div>
  <div class="mf-row fact"><span class="mf-tag">事实</span><span class="mf-text">降的是 API 单价</span></div>
</div>
```
- 这些组件**别堆**：一屏 ≤2 个「大声」元素；每个都要有信息增量，否则删。
- 打印：要点框 / 误区对照的底色已加 `print-color-adjust:exact`；拉引、dropcap 是文字与
  border，打印天然保留。

### 4.36 术语注记（生僻词首现给定义）

读者可能不懂的专业词（quota、RPM、rate card…）首次出现时，给一句话定义。屏幕与打印都可见。

```html
quota<span class="term">订阅额度池</span>
```
渲染为 `quota（订阅额度池）`：术语本身保持行内代码样式（主色粗体），括号定义是弱化的
灰色小字，不打断阅读。

- 只给**生僻/领域词**定义；显然词（URL、API、CPU）不必注。
- **只首现处注**，别每个出现都加；正文本段已解释的词不必重复。
- 术语多且成体系 → 参考类型页末尾用「术语速查」表（structure-guide reference）更合适，
  正文里 `.term` 只用于零散生僻词。
- 摘要卡等静态图同理：生僻词在卡底部 `.gloss` 注记一行（见 card-template）。

### 4.37 分享摘要卡（多布局 × 多风格）

摘要卡模板 `assets/card-template.html` 内置 **6 套布局**（`.card` 上 `data-layout="..."` 切换）
× **9 套风格**（`<html data-style="..."`，与页面同套）。生成时按**内容**选布局，不只是换颜色：

| 布局 | `data-layout` | 构图 | 适合内容 |
|---|---|---|---|
| 数据型（默认） | `data` | 左侧结论 + 3~4 要点，右侧一个大数字（视觉焦点） | 有**单一关键数字**的内容（降幅、占比、耗时） |
| 观点型 | `quote` | 巨大引号 + 一句金句做主角，底部两行支撑点 | 观点/判断类——「一句话带走什么」比数字重要 |
| 头条编辑型 | `masthead` | 眉题 + 通栏大标题 + 导语 + 分隔线 + 结论/要点两栏 | 综述 / 新闻式摘要 |
| 数据网格型 | `grid` | 一行若干指标格（发丝线分隔），无单一主角 | **多指标、每个都重要**（多个配额/比率/限量），Swiss KPI 仪表盘构图 |
| 海报宣言型 | `poster` | 色条 + 巨型标题占满主视觉 + 一行支撑 | 声明 / 大胆 / 挑衅式内容（标题须短，两行内） |
| 步骤型 | `steps` | 编号步骤两列排布 | 「先做什么再做什么」的操作 / 教程 |

**选择逻辑**：先问「这张卡想让读者一眼带走什么」——一个数字→`data`；一个判断→`quote`；
一件事的来龙去脉→`masthead`；一组平行指标→`grid`；一个强立场→`poster`；一组动作→`steps`。
拿不准用 `data`。

**排版底线**（§2.3 的专业原则在卡片上的落点）：
- 大数字用 `tabular-nums` 对齐（模板已内置）；指标格发丝线分隔，无多余装饰（data-ink）
- 数据卡别堆装饰——右侧大数字 + 左侧要点是 `data` 布局的既定结构，别再加色块/图标
- 陌生名词卡底部 `.gloss` 注一行；静态图不能 hover
- 卡片必须一屏装下（1200×630）：内容放不下 → 压字删条，不是缩小字号硬塞

---

## 附录：mermaid 预渲染 SVG（复杂时序 / 状态图）

mermaid 是最流行的文本图示语法，但**运行时内联太重**（`mermaid.min.js` 实测
3.57MB / gzip 971KB），**禁止把 mermaid 运行时内联进单文件页**。正确做法：
**生成期预渲染成 SVG 再内联**——成品零 JS、矢量清晰、可打印，几 KB 到几十 KB。

流程：
1. 在 https://mermaid.live 写 mermaid 文本，预览满意
2. 导出 SVG（mermaid.live 菜单 → Save as SVG；或用 mermaid-cli / mermaid.ink API 生成）
3. 把 `<svg>...</svg>` 内联进 HTML，按 §5 图标规范统一尺寸（`width:100%; height:auto`）
4. **可访问性（硬要求）**：外层 `role="img"` + `<title>`（图名）+ `<desc>`（图意文字描述），
   屏幕阅读器才能读——mermaid 官方也自动注入 `aria-roledescription`，印证该规范
5. 深色模式注意：mermaid 默认亮色主题，SVG 内固定用深色文字/描边（不要只依赖浅色系），
   否则深色主题下会糊；必要时接受固定配色

**什么时候用**：时序图（对象间消息交互，如 API 调用链）、状态图（事件驱动状态迁移）、
类图、甘特。**简单线性流程用 §4.32 纯 CSS 流程图**——轻、可控、打印好，别杀鸡用牛刀。

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
