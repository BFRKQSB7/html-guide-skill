#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""html-guide 输出自检脚本。

校验生成的 HTML 是否符合 html-guide 的硬性要求（单文件自包含、结构完整、
打印样式、暗色模式、目录、可访问性基础）。error 必须修复；warning 尽量修复。

用法：
    python check_html.py <path/to/output.html>
退出码：0 = 通过；1 = 存在 error。

仅依赖标准库。
"""
import re
import sys


def check(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        src = f.read()

    errors, warnings = [], []

    def err(msg):
        errors.append(msg)

    def warn(msg):
        warnings.append(msg)

    # ---- 基础结构 ----
    if not re.search(r"<!DOCTYPE html>", src, re.I):
        err("缺少 `<!DOCTYPE html>`")
    m = re.search(r"<html([^>]*)>", src, re.I)
    if not m:
        err("缺少 `<html>` 标签")
    else:
        if "lang=" not in m.group(1):
            warn("`<html>` 未声明 `lang`（可访问性）")
    if "<head>" not in src:
        err("缺少 `<head>`")
    if "<body" not in src:
        err("缺少 `<body>`")
    if not re.search(r"</html>", src, re.I):
        err("缺少闭合 `</html>`")
    if not re.search(r"<meta\s+charset", src, re.I):
        err("缺少 `<meta charset>`")
    if not re.search(r'name="viewport"', src, re.I):
        err("缺少 `name=\"viewport\"` 移动端适配")
    title = re.search(r"<title>(.*?)</title>", src, re.S)
    if not title or not title.group(1).strip():
        err("缺少 `<title>`")
    elif "页面标题" in title.group(1) or "在这里" in title.group(1):
        err("`<title>` 仍是骨架占位符，需改成实际标题")

    # ---- 单文件自包含：禁止外部资源引用 ----
    for pat, label in [
        (r'<link[^>]+rel="stylesheet"[^>]+href="https?://', "外部样式表"),
        (r'<script[^>]+src="https?://', "外部脚本"),
        (r'<img[^>]+src="https?://', "外部图片"),
        (r"url\(https?://", "CSS 中的外部 URL"),
        (r'<iframe[^>]+src="https?://', "外部 iframe"),
        (r'@import\s+url?\(', "@import 外部资源"),
    ]:
        if re.search(pat, src, re.I):
            err(f"发现{label}引用 —— 页面必须自包含，不得依赖外部资源")
    if not re.search(r"<style>", src):
        err("缺少内联 `<style>`（页面必须有内联 CSS）")

    # ---- 交互与体验 ----
    if not re.search(r"<script>", src):
        warn("缺少内联 `<script>`（交互功能：目录高亮/复制/Tab 将不可用）")
    if re.search(r"<script[^>]+src=", src):
        err("发现外部 `<script src=...>` 引用")

    # ---- 打印与暗色 ----
    if not re.search(r"@media\s*print", src):
        err("缺少 `@media print` 打印样式（用户要求可打印/导出 PDF）")
    if not re.search(r"prefers-color-scheme", src):
        warn("缺少 `prefers-color-scheme` 暗色模式适配")

    # ---- 目录 ----
    if 'id="toc"' not in src and "id='toc'" not in src:
        warn("缺少 `id=\"toc\"` 目录元素（长页面应提供目录）")

    # ---- 新特性（骨架默认内置；缺失说明偏离了骨架）----
    if not re.search(r"data-theme|themeToggle", src):
        warn("缺少深浅色切换（themeToggle / data-theme）")
    if not re.search(r"tok-|tokenize", src):
        warn("缺少代码语法高亮（tok-* 或 tokenize）")
    if not re.search(r"step-result", src):
        warn("缺少 `.step-result` 预期结果块样式（教程类页面建议使用）")

    # 代码块必须带 lang- 类（否则语法高亮不生效）——只查 <pre><code>，不误报行内 <code>
    pre_code_blocks = re.findall(r"<pre[^>]*>\s*<code[^>]*>", src)
    missing_lang = [c for c in pre_code_blocks if "lang-" not in c]
    if pre_code_blocks and missing_lang:
        warn(f"{len(missing_lang)}/{len(pre_code_blocks)} 个代码块缺少 `lang-*` 类（语法高亮将不生效）")

    # ---- 正文骨架占位残留 ----
    for placeholder in ["在这里写一句页面描述", "页面主标题", "页面标题 — 副标题"]:
        if placeholder in src:
            warn(f"发现骨架占位文本「{placeholder}」未替换")

    return errors, warnings


def main():
    # Windows 控制台默认 GBK，重配置为 UTF-8 以正确显示中文/符号
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    if len(sys.argv) < 2:
        print("用法: python check_html.py <path/to/output.html>")
        return 2
    path = sys.argv[1]
    try:
        errors, warnings = check(path)
    except FileNotFoundError:
        print(f"❌ 文件不存在: {path}")
        return 1
    except (UnicodeDecodeError, IsADirectoryError) as e:
        print(f"❌ 无法读取文件: {e}")
        return 1

    for w in warnings:
        print(f"  [WARN]  {w}")
    for e in errors:
        print(f"  [ERROR] {e}")

    print(f"\n{len(errors)} error, {len(warnings)} warning — {path}")
    if errors:
        print("存在必须修复的 error，修复后重跑本脚本。")
        return 1
    print("通过 OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
