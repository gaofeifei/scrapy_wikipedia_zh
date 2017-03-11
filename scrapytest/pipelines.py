# -*- coding: utf-8 -*-
from scrapy.exporters import JsonItemExporter, CsvItemExporter, XMLGenerator

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapytestPipeline(object):
    def process_item(self, item, spider):
        return item


class BestsellerItemJsonPipeline(object):

    def open_spider(self, spider):
        self.file = open('XXX.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
         self.exporter.export_item(item)
         return item