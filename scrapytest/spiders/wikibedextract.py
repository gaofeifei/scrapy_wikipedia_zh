#  -*-coding: utf-8-*-

import scrapy
from scrapy import Request
from scrapytest.items import linkItem
from BeautifulSoup import BeautifulSoup


class wikibedextract(scrapy.Spider):
    name = "wikibedpage"  # 爬虫的名字，执行时使用
    allowed_domains = ["wikipedia.kfd.me/"]
    start_urls = ["https://wikipedia.kfd.me/wiki/Category:%E6%96%87%E5%8C%96"]

    def __init__(self):
        pass

    def start_requests(self):
        for url in self.start_urls:
            req = Request(url)
            req.meta['url'] = url
            yield req

    def parse(self, response):
        link_url = response.meta['url']
        HOST_URL = "https://wikipedia.kfd.me"
        results = []
        # title = soup.title.text  # 标题名称
        # print title
        print '**********start*********'
        html = response.body
        soup = BeautifulSoup(html)
        title = soup.find('h1', {'id': 'firstHeading'}).text
        links = soup.findAll('a', {'class': 'CategoryTreeLabel  CategoryTreeLabelNs14 CategoryTreeLabelCategory'})
        for link in links:
            if len(links) > 0:
                url = HOST_URL + link.get('href')  # 二级子分类页面中所有超链接
                name = link.text
                wiki_link_item = (title, link_url, name, url)
                item = linkItem()
                keys = linkItem.RESP_ITER_KEYS_LINK
                for key in keys:
                    item[key] = wiki_link_item[keys.index(key)]
                    print '*********'
                    results.append(item)
                    return results