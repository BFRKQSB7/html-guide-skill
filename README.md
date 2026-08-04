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
| 深浅色切换 | 右上角 ☀️/🌙，跟随系统 + 手动覆盖 |
| 打印 / PDF | 右上角 🖨️，`@media print` 专为导出设计 |
| 回到顶部 | 右下角 ↑，滚动自动出现 |
| 自动目录 | 两级目录 + 滚动高亮当前位置 + 隐藏滚动条 |
| 引用跳转 | 正文上标 `[n]` 可点击直达来源 |
| 决策小测 | 选完自动给结论（选型类页面） |
| 速查搜索 | 速查表搜索框吸顶常驻，实时过滤 |
| 终端徽标 | `>_` 圆角方框代表命令行内容 |
| 暖纸色浅色主题 | 非纯白刺眼背景 |

## 安装

把 `html-guide` 文件夹放进你的 Claude Code skills 目录：

- **Windows**: `C:\Users\NYRO\.claude\skills\html-guide`
- **macOS / Linux**: `~/.claude/skills/html-guide`

（也可在 Claude Code 里用 `/plugin` 或 `/install-github-repo` 从本仓库安装。）

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
├── references/
│   ├── design-system.md        # 视觉设计体系 + 反 AI 味规范
│   ├── structure-guide.md      # 文档类型 → 页面结构映射
│   └── search-guide.md         # 联网搜索与代理降级（curl -x 127.0.0.1:7896）
├── assets/
│   └── skeleton.html           # 可复用骨架模板（内联 CSS/JS，含全部交互）
├── scripts/
│   └── check_html.py           # 成品自检（自包含/打印/目录/高亮等）
└── evals/                      # 评测用例集（skill-creator 规范）
```

## 验证

经过 4 轮评测迭代（带 skill 对照基线），6 类用例断言通过率 100%，核心质量点（语法高亮、目录、引用跳转、深浅色、吸顶搜索、决策小测）均经无头 Chrome 真实渲染验证。

## License

MIT
