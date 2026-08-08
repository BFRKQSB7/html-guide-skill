#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""html-guide A4 分页成图工具

把一个 html-guide 生成的成品页，转成多张统一 A4（794×1123 @96dpi）图片：
- 生成专门的截图用 A4 HTML（去目录/按钮/进度条/页脚等多余元素），保留原页面风格
- 表格/callout/代码块整块不切，段落可在句号处跨页填满页面（正文字号 16px/1.8 占满页）
- 每页带作者页脚 + 页码；末页稀疏时垂直居中 + 「完」收尾
- 大标题超高自动缩字号（防 Arial Black 等宽字体爆开）

用法:
  python make_a4.py <输入.html> <输出目录> [--style modern|newspaper|magazine|minimal|brutal|terminal|tech] [--light|--dark]

示例:
  python make_a4.py luna.html ./luna-a4 --style magazine --light
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile

CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
SW, SH, PADX, PADY = 794, 1123, 48, 26

# 统一排版：大字号占满页面；保留主题字体身份（超高标题由 JS 收缩）
A4_CSS = """
<style>
  body{margin:0;background:#333}
  #wrap{width:794px;margin:0 auto;padding:12px 0 16px}
  .sheet{width:794px;height:1123px;background:var(--bg);padding:26px 48px;margin:0 auto 12px;box-sizing:border-box;overflow:hidden;position:relative}
  .sheet.last{display:flex;flex-direction:column;justify-content:center}
  .sheet .closing{margin-top:1.6em;text-align:center;color:var(--text-3);font-family:var(--serif);letter-spacing:.35em;font-size:1rem}
  .sheet h1{font-size:2.4rem !important;font-weight:800 !important;line-height:1.3 !important;margin:0 0 .4rem !important}
  .sheet .subtitle{font-size:.95rem !important;color:var(--text-2) !important;margin:0 0 .3rem !important;line-height:1.5 !important}
  .sheet .meta{font-size:.78rem !important;color:var(--text-3) !important;margin-bottom:.9rem !important}
  .sheet h2{font-size:1.5rem !important;font-weight:700 !important;line-height:1.3 !important;margin:1.2rem 0 .5rem !important}
  .sheet h3{font-size:1.1rem !important;margin:.9rem 0 .35rem !important}
  .sheet h4{font-size:1rem !important;margin:.8rem 0 .3rem !important}
  .sheet p,.sheet li{font-size:16px !important;line-height:1.8 !important}
  .sheet p{margin:.5em 0 .7em !important}
  .sheet ul,.sheet ol{margin:.5em 0 .7em !important}
  .sheet li{margin:.12em 0 !important}
  .sheet td{font-size:14.5px !important}
  .sheet .table-wrap,.sheet .callout,.sheet .steps,.sheet .stats,.sheet .takeaway,.sheet .tldr,.sheet .mythfact,.sheet pre,.sheet blockquote,.sheet .flow,.sheet .timeline{margin:.8em 0 !important}
  .sheet .step{margin-bottom:.7rem !important}
  .sfoot{position:absolute; left:48px; right:48px; bottom:12px; font-size:11px; color:var(--text-3);display:flex;justify-content:space-between;border-top:1px solid var(--border);padding-top:6px}
</style>
"""

