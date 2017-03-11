#-*-coding: utf-8-*-

import re
import sys
import scrapy
import xlwt
import urllib
import urllib2
from scrapytest.items import wikiclassifyItem
from BeautifulSoup import BeautifulSoup, SoupStrainer


class wikiclassifypage(scrapy.Spider):
    name = "wikiclassifypage2"  # 爬虫的名字，执行时使用
    allowed_domains = ["wikipedia.kfd.me/"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = ["https://wikipedia.kfd.me/wiki/Wikipedia:%E5%88%86%E9%A1%9E%E7%B4%A2%E5%BC%95"]

    def parse(self, response):  # 真正的爬虫方法
        soup = BeautifulSoup(response.text)  # 得到
        HOST_URL = "https://wikipedia.kfd.me"
        results = []
        print soup.title  # 标题名称
        #print soup.body
        # id=".E7.A4.BE.E4.BC.9A"
        print '**********start*********'
        print soup.title.string
        content_title = soup.find('h1', {'id': 'firstHeading'})
        ct = content_title.string
        print ct
        # 分类标题  title="Category:社会"
        a_l = soup.find('a', {'title': 'Category:社会'}).text
        print a_l
        # 正文解析   a title="Category:文化"
        a_text = soup.find('a', {'title': 'Category:文化'}).text
        print a_text
        a_href = soup.find('a', {'title': 'Category:文化'}).get('href')
        print a_href
        # print '********'
        # soup.findAll(attrs={'style': r'vertical-align: top; padding-bottom: 1em; width: 45%;'})
        links = soup.findAll('a', attrs={'href': re.compile('/wiki/Category: *?')})
        print '!!!!!!!!!!!!!!'
        # print links
        for link in links:
            # print link
            if len(links) > 0:
                url_links = link.get('href')
                url_link = HOST_URL + link.get('href')
                title_link = link.text
                # print title_link
                # print url_link
                wiki_class_item = (ct, url_links, title_link, url_link)

                item = wikiclassifyItem()
                keys = wikiclassifyItem.RESP_ITER_KEYS_WIKI_CLASS
                for key in keys:
                    item[key] = wiki_class_item[keys.index(key)]
                    print item[key]
                    print '^^^^^'
                results.append(item)
                return results  # ????












