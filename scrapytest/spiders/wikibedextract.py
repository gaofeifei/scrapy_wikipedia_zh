#-*-coding: utf-8-*-

import sys
import scrapy
import xlwt
import urllib
import urllib2
from scrapytest.items import wikibedItem



from BeautifulSoup import BeautifulSoup


class wikibedextract(scrapy.Spider):
    name = "wikibedpage"  # 爬虫的名字，执行时使用
    allowed_domains = ["wikipedia.kfd.me/"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = ["https://wikipedia.kfd.me/wiki/Category:%E6%96%87%E5%8C%96"]

    def parse(self, response):  # 真正的爬虫方法
        soup = BeautifulSoup(response.text)  # 得到
        HOST_URL = "https://wikipedia.kfd.me"
        results = []
        print soup.title.text  # 标题名称l
        content_title = soup.find('h1', {'id': 'firstHeading'})
        print content_title.text
        print soup.find('div', {'id': 'mw-subcategories'}).find('h2').text
        soup.find('div', {'id': 'mw-subcategories'}).find('div', {'class'})





