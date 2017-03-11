#-*-coding: utf-8-*-

import scrapy
from scrapy import Request
from scrapytest.items import citiaoItem
from BeautifulSoup import BeautifulSoup


class wikicategoryextract(scrapy.Spider):
    name = "wikicategoryextract"  # 爬虫的名字，执行时使用
    allowed_domains = ["wikipedia.kfd.me/"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = ["https://wikipedia.kfd.me/wiki/%E5%94%90%E7%B4%8D%C2%B7%E5%B7%9D%E6%99%AE"]

    def __init__(self):
        pass

    def start_requests(self):
        for url in self.start_urls:
            req = Request(url)
            req.meta['url'] = url
            yield req

    def parse(self, response):  # 真正的爬虫方法
        url_link = response.meta['url']
        results = []
        print '**********start*********'
        html = response.body  # response是获取到的来自网站的返回
        # print html
        # 以下四行将html存入文件  完整的wiki頁面
        filename = "wikiforTrump.html"
        file = open(filename, 'w')
        file.write(html)
        file.close()
        soup = BeautifulSoup(html)  # 得到
        content_text = soup.find('div', {'id': 'mw-content-text'}).text
        name = soup.find("h1", {"id": "firstHeading"}).text
        wiki_citiao_item = (name, url_link, html, content_text)
        item = citiaoItem()
        keys = citiaoItem.RESP_ITER_KEYS_CITIAO
        for key in keys:
            item[key] = wiki_citiao_item[keys.index(key)]
            print '^^^^^'
        results.append(item)
        return results  # ????

