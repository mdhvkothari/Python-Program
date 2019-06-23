# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# first scrap data then make item in items.py then pipeline then database


class AmazonScrapPipeline(object):
    def process_item(self, item, spider):
        return item
