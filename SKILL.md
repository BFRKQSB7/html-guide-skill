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

### Step 2.5：确认输出内容（多选，先问这个）

确定完内容后，**先问用户要哪些输出**（AskUserQuestion，`multiSelect: true`，可多选）：
- **HTML**（默认，几乎总选）——单文件指导文档本体
- **长图** —— 整页内容滚成一张长图（纵向长截图，适合看全貌，流程见 Step 6.1）
- **多图（A4 分页）** —— 生成专门截图用的 A4 分页 HTML，内容按块分页成多张**同尺寸 A4** 图，
  不切断一句话/图表/表格（流程见 Step 6.2）
- **摘要卡** —— 1200×630 结论卡，供论坛 / 微信等不能发 HTML 的渠道分享（流程见 Step 6.3）

三项全不选时默认 HTML。选了「长图 / 多图 / 摘要卡」才走 Step 6 的成图流程。

### Step 2.6：确认风格（单选，后问）

再问用户用什么风格（AskUserQuestion，**强制单选**，第一项「自动推荐」）：
- 自动推荐（默认）：news 综述→`newspaper`、观点长文→`magazine`、数据横评→`minimal`、
  结构化说明/数据面→`swiss`、论文/规范→`academic`、长文讲解/深度阅读→`book`、
  命令行教程→`terminal`、产品/API 说明→`tech`、其余→`modern`
- 可见选项给「自动推荐 + 3 个与内容最贴的风格」（≤4 个），其余风格走「其他」；
  完整 9 套清单见 design-system §2.2
- 若 `user-config.md` 配了 `style:` 且用户没异议，用作默认

**先问后写**——写完整页再换皮是返工。正文与组件不随风格变，最后在 `<html data-style="...">`
写属性即可。完整内容图片与摘要卡用**同一套**风格。

### Step 3：联网核实与补充（必做）

🚧 **GATE**：Step 2 完成；已列出需要核实/补充的信息点。

> 联网是否走代理、走哪个端口，是**本机个性化信息**：先读 skill 目录下 `user-config.md`
> 的 `proxy:` 行（没有则用环境变量 `HTTP_PROXY` / `HTTPS_PROXY`；`user-config.example.md`
> 是模板）。`WebSearch` / `WebFetch` 工具默认走系统代理即可正常工作。具体配置与降级方案见
> `references/search-guide.md`。
>
> `WebSearch` / `WebFetch` 若失效（报错 / 域名被拦 / JS 渲染页拿不到正文），改用
> **browser-testing skill**（Chrome DevTools MCP）走用户浏览器采集，前提是用户装有该 skill；
> 完整降级链见 `references/search-guide.md` §4。

对以下信息点**逐条**联网核实或补充（代理配置、降级策略、引用规范都在 search-guide.md）：

1. **事实类**：数字、日期、比例、人物、公司、事件 —— 核对数值是否准确
2. **命令/代码/配置**：命令参数、API 用法、配置字段 —— 对照官方文档或权威来源
3. **版本与时效**：软件版本号、是否已过时、当前推荐做法 —— 用当前年份的检索词
4. **概念定义**：对核心概念给一个权威、通俗的表述
5. **内容空缺**：用户只给主题时，正文主体靠这一步补齐
6. **能力/可行性类主张**（最容易翻车，见 search-guide §2.6）：写「能不能 / 够不够 / 支不支持 /
   门槛多高」前**先穷尽再断言**——枚举该对象的所有社区衍生路线（量化 / 插件 / 补丁 / 替代实现 /
   变通方案等）+ 搜真实使用报告（中文 bilibili/知乎、英文 reddit / 论坛 / 官方 issue）。
   **门槛 / 下限 / 可行性类主题，真实用户实测是权威，默认必搜**；找不到证据 ≠ 不存在，穷举不全
   就把结论降级为「截至 YYYY-MM，已知途径门槛高」并注明未穷尽。**正文里的否定/限制性陈述必须带
   来源**，或用「截至日期未找到」。

