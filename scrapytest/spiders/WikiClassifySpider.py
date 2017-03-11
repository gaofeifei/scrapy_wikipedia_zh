# -*- coding: utf-8 -*-

import scrapy
import sys
from scrapytest.items import wikiclassifyItem
reload(sys)
sys.setdefaultencoding("utf-8")

class mywiki_spiders(scrapy.Spider):
    name = "wikiclassifyspider"  # 爬虫的名字，执行时使用

    allowed_domains = ["wikipedia.kfd.me/"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = ["https://wikipedia.kfd.me/wiki/Wikipedia:%E5%88%86%E9%A1%9E%E7%B4%A2%E5%BC%95"]

    def parse(self, response):  # 真正的爬虫方法
        td_nodes = response.xpath('//td')
        item = wikiclassifyItem()
        for td_node in td_nodes:
            pub_title = td_node.xpath('.//h2//span//b//a/text()').extract()
            for td_node_url in td_nodes:
                category = td_node_url.xpath('.//p//a/text()').extract()
                category_url = td_node_url.xpath('.//p//a/href').extract()
                for pub_title1 in pub_title:
                    pub_title1[0: max(list)]
                    title12 = title1
                    item['pub_title'] = title12.encode('utf-8')
                    # item['category'] = category
                    # item['category_url'] = category_url
                    # print '****************'
                    # print type(pub_title)
                    # print dir(pub_title)
                    # print '****************'
                    yield item

