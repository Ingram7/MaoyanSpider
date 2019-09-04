# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from .items import MaoyanspiderItem, MaoyanReviewspiderItem, MaoyanCinemasspiderItem

class MongoPipeline(object):
    def __init__(self, local_mongo_host, local_mongo_port, mongo_db):
        self.local_mongo_host = local_mongo_host
        self.local_mongo_port = local_mongo_port
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):

        return cls(
            local_mongo_host=crawler.settings.get('LOCAL_MONGO_HOST'),
            local_mongo_port=crawler.settings.get('LOCAL_MONGO_PORT'),
            mongo_db=crawler.settings.get('DB_NAME')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.local_mongo_host, self.local_mongo_port)
        # 数据库名
        self.db = self.client[self.mongo_db]
        # 以Item中collection命名 的集合  添加index
        self.db[MaoyanspiderItem.collection].create_index([('id', pymongo.ASCENDING)])
        self.db[MaoyanReviewspiderItem.collection].create_index([('id', pymongo.ASCENDING)])
        self.db[MaoyanCinemasspiderItem.collection].create_index([('id', pymongo.ASCENDING)])

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, MaoyanspiderItem):
            self.db[item.collection].update({'id': item.get('id')},
                                            {'$set': item},
                                            True
                                            )

        elif isinstance(item, MaoyanReviewspiderItem):
            self.db[item.collection].update({'id': item.get('id')},
                                            {'$set': item},
                                            True
                                            )

        elif isinstance(item, MaoyanCinemasspiderItem):
            self.db[item.collection].update({'id': item.get('id')},
                                            {'$set': item},
                                            True
                                            )
        return item