搜索不一定要全覆盖 —— 优先核实那些**写错代价高**的点（命令、数字、版本、**可行性/下限**）。
常识性、无争议的内容不必为搜而搜。**「写错代价最高」的是否定性主张：一个社区反例就推翻，
还会扩散到全部交付物返工**——这类点宁多搜、勿臆断。

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
   - **按 user-config 功能偏好裁剪**：读 skill 目录下 `user-config.md` 的「功能偏好」节，
     设为 `off` 的功能省略对应元素（`#themeToggle` / `#printBtn` / `#toTop` / `#kbar` /
     `#progress` / `#toc`，映射见 user-config.example.md），骨架 JS 对缺失元素自带守卫；
     默认全开。裁剪后 check_html 对应的 warning 属预期，忽略即可
   - 可选组件按需用：`<details class="fold">` 折叠进阶/可选内容、`<pre class="linenos">`
     显示代码行号、`<span class="em">` 中文着重号（用法见 design-system §4.23–4.28）
   - 全部文字用 `<html lang="...">` 与用户语言一致（默认中文）
   - **作者署名**：读 `user-config.md` 的 `author` 键，把名字填入 hero 元信息的
     `<span class="author">`（带 GitHub 图标）与 footer；author 留空则删掉这两处作者元素。
     摘要卡（Step 6）同样署名。署名是生成时的必做项，别漏。
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
   `--a1..--a5` 加总≈100 且配了图例、功能性图标按钮（主题/打印）有简短 `.btn-tip`
   tooltip 而意义自明的（搜索/复制/回顶）不加。发现布局隐患当场修复。
   **证据自检（写错代价最高的一关，对应 search-guide §2.6）**：通读所有否定/限制性陈述
   （跑不动 / 不支持 / 仅限 / 门槛 / 下限 / 上限），逐个问——带来源了吗？来源是真实用户实测还是我
   推断的？涉及门槛 / 下限 / 可行性的，我有没有真搜过社区衍生方案与实测（bilibili / reddit /
   issue）？任何一条答不上，回去补搜或把结论降级为「截至 YYYY-MM」，不许带着没有来源的否定句交稿。
3. **防废话自检**：对照 structure-guide「跨类型通用原则」的防废话清单逐条过——
   删句测试（删掉任一句语义不变就删）、三类套话（「值得注意的是 / 在本指南中你将学到 /
   总之」式收尾）、一句一想法、结论先行；并核对每张图 / 表按「图/表/文选择」规则——非量化
   结构用图示、量化数据用柱状 / 环形、精确值用表、三行能说清不硬配图。
4. **无头渲染验证（强烈建议）**：骨架的 JS 功能（语法高亮/目录/复制/Tab/小测）一旦被改写
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
5. **清理临时文件（必做）**：无头验证产生的 `dom*.txt` 等临时文件**只放临时目录**，
   或验证后删除——**输出目录里只保留最终的 .html**。评测反馈点名过临时文件混进成品。
6. **⚠️ 严禁自动弹出浏览器**：你运行在用户的真实桌面会话里，`webbrowser.open` /
   `os.startfile` / `start` / 任何预览服务都会在用户屏幕上弹出窗口，造成干扰，**禁止使用**。
   需要视觉确认时，把文件路径告诉用户，让用户自己选择打开。
7. **交付**：把文件路径告诉用户，一句话说明这份文档的结构与来源数量。如用户需要，
   可再导出 PDF（浏览器打印 → 另存为 PDF）。

### Step 6：其他输出（按 Step 2.5 的勾选）

用户在 Step 2.5 勾了「完整内容图片」或「摘要卡」才走这里；两者都用 Step 2.6 选的那套风格。

#### 6.1 长图（整页一张，纵向长截图）

整页内容滚成一张长图，适合在支持长图的渠道看全貌（手机看图 / 图文混排）。
**局限**：页面超过 ~16000px 无法一次截（Chrome 纹理上限，需分段再拼）；长图在社交平台常被压缩。

1. **建一次性截图样式，让长图正文居中且饱满**（历史教训：直接整页截会让正文靠左、右侧一大片
   空白——TOC 隐藏后 `.layout` 仍按原宽度排，正文占不满）。注入一个 capture `<style>`（或临时
   复制页加样式，截完即删），要点：
   - 隐藏交互构件：`#toc`、`.theme-toggle`、`.print-btn`、`.to-top`、`#progress`、`.skip-link`
   - **正文居中**：`#toc{display:none}` 之后 `.layout{justify-content:center;max-width:64rem}` +
     `main{max-width:56rem;margin:0 auto}`——否则正文停留在左侧，右侧空一大块
   - **适当调大字号填满页面**：`body{font-size:19px}`、`h1{font-size:clamp(2.6rem,5.5vw,3.2rem)}`、
     `h2{font-size:1.75rem}`、`h3{font-size:1.35rem}`、`.hero .subtitle{font-size:1.3rem}`
     （比普通页面大一号，长图在手机上看才不吃力，也避免大段留白）
   - **⚠️ 覆盖要加 `!important`**：主题规则（如 `html[data-style="magazine"] main{max-width:44rem}`）
     的特异性高于裸 `main{max-width:68rem}`，不加强制会静默失效——长图列宽还是老宽度、正文依旧
     窄条靠左（已踩过：`main{max-width:68rem}` 没生效，main 仍 704px）。列宽/字号这些要覆盖主题的
     规则一律 `!important`；注入后先 `getComputedStyle` 复核实际值再截图
   - 字号放大后页高随之增加：**重测全高**，仍超 ~16000px 才走分段；`.layout` 里的 `gap` 也可适当加大