PAGER_JS = """
<script>
(function(){
  var SW=794, SH=1123, PADX=48, PADY=26, CONTENT=SW-PADX*2, avail=SH-PADY*2-20;
  var nameEl = document.querySelector(".author-name") || document.querySelector(".author");
  var author = (nameEl && nameEl.textContent.trim()) || "";
  var wrap=document.getElementById("wrap");
  document.querySelectorAll("#toc,.theme-toggle,.print-btn,.to-top,.progress,.kbar,footer,.skip-link,.layout").forEach(function(e){e.style.display="none";});
  var blocks=[];
  var hero=document.querySelector("header.hero");
  var heroTitle=null;
  if(hero){
    var ht = hero.querySelector("h1");
    if(ht){ ht.querySelectorAll("br").forEach(function(b){ b.remove(); }); blocks.push(ht); heroTitle=ht; }
    [".subtitle",".meta"].forEach(function(s){ var el=hero.querySelector(s); if(el) blocks.push(el); });
  }
  document.querySelectorAll("main > section").forEach(function(sec){
    var kids=[]; for(var i=0;i<sec.children.length;i++) kids.push(sec.children[i]);
    for(var i=0;i<kids.length;i++){
      var k=kids[i];
      if(k.classList && k.classList.contains("table-wrap") && kids[i+1] && kids[i+1].tagName==="P"){
        var unit=document.createElement("div"); unit.className="block-unit";
        unit.appendChild(k); unit.appendChild(kids[i+1]);
        kids[i]=unit; kids.splice(i+1,1);
      }
    }
    kids.forEach(function(b){ blocks.push(b); });
  });
  // 测高容器必须是真实 .sheet（同宽同边距），否则按基础边距测高会高估块高、提前断页
  var meas=document.createElement("div");
  meas.className="sheet"; meas.style.cssText="position:absolute;left:-9999px;top:0;margin:0;";
  document.body.appendChild(meas);
  var inc=[], prev=0;
  blocks.forEach(function(b){ meas.appendChild(b); var r=b.getBoundingClientRect(); inc.push(Math.round(r.bottom-prev)); prev=r.bottom; });
  var pageNo=0;
  function newSheet(){ var d=document.createElement("div"); d.className="sheet"; wrap.appendChild(d);
    var f=document.createElement("div"); f.className="sfoot";
    f.innerHTML = "<span>"+author+" · 由 html-guide 生成</span><span>"+(++pageNo)+"</span>";
    d.appendChild(f); return d; }
  var used=0, page=newSheet();
  blocks.forEach(function(b,i){
    var h=inc[i];
    if(used>0 && used+h>avail){
      var splitOk=false;
      // 段落可在句号/分号处跨页（不切断句子）填满页底；表格等整块去下一页
      if(b.tagName==="P" && b.textContent.length>=30 && (avail-used)>60){
        var remaining=avail-used, text=b.textContent;
        var idx=Math.round(text.length*remaining/h), punct="。！？；：", cut=-1;
        for(var j=Math.min(idx+3,text.length-1); j>=0; j--){ if(punct.indexOf(text[j])>=0){ cut=j; break; } }
        if(cut>=10 && cut<text.length-5){
          var rest=document.createElement("p"); rest.textContent=text.slice(cut+1).trim();
          if(rest.textContent.length>=2){
            b.textContent=text.slice(0,cut+1);
            page.appendChild(b); used += b.getBoundingClientRect().height;
            var m=document.createElement("div"); m.className="sheet"; m.style.cssText="position:absolute;left:-9999px;top:0;margin:0;";
            document.body.appendChild(m); m.appendChild(rest); var rh=rest.getBoundingClientRect().height; m.remove();
            page=newSheet(); used=0; page.appendChild(rest); used+=rh; splitOk=true;
          }
        }
      }
      if(!splitOk){ page=newSheet(); used=0; page.appendChild(b); used+=h; }
    } else { page.appendChild(b); used+=h; }
  });
  meas.remove();
  document.getElementById("main").style.display="none";
  if(hero) hero.style.display="none";
  // 大标题：超高自动收缩（保留主题字体，防宽字体爆成 4 行）+ 标点断行
  if(heroTitle){
    var lh=parseFloat(getComputedStyle(heroTitle).lineHeight)||50;
    var maxH=lh*3+10, fs=parseFloat(getComputedStyle(heroTitle).fontSize)||38, g=0;
    while(heroTitle.offsetHeight>maxH && fs>14 && g++<40){ fs-=1; heroTitle.style.fontSize=fs+"px"; }
    if(heroTitle.offsetHeight>lh+8){
      var text=heroTitle.textContent, punct="，。；：、", mid=text.length/2, best=-1, bestD=1e9;
      for(var i=0;i<text.length;i++){ if(punct.indexOf(text[i])>=0){ var d=Math.abs(i-mid); if(d<bestD){bestD=d;best=i;} } }
      if(best>0){ heroTitle.textContent=""; heroTitle.appendChild(document.createTextNode(text.slice(0,best+1))); heroTitle.appendChild(document.createElement("br")); heroTitle.appendChild(document.createTextNode(text.slice(best+1))); }
    }
  }
  // 稀疏末页：垂直居中 + 收尾标记
  var sheets=document.querySelectorAll(".sheet"), last=sheets[sheets.length-1];
  if(last){
    var lastH=0;
    for(var i=0;i<last.children.length;i++){ var el=last.children[i]; if(!el.className||el.className.indexOf("sfoot")<0){ lastH+=el.getBoundingClientRect().height; } }
    if(lastH<(SH-PADY*2)*0.65){ last.classList.add("last"); var c=document.createElement("div"); c.className="closing"; c.textContent="—— 完 ——"; last.appendChild(c); }
  }
})();
</script>
"""


