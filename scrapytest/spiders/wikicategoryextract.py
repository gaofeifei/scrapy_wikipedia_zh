#-*-coding: utf-8-*-

import re
import sys
import scrapy
import xlwt
import urllib
import urllib2
from scrapytest.items import wikicategoryItem
from BeautifulSoup import BeautifulSoup, SoupStrainer



class wikicategoryextract(scrapy.Spider):
    name = "wikicategoryextract"  # 爬虫的名字，执行时使用
    allowed_domains = ["wikipedia.kfd.me/"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = ["https://wikipedia.kfd.me/wiki/%E5%94%90%E7%B4%8D%C2%B7%E5%B7%9D%E6%99%AE"]

    def parse(self, response):  # 真正的爬虫方法
        soup = BeautifulSoup(response.text)  # 得到
        HOST_URL = "https://wikipedia.kfd.me"
        url_links = "https://wikipedia.kfd.me/wiki/%E5%94%90%E7%B4%8D%C2%B7%E5%B7%9D%E6%99%AE"  # 當前詞條的url
        results = []
        print '**********start*********'
        content_title = soup.find('h1', {'id': 'firstHeading'})
        category_name = content_title.string  # 詞條名稱
        print category_name
        # 當前詞條的url 就是id
        html = response.body  # response是获取到的来自网站的返回
        # print html
        # 以下四行将html存入文件  完整的wiki頁面
        filename = "wikiforTrump.html"
        file = open(filename, 'w')
        file.write(html)
        file.close()
        content_text = soup.find('div', {'id': 'mw-content-text'}).text
        print content_text
        wiki_class_item = (category_name, url_links, html, content_text)
        item = wikicategoryItem()
        keys = wikicategoryItem.RESP_ITER_KEYS_WIKI_CATEGORY
        for key in keys:
            item[key] = wiki_class_item[keys.index(key)]
            print item[key]
            print '^^^^^'
        results.append(item)
        # return results  # ????














