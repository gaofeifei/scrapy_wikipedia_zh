#-*-coding: utf-8-*-

import sys
import scrapy
import xlwt
import urllib
import urllib2
from scrapytest.items import wikiclassifyItem
from BeautifulSoup import BeautifulSoup


class wikiclassifypage(scrapy.Spider):
    name = "wikiclassifypage"  # 爬虫的名字，执行时使用
    allowed_domains = ["wikipedia.kfd.me/"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = ["https://wikipedia.kfd.me/wiki/Wikipedia:%E5%88%86%E9%A1%9E%E7%B4%A2%E5%BC%95"]

    def parse(self, response):  # 真正的爬虫方法
        soup = BeautifulSoup(response.text)  # 得到
        item = wikiclassifyItem()
        HOST_URL = "https://wikipedia.kfd.me"
        results = []
        print soup.title  # 标题名称
        #print soup.body
        # id=".E7.A4.BE.E4.BC.9A"
        print '**********start*********'
        print soup.title.string
        content_title = soup.find('h1', {'id': 'firstHeading'})
        print content_title.string
        # 分类标题  title="Category:社会"
        a_l = soup.find('a', {'title': 'Category:社会'}).text
        print a_l
        # 正文解析   a title="Category:文化"
        a_text = soup.find('a', {'title': 'Category:文化'}).text
        print a_text
        a_href = soup.find('a', {'title': 'Category:文化'}).get('href')
        print a_href
        # print '********'
        tds = soup.findAll(attrs={'style': r'vertical-align: top; padding-bottom: 1em; width: 45%;'})
        print '!!!!!!!!!!!!!!'
        print tds
        print '!!!!!!!!!!!!!!'
        # print '********'
        item['pub_title'] = a_l
        item['category_id'] = a_href
        item['category_name'] = a_text
        a_hrefs = HOST_URL + a_href
        item['category_url'] = a_hrefs
        print '%%%%%%%%%%%'
        print item['pub_title']
        print item['category_id']
        print item['category_name']
        print item['category_url']
        wiki_class_item = [a_l, a_href, a_text, a_hrefs]
        item_wiki = wikiclassifyItem()
        keys = wikiclassifyItem.RESP_ITER_KEYS_WIKI_CLASS
        for key in keys:
            item[key] = wiki_class_item[keys.index(key)]
            print '&&&&&&&'
            print item[key]
        results.append(item)
        print '*&*&*&*&*&*&'
        print results.pop(0)
        list_h2s = tds.find('h2')
        if list_h2s:
            result_lis = list_h2s.findAll('a')
            if len(result_lis) == 0:
                return results
            for li in result_lis:
                title_a = li.find('a').text
                url_a = li.find('a').get('href')
                print title_a
                print url_a
                print '%%%%%%%%%%%'
                print '**********end*********'
        return results











