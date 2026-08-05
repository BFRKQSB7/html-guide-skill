# 联网搜索与代理（7896）

Step 3 的实操指南。本环境已配置本地代理 **`127.0.0.1:7896`（Clash）**，系统级代理
已指向它，因此大多数联网方式可直接工作。下面是正确的姿势与降级方案。

---

## 1. 网络工具怎么走代理

| 工具 | 走代理方式 | 说明 |
|---|---|---|
| `WebSearch`（内置搜索） | 自动走系统代理 | 优先用它做信息检索，一条查询搜多个来源 |
| `WebFetch`（抓取网页） | 自动走系统代理 | 抓官方文档、权威页面正文 |
| `curl`（Bash） | 显式加代理参数 | 见下 |
| browser-testing skill（Chrome DevTools MCP） | 走用户浏览器 | 前两者失效 / JS 渲染页时兜底：经用户 Chrome 采集（前提：用户装有该 skill） |

`WebSearch` / `WebFetch` 是首选：它们走系统代理（即 7896），不需要额外配置。
只有需要用 Bash 直接抓数据时才用 curl。

**curl 走代理的写法（三选一，效果相同）：**

```bash
# 方式一：单条命令显式指定
curl -sL -x http://127.0.0.1:7896 https://example.com

# 方式二：会话内导出环境变量（一次性，只对当前 shell 生效）
export HTTPS_PROXY=http://127.0.0.1:7896 HTTP_PROXY=http://127.0.0.1:7896
curl -sL https://example.com
```

> Windows Git Bash 注意：`curl` 是 Git 自带的 curl。上述 `-x` 参数在 Git Bash 下同样有效。

## 2. 搜索策略

**核实对象**（写错代价高的优先）：

1. **命令与参数** —— 搜索官方文档，核对命令写法、参数名、输出格式
2. **数字与版本** —— 版本号、日期、比例、系统要求；用**当前年份**（如 `2026`）加入检索词
3. **配置与 API** —— 配置文件字段、API 端点、默认值
4. **概念定义** —— 找权威来源（官方文档、规范、知名教程）作为表述依据
5. **内容空缺** —— 用户只给主题时，正文主体来自搜索结果的综合

**检索技巧：**

- 一次搜索丢一个查询，按需拆细；用英文检索技术内容通常更准（中文做补充）
- 官网域名（`docs.xxx.com`、`learn.microsoft.com`、`developer.mozilla.org`）优先于
  个人博客；个人博客优先于问答灌水帖
- 核实一条信息，看**两个独立来源**再下结论，避免单一来源错误
- 版本敏感内容标注「截至 2026-XX」；无法核实的内容明确写「未核实」，不要硬写

## 2.5 时效性收集（横评 / 对比 / 榜单类页面必做）

这类页面的命门是「截至今天」的**完整性**——历史教训：生成「8 月最新横评」时只做主题
搜索，漏掉 DeepSeek V4 Flash 0731 正式版（8-01 发布，在 deepseek-ai 组织页按更新时间
排序是第一行）。根因：没有「枚举厂商 → 扫官方渠道 → 按时间倒序」。对策（按序执行）：

1. **厂商清单枚举**：先写死名单再逐家覆盖——OpenAI / Anthropic / Google DeepMind /
   Meta / DeepSeek / Moonshot-Kimi / Zhipu-GLM / Alibaba-Qwen / xAI / Mistral /
   ByteDance-Doubao / MiniMax。枚举保证不遗漏，而不是临场想一家搜一家
2. **官方渠道按时间倒序扫**：最可靠的是各家 Hugging Face 组织页按 `lastModified` 倒序，
   新模型/新版本一定在列表顶部；JSON API 直出、无 JS 渲染问题：
   ```bash
   curl -s -x http://127.0.0.1:7896 "https://huggingface.co/api/models?author=<厂商>&sort=lastModified&direction=-1&limit=10"
   ```
3. **日期窗口显式化**：定死 `[知识截止, 今天]` 窗口，窗口内每一家的新发布/更新必须逐条
   交代，或明确标注「该窗口内无更新」——不留空窗
4. **补官方博客 / 新闻页**：HF 之外再看每家官方 news/blog 页；**JS 渲染的 SPA 页**
   （如 DeepSeek 新闻页是 Docusaurus，抓 HTML 全是导航）改用浏览器 skill 或直接靠
   HF JSON API，别在抓 HTML 上浪费时间
5. **来源时效自检**：每个引用来源记录「数据截至」；来源最新条目早于页面日期就标注
   过期并补其他渠道

## 3. 来源记录与引用

每核实一条，记录：`来源标题 + URL`。全部收进页面的 **参考来源** 区，正文用 `<sup>[n]</sup>`
上标引用。

- 来源编号按正文出现顺序排列，与「参考来源」列表对应
- 链接可访问的必须给链接；同源多条合并为一条
- 来源数量没有硬性要求，但事实密集的页面（数字、命令、版本）建议 3~8 条

## 4. 代理/搜索失败的降级

| 现象 | 处理 |
|---|---|
| `WebSearch` 无结果或超时 | 换关键词重试一次；仍失败则用 `WebFetch` 直抓已知官方页面 |
| `WebSearch` / `WebFetch` 都失效（工具报错、域名被拦、JS 渲染拿不到正文） | 用 **browser-testing skill**（Chrome DevTools MCP）走用户浏览器采集：`new_page` 打开目标 → `evaluate_script` 提取数据/正文 → 必要时 `take_screenshot`。前提：用户装有该 skill |
| `curl` 连接被重置 / 超时 | 确认 7896 代理活着：`curl -s -x http://127.0.0.1:7896 https://www.google.com`；失败则尝试去掉 `-x` 直连（本机部分域名可直连） |
| 整个网络不可用 | 停止联网核实，在页面「参考来源」标注**「本章未联网核实，信息来自模型知识」**，正文对未核实的关键事实加 warning callout |

> 记忆参考：本机直连 `github.com` 会连接重置，git 依赖代理；只有
> `raw.githubusercontent.com` / `codeload.github.com` 可以 curl 直连。若 git 报错
> 检查 git 的 http.proxy 是否被改回了 7897。