def build_a4_html(src_html, style, theme):
    """从源页构建 A4 成像 HTML：保留 <style>（含主题块），换 hero+main+分页。"""
    style_block = src_html[src_html.index("<style>"):src_html.index("</style>") + 8]
    try:
        hero = src_html[src_html.index('<header class="hero">'):src_html.index("</header>") + 9]
    except ValueError:
        hero = ""
    main = src_html[src_html.index('<main id="main">'):src_html.index("</main>") + 8]
    sa = ' data-style="' + style + '"' if style and style != "modern" else ""
    head = ('<!DOCTYPE html>\n<html lang="zh-CN" data-theme="' + theme + '"' + sa + '>\n'
            '<head>\n<meta charset="UTF-8">\n' + style_block + "\n" + A4_CSS + "\n</head>\n<body>\n")
    return head + hero + "\n" + main + '\n<div id="wrap"></div>\n' + PAGER_JS + "\n</body>\n</html>"


def count_sheets(a4_path):
    out = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--dump-dom",
                          "file:///" + a4_path.replace("\\", "/")],
                         capture_output=True, encoding="utf-8").stdout or ""
    return len(re.findall(r'class="sheet[^"]*"', out))


def main():
    ap = argparse.ArgumentParser(description="html-guide A4 分页成图")
    ap.add_argument("input", help="源 HTML")
    ap.add_argument("outdir", help="输出目录")
    ap.add_argument("--style", default="", help="data-style 主题：newspaper/magazine/minimal/brutal/terminal/tech")
    ap.add_argument("--light", action="store_true", help="浅色（默认跟随系统）")
    ap.add_argument("--dark", action="store_true", help="强制深色")
    args = ap.parse_args()

    src = open(args.input, encoding="utf-8").read()
    theme = "light" if args.light else ("dark" if args.dark else "")
    a4 = build_a4_html(src, args.style, theme)

    tmp = os.path.join(tempfile.gettempdir(), "htmlguide-a4.html")
    open(tmp, "w", encoding="utf-8").write(a4)

    n = count_sheets(tmp)
    if n == 0:
        print("!! 分页失败：未生成 sheet（源页是否有 <main>？）", file=sys.stderr)
        sys.exit(1)
    full_png = os.path.join(tempfile.gettempdir(), "htmlguide-a4-full.png")
    height = 12 + n * SH + (n - 1) * 12 + 16
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--screenshot=" + full_png, "--window-size=%d,%d" % (SW, height),
                    "file:///" + tmp.replace("\\", "/")], capture_output=True)

    try:
        from PIL import Image
    except ImportError:
        print("!! 需要 Pillow：pip install Pillow", file=sys.stderr)
        sys.exit(1)
    os.makedirs(args.outdir, exist_ok=True)
    im = Image.open(full_png).convert("RGB")
    for i in range(n):
        y0 = 12 + i * (SH + 12)
        im.crop((0, y0, SW, y0 + SH)).save(os.path.join(args.outdir, "page-%d.png" % (i + 1)))
    os.remove(full_png)
    print("已生成 %d 页 A4 到 %s" % (n, args.outdir))


if __name__ == "__main__":
    main()