2. 整页截图：`--screenshot=long.png --window-size=1280,<全高>`（隐藏交互构件后测出的全高）
3. 超高页面：分段截（重叠 ~200px）再纵向拼接
4. 长图给「整体印象」；要耐读/可打印用 6.2 的 A4 分页

#### 6.2 多图（A4 分页，一张一页，尺寸统一）

**一键脚本**（已内置本页全部规则：统一排版/表格不切/段落跨页/作者页脚/末页居中/标题防爆开）：
```bash
python scripts/make_a4.py <输入.html> <输出目录> [--style magazine] [--light|--dark] [--scale 1.5]
```
- `--scale`：导出倍率，默认 1.0（794×1123）。**分享/发手机建议 1.5**（→1191×1684，更清晰、
  比 2× 省体积）；截图命令加 `--force-device-scale-factor`，裁剪坐标按倍率换算（含 0.5px 舍入，
  逐页独立舍入不累积）。校验仍以 794×1123 版式为准。
脚本生成一个专门截图用的 A4 分页 HTML（去掉目录 / 按钮 / 进度条 / 页脚等多余元素），
内容按**块**（段落 / 表格 / 图表 / callout / 步骤）分页成多张**同尺寸 A4**（794×1123 @96dpi），
表格/图表不跨页 → **绝不切断图表**。以下为手动流程（脚本内部逻辑，如需改细节）：

1. 基于成品页做一份 `<name>-a4.html`：保留原 `<style>`（同一套风格），去掉页面结构，换成：
   - **隐藏所有原页面元素**（含 `header.hero` 空壳——它带着 hero 的 padding 会把 wrap 往下推、
     导致截图串页；`#toc`/按钮/进度条/页脚全隐藏）
   - `#wrap`（794px 居中，底色深灰方便区分页）+ `.sheet`
     （`width:794px;height:1123px;background:var(--bg);padding:32px 48px;overflow:hidden`）
     —— **不强制浅色**，sheet 用页面主题底色，A4 页保留原网页风格
   - 每页一个页脚 `.sfoot`（作者名 + 页码，`position:absolute;bottom:12px`；作者名从页面
     `.author-name` 或 `.author` 提取文本，别用占位符）
   - 一段分页 JS：把正文块（hero 标题 + 各 section 的直接子元素）**顺序追加进测高容器**，
     用增量位置（含 margin 折叠）测每块实际占高，贪心填页（`used + h > avail` 则换页）
   - **⚠️ 测高容器必须是真实 `.sheet`**（同宽 + 同边距覆盖），不能是裸 div——否则 `.sheet p`
     等收紧边距不生效，按骨架大边距测高会**高估块高 → 提前断页 → 每页底下留大空白**
     （实测页空从 374px 降到 96px）
   - **avail 预留 ~10px** 保证内容不撞页脚
   - **每页填满检查**：分页后逐页核对内容底部——非末页不应有大块空白（块边界断页的
     适度间隙可接受）；末页内容短属正常，别强行拉满
   - **稀疏末页美化**：末页内容 <65% 页高时，`.sheet.last{display:flex;flex-direction:column;
     justify-content:center}` **垂直居中** + 末尾加收尾标记「—— 完 ——」，让大块空白
     上下均匀、像设计过的收尾而非截断
   - ⚠️ 给末页加 `.last` 类后 class 变 `class="sheet last"`，统计页数/裁剪时别用
     `grep 'class="sheet"'` 精确匹配（会漏掉末页）——用 `class="sheet[^"]*"`
   - **⚠️ 预览/验证截图必须走完整分页流程**（含 hero 大标题、作者页脚、末页收尾），
     **禁止为求快用简化版分页脚本**——漏掉 hero 提取会截出「没大标题」的假成品误导判断
     （已踩过：快速验证版只收 main 内容、漏 hero 标题，用户从截图上发现）
   - **大标题自然换行 + 加大字号**：提取 hero 标题时去掉 `<br>`；标题字号加大（约 `2.2rem`，
     节间距省下来的纵向空间给标题），明显大于 h2（h2 约 `1.35rem`）。**换行时按标点
     （，。；）在中点附近断行**（插入 `<br>`），避免第二行只剩一两个字；判断是否换行用
     **高度**（`offsetHeight > 行高`），**别用 `scrollWidth`**——换行元素的 scrollWidth
     无水平溢出，条件永远不成立
   - **排版统一（关键）**：A4 页 `.sheet` 里**强制统一字号/字重/行高**（`!important` 覆盖主题
     排版差异），但**保留主题字体身份**（别强制换黑体——brutal 的 Arial Black 等是主题气质）。
     `h1 2.2rem/800`、正文 `15px/1.6`、`h2 1.35rem/700`。保留字体后各主题分页会有小幅差异
     （如衬线/等宽字体主题多 1 页），属可接受的「容错」
   - **⚠️ 大标题防爆开**：宽字体主题（brutal 的 Arial Black/Impact）在 2.2rem 会把标题爆成
     4 行——分页后用 JS 测标题高度，超过 ~3 行就自动缩小字号（保留字体），再按标点断行
   - **用大字号填满页（正解，别反向调小）**：正文 `16px/1.8`、标题 `2.4rem`、`h2 1.5rem`。
     大字号让内容占满页面高度，表格整块放不下才去下一页——页底只余页脚区 ~20-80px。
     ⚠️ **别为「排满」越调越小**（曾降到 14px/1.45，空隙反而更大）：块边界空隙 = `avail - used`，
     字号越小 used 越小、空隙越大。表格/callout 永不切断（原则），靠大字号消空隙
   - **收紧 h2/h3 间距**：`.sheet h2{margin-top:1.1rem}` `.sheet h3{margin-top:.9rem}`
     ——骨架的 h2 用 `--space`（40-64px），在 A4 页上节间空行太大
   - **合并图注**：收集块时把 `.table-wrap`（及代码块）和紧随的注释 `<p>` 包进同一
     `.block-unit`——否则表格在上一页、注释落到下一页成孤儿（用户会看到注释跑页）
