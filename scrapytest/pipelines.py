# -*- coding: utf-8 -*-

import time
import pymongo
from scrapytest.items import citiaoItem
from scrapytest.utils import _default_mongo
from twisted.internet.threads import deferToThread
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


class MongodbPipeline(object):
    def __init__(self, host, port, db_name, citiao_collection):
        self.db_name = db_name
        self.host = host
        self.port = port
        self.db = _default_mongo(host, port, usedb=db_name)
        self.citiao_collection = citiao_collection

    @classmethod
    def from_settings(cls, settings):
        db_name = settings.get('MONGOD_DB', None)
        host = settings.get('MONGOD_HOST', None)
        port = settings.get('MONGOD_PORT', None)
        citiao_collection = settings.get('CITIAO_COLLECTION', None)
        return cls(host, port, db_name, citiao_collection)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def process_item(self, item, spider):
        if isinstance(item, citiaoItem):
            return deferToThread(self.process_citiao, item, spider)

    def process_item_sync(self, item, spider):
        if isinstance(item, citiaoItem):
            return self.process_citiao(item, spider)

    def process_citiao(self, item, spider):
        citiao = item.to_dict()
        citiao["_id"] = citiao["url"]

        if self.db[self.citiao_collection].find({"_id": citiao["_id"]}).count():
            self.update_citiao(self.citiao_collection, citiao)
        else:
            try:
                citiao["first_in"] = time.time()
                citiao["last_modify"] = citiao["first_in"]
                self.db[self.citiao_collection].insert(citiao)
            except pymongo.errors.DuplicateKeyError:
                self.update_citiao(self.citiao_collection, citiao)

        return item

    def update_citiao(self, collection, item):
        updates = {}
        updates['last_modify'] = time.time()
        for key in citiaoItem.RESP_ITER_KEYS_CITIAO:
            if item.get(key) is not None:
                updates[key] = item[key]

        updates_modifier = {"$set": updates}
        self.db[collection].update({"_id": item["_id"]}, updates_modifier)
