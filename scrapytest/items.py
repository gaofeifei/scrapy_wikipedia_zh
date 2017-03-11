# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class myspiderItem(scrapy.Item):
    # define the fields for your item here like:
    top_cat = scrapy.Field()
    sub_cat = scrapy.Field()


class wikiclassifyItem(scrapy.Item):
    pub_title = scrapy.Field()
    category_id = scrapy.Field()
    category_name = scrapy.Field()
    category_url = scrapy.Field()
    RESP_ITER_KEYS_WIKI_CLASS = ['pub_title', 'category_id', 'category_name', 'category_url']


class wikibedItem(scrapy.Item):
    pubbed_title = scrapy.Field()
    categorybed_id = scrapy.Field()
    categorybed_name = scrapy.Field()
    categorybed_url = scrapy.Field()
    RESP_ITER_KEYS_WIKI_BED = ['pubbed_title', 'categorybed_id', 'categorybed_name', 'categorybed_url']


