# -*- coding: utf-8 -*-
import scrapy
from scrapytest.items import myspiderItem


class mywiki_spiders(scrapy.Spider):
    name = "myspider"  # 爬虫的名字，执行时使用

    allowed_domains = ['dmoz.org/']  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = ['http://www.dmoz.org/']

    def parse(self, response):  # 真正的爬虫方法
        aside_nodes = response.xpath('//aside')
        for aside_node in aside_nodes:
            item = myspiderItem()
            top_cat = aside_node.xpath('.//h2//a/text()').extract()
            sub_cat = aside_node.xpath('.//h3//a/text()').extract()

            item['top_cat'] = top_cat
            item['sub_cat'] = sub_cat

            yield item

