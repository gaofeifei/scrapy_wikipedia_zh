#  -*-coding: utf-8-*-

import re
import scrapy
from scrapy import Request
from scrapytest.items import wikiclassifyItem
from BeautifulSoup import BeautifulSoup


class wikiclassifypage(scrapy.Spider):
    name = "wikiclassifypage3"  # 爬虫的名字，执行时使用
    allowed_domains = ["wikipedia.kfd.me/"]
    start_urls = ["https://wikipedia.kfd.me/wiki/Wikipedia:%E5%88%86%E9%A1%9E%E7%B4%A2%E5%BC%95"]


    def __init__(self):
        pass

    def start_requests(self):
        for url in self.start_urls:
            req = Request(url)
            req.meta['url'] = url
            yield req

    def parse(self, response):
        url_link = response.meta['url']
        HOST_URL = "https://wikipedia.kfd.me"
        results = []
        print '**********start*********'
        html = response.body
        soup = BeautifulSoup(html)
        title = soup.find('h1', {'id': 'firstHeading'}).text
        links = soup.findAll('a', attrs={'href': re.compile('/wiki/Category: *?')})
        for link in links:
            # print link
            if len(links) > 0:
                name = link.text
                url = HOST_URL + link.get('href')
                wiki_class_item = (title, name, url)
                item = wikiclassifyItem()
                keys = wikiclassifyItem.RESP_ITER_KEYS_WIKI_CLASS
                for key in keys:
                    item[key] = wiki_class_item[keys.index(key)]
                    print '********'
                results.append(item)
                return results