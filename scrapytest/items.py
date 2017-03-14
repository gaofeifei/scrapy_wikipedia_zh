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
    _id = scrapy.Field()  # 唯一标识符
    title = scrapy.Field()  # 分类
    name = scrapy.Field()  # 子分类名称
    url = scrapy.Field()  # 子分类超链接

    RESP_ITER_KEYS_WIKI_CLASS = ['title', 'name', 'url']

    def __init__(self):
        super(wikiclassifyItem, self).__init__()

    def to_dict(self):
        d = {}
        for k, v in self.items():
            if isinstance(v, (wikiclassifyItem)):
                d[k] = v.to_dict()
            else:
                d[k] = v
        return d


class linkItem(scrapy.Item):
    _id = scrapy.Field()  # 唯一标识符
    title = scrapy.Field()  # 一级目录名称
    url_link = scrapy.Field()  # 一级目录超链接
    name = scrapy.Field()  # 二级目录名称
    url = scrapy.Field()  # 二级目录页面超链接

    RESP_ITER_KEYS_LINK = ['title', 'url_link', 'name', 'url']

    def __init__(self):
        super(linkItem, self).__init__()

    def to_dict(self):
        d = {}
        for k, v in self.items():
            if isinstance(v, (linkItem)):
                d[k] = v.to_dict()
            else:
                d[k] = v
        return d


class citiaoItem(scrapy.Item):
    _id = scrapy.Field() # 唯一标识符
    name = scrapy.Field() # 词条名称
    url = scrapy.Field() # 词条页面超链接
    html = scrapy.Field() # 词条完整的HTML页面
    content = scrapy.Field() # 词条页面除上面、左面、下面的部分

    RESP_ITER_KEYS_CITIAO = ['name', 'url', 'html', 'content']

    def __init__(self):
        super(citiaoItem, self).__init__()

    def to_dict(self):
        d = {}
        for k, v in self.items():
            if isinstance(v, (citiaoItem)):
                d[k] = v.to_dict()
            else:
                d[k] = v
        return d