2. 无头截图 `--window-size=794,<全高>` → 按每 1123px 一页裁成 `page-NN.png`（尺寸统一）
3. 校验：每页底部留白 ≥40px（无裁切、有 A4 页边距感）；单个块超高时独占一页
4. 长文用 A4 分页比长图更耐读，也便于打印

#### 6.3 分享摘要卡

**定位**：图只装「一眼看完」的内容——给不愿读长文的人看一眼结论；HTML 给愿意读的人读完整机制。
卡片装标题 + 一句话结论 + 3~5 要点即可，**别整页截图长文**（长图字小、不能搜、没人读）。

1. 复制 `assets/card-template.html` 为 `<name>-card.html`；模板内置 **6 套布局**
   （`.card` 的 `data-layout="..."`：`data` 数据型 / `quote` 观点型 / `masthead` 头条编辑型 /
   `grid` 数据网格型 / `poster` 海报宣言型 / `steps` 步骤型，选择规则见 design-system §4.37）
   ——按内容选布局，不只换主题：一个数字→`data`、一个判断→`quote`、综述→`masthead`、
   一组平行指标→`grid`、强立场→`poster`、一组动作→`steps`。填当前布局骨架的占位内容，
   其余布局是隐藏模板不用动；改 `.card` 的 `data-layout` 即可切换
2. 卡片 `<html data-style="...">` 用与页面**同一套**风格；`data` 布局右侧大数字（数据型内容），
   观点型内容换 `quote` 布局，别硬套大数字
3. 无头截图成图（卡片版式固定 1200×630，但**导出用 2× 高清**——历史教训：1× 导出 1200×630 在手机/高分屏
   上发虚，用户自己浏览器截图（约 1.5×≈1800×945）反而更清晰）：
   ```bash
   # 高清导出：--force-device-scale-factor=2 → 2400×1260 PNG（布局不变，只提高像素密度）
   "C:/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu --hide-scrollbars \
     --force-device-scale-factor=2 \
     --screenshot=<name>-card.png --window-size=1200,630 "file:///<name>-card.html"
   ```
   - 需要更清晰可提到 scale 3（3600×1890）；校验"内容一屏装下"始终以 1200×630 的 CSS 版式为准（DPR 只改
     像素密度不改布局）
4. 内容放不下（被裁）→ 压缩要点字数或删一条，卡片必须一屏装下；陌生名词用底部 `.gloss` 注记一行

**✅ 完成。**

---

## 参考资源

| 资源 | 路径 | 何时读 |
|---|---|---|
| 视觉设计体系（配色/字体/间距/组件） | `references/design-system.md` | 每次写 HTML 前必读 |
| 文档类型→结构映射 | `references/structure-guide.md` | 每次 Step 2 判定后读对应章节 |
| 联网搜索与代理（user-config.md 个性化配置） | `references/search-guide.md` | Step 3 联网前必读 |
| HTML 骨架模板 | `assets/skeleton.html` | 每次 Step 4 作为起点 |
| 校验脚本 | `scripts/check_html.py` | Step 5 自检 |

## Notes

- **Windows**：命令用 `python`（不是 `python3`，python.org 安装版没有 `python3.exe`）。
- **不要把普通问答升级成 HTML**：只有当用户明确要「HTML/网页/页面化」时才触发本 skill；
  否则正常回答即可。
- 若用户之后对生成的页面提出修改（改配色、加章节、改结构），直接改对应 HTML 重新交付，
  不必重跑整个流程。
