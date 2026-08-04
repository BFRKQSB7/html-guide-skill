# 我的爬虫项目笔记（原始稿）

我做了一个爬虫，爬豆瓣电影 Top250 的。用 Scrapy 写的。

## 大概思路
- 入口是 start_urls，从第一页开始
- 每页 25 部电影，翻页是改 query 参数，?start=25 就是第二页
- 爬下来解析 title、rating、quote 这些字段
- 存成 JSON 或者 CSV

## 用到的东西
- scrapy 这个框架
- 需要安装 python3，然后 pip install scrapy
- 用 scrapy genspider 生成爬虫骨架
- item 里定义字段

## 几个我踩过的坑
1. 豆瓣有反爬，不设 USER_AGENT 会被 403
2. robots.txt 会挡住，要在 settings 里关掉 ROBOTSTXT_OBEY=False
3. 解析的时候 xpath 或 css 选择器要对着 devtools 里看的实际结构写
4. 别忘了关闭并发太重会被封 IP，可以设 CONCURRENT_REQUESTS 小一点，或者加下载延时 DOWNLOAD_DELAY

## 目录结构大概是
spider_tutorial/
  scrapy.cfg
  tutorial/
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
    spiders/
      __init__.py
      douban.py

## 跑法
scrapy crawl douban -o top250.json
或者 -o top250.csv
