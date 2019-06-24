# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# first scrap data then make item in items.py then pipeline then database

import sqlite3

class AmazonScrapPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" drop table if exists quotes_db """)
        self.curr.execute(""" create table quotes_db(
                        title text,
                        author text,
                        tags text) """)


    def process_item(self, item, spider):
        self.store_db(item)
        return item


    def store_db(self,item):
        self.conn.execute(""" insert into quotes_db values (?,?,?)""",(
            item['title'][0],
            item['author'][0],
            item['tags'][0]
        ))
        self.conn.commit()
