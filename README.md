# html-guide-skill

把任意内容（对话回答、笔记、代码、项目讲解、主题、URL）自动生成一份**自包含、可交互、可打印、现代化视觉**的 HTML 指导文档——教程、指南、讲解页、操作手册、学习路径皆可，页面结构根据内容自适应。

## 它能做什么

给 Claude 一个主题、一段笔记、或一句"把我刚讲的内容做成好看的 HTML"，它就会产出一个**单个 `.html` 文件**：

- **单文件自包含**：CSS / JS / 图标全部内联，零外部 CDN / 字体 / 图片，双击即可离线打开，打印成 PDF 也整洁
- **联网核实**：涉及事实、命令、版本、配置时先联网核实，页底附**可点击跳转的参考来源**（正文 `[1]` 直达）
- **结构自适应**：根据内容自动判定文档类型——操作教程 / 知识讲解 / 选型对比 / 参考速查 / 代码指南

内置的能力（骨架自带，无需手写）：

| 能力 | 说明 |
|---|---|
| 语法高亮 | 代码块像编辑器一样上色（Python/Bash/JS/TS/JSON/SQL/HTML/CSS） |
| 深浅色切换 | 右上角 ☀️/🌙，默认跟随系统，手动切换仅本次会话生效（不记忆）；切换带 0.3s 颜色过渡（尊重系统减弱动效） |
| 打印 / PDF | 右上角 🖨️，`@media print` 专为导出设计 |
| 回到顶部 | 右下角 ↑，滚动自动出现 |
| 自动目录 | 两级目录 + 滚动高亮当前位置 + `aria-current` |
| 引用跳转 | 正文上标 `[n]` 可点击直达来源（`file://` 下用 JS 滚动，无安全报错） |
| 章节快速跳转 | 按 `Ctrl+K` 弹出章节搜索，输入即过滤、键盘直达 |
| 标题锚点 | hover 显示 `¶`，方便深链到小节 |
| 阅读进度条 | 顶部细条随滚动增长 |
| 阅读时长估算 | hero 阅读时长按正文长度自动计算 |
| 决策小测 | 选完自动给结论（选型类页面） |
| 速查搜索 | 速查表搜索框吸顶常驻，实时过滤 |
| 折叠进阶 | `<details>` 渐进披露，可选/进阶内容不打断主线 |
| 代码行号 | `<pre class="linenos">` 可选行号，复制不含行号 |
| 终端徽标 | `>_` 圆角方框代表命令行内容 |
| 中文着重号 | `<span class="em">` 规范的中文强调 |
| 得分柱状图 | 对比/横评页用横向柱状图 + 得分明细表呈现真实基准分（纯 CSS，无外部库） |
| 环形图 | 占比/构成数据（厂商份额、难度分布）用环形图 + 图例呈现（纯 CSS conic-gradient） |
| 无障碍底线 | 链接下划线、`:focus-visible` 焦点环、跳过正文链接、`prefers-reduced-motion` |
| 暖纸色浅色主题 | 非纯白刺眼背景 |
| 多风格主题 | 9 套视觉主题（报纸 / 杂志 / 极简 / 瑞士国际 / 书卷 / 粗野 / 终端 / 深色科技…，含设计师血统 swiss·Müller-Brockmann、book·Tschichold），深浅色自动反转，`data-style` 一属性切换、主题按钮实时预览 |
| 摘要卡多布局 | `assets/card-template.html` 内置 6 套卡片布局（数据 / 观点 / 头条编辑 / 数据网格 / 海报 / 步骤）× 9 套风格，1200×630 分享卡，适合不能发 HTML 的渠道 |
| A4 分页成图 | `scripts/make_a4.py` 一键把成品页分成多张**同尺寸 A4** 图——表格/图表整块不切、段落句号处跨页填满、作者页脚 + 页码、末页居中收尾 |

## 安装

> 本仓库**根目录就是 skill 本体**（`SKILL.md` 在仓库根下），所以 Releases 页的 **Source code (zip)** 就是完整的 skill 安装包——直接用它即可，页面无需再找单独的 zip 资产。

### 从 Releases 安装

1. 打开 [Releases](https://github.com/BFRKQSB7/html-guide-skill/releases)，选最新版本
2. 下载 **Source code (zip)**（GitHub 对每个版本自动生成，内容即该版本的全部 skill 文件）
3. 解压 → 把解压出的文件夹放到 skills 目录（**目标目录名必须是 `html-guide`**，且里面直接就是 `SKILL.md`）：

| 平台 | 放置位置 |
|------|---------|
| Windows | `C:\Users\NYRO\.claude\skills\html-guide` |
| macOS / Linux | `~/.claude/skills/html-guide` |

### 其他安装方式

- 直接复制仓库的 `SKILL.md` + `references/` + `assets/` + `scripts/` + `evals/` 到 `~/.claude/skills/html-guide/`
- 或在 Claude Code 里用 `/plugin` 或 `/install-github-repo` 从本仓库安装

安装后重启 Claude Code，"把这段内容做成 HTML" 即可触发。

首次使用前，复制 `user-config.example.md` 为 `user-config.md` 并填写本机代理端口
（联网核实用；不填则用系统代理 / 环境变量）。`user-config.md` 是本机个性化文件，不入库。

## 触发方式

当你说出下面任意一种意思时，它会自动生效：

- "把这段内容做成一个好看的 HTML 教程 / 指南 / 讲解页"
- "把 XX 整理成一个网页"
- "把这个项目讲清楚并做成一个可打印的 HTML 文档"
- 英文："make an HTML guide"、"render this as HTML"、"create an interactive tutorial page"

## 目录结构

```
html-guide/
├── SKILL.md                    # 主流程（接收→判型→联网核实→撰写→自检交付）
├── user-config.example.md      # 个性化配置模板（复制为 user-config.md 填本机代理端口）
├── references/
│   ├── design-system.md        # 视觉设计体系 + 反 AI 味规范 + 组件库
│   ├── structure-guide.md      # 文档类型 → 页面结构映射
│   └── search-guide.md         # 联网搜索与代理降级（代理端口见 user-config.md）
├── assets/
│   ├── skeleton.html           # 可复用骨架模板（内联 CSS/JS，含全部交互 + 9 套主题）
│   └── card-template.html      # 分享摘要卡模板（6 布局 × 9 风格，1200×630）
├── scripts/
│   ├── check_html.py           # 成品自检（自包含/打印/目录/高亮/无障碍等）
│   └── make_a4.py              # A4 分页成图（长文转多张统一 A4 图，表格不切）
└── evals/                      # 评测用例集（skill-creator 规范）
```

## 验证

经 6 轮评测迭代（带 skill 对照基线），6 类用例断言通过率 100%，核心交互（语法高亮、目录、引用跳转、深浅色、吸顶搜索、决策小测、主题过渡、Ctrl+K 跳转）均经无头 Chrome 真实渲染验证。9 套主题 × 6 类卡片布局 × 深浅色均经无头渲染逐一核对（底色/强调色/对齐/无溢出），A4 分页脚本在成品页上实测通过。

## License

MIT
