# user-config.md 模板 — 本机个性化配置

复制本文件为 `user-config.md` 并填写。`user-config.md` 存**本机个性化信息**，
已在 `.gitignore` 排除，**不随 skill 发布到 GitHub**。

⚠️ 重要：代理端口、账号等是**每台机器各不相同**的个性化信息，不要把它们写进
skill 正文（SKILL.md / search-guide.md / design-system.md），否则发布时会把
个人环境当通用默认。

## 网络代理（search-guide 联网时读取）

`proxy:` 行是 search-guide Step 3 联网时用的代理地址。每台机器不同，例如：
- Clash 用户常见 `http://127.0.0.1:7890`（或其他端口）
- v2ray / SSR / 系统代理可能是其他端口，或直接用系统代理不填

```ini
proxy: http://127.0.0.1:<你的代理端口>
```

如果不需要代理（或系统已全局代理、直接可上网），可留空。

## 功能偏好（可选，默认全开）

不想要某个内置功能，就写 `off`；生成页面时会省略对应元素（骨架 JS 对缺失元素
自带守卫，不会报错）。

| 键 | 功能 | 关闭时省略的元素 |
|---|---|---|
| `theme-toggle` | 右上角深浅色切换按钮 | `#themeToggle` |
| `print-btn` | 右上角打印 / 导出 PDF 按钮 | `#printBtn` |
| `to-top` | 右下角回到顶部按钮 | `#toTop` |
| `kbar` | Ctrl+K 章节快速跳转 | `#kbar` 弹层 |
| `progress` | 顶部阅读进度条 | `#progress` |
| `toc` | 侧边自动目录 | `#toc` |

```ini
theme-toggle: on
print-btn: on
to-top: on
kbar: on
progress: on
toc: on
```

## 作者署名（可选，默认空 = 不署名）

生成页面与摘要卡时，把这里的名字写入 hero 元信息与 footer（带 GitHub 图标）。
想改署名只需改这一行，重生成即可。

```ini
author: 你的GitHub用户名
```

## 本机专属备注（可选）

放只对你自己有意义的联网备注，例如本机某些域名要直连 / 依赖代理等。
