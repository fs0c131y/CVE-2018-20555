# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SespiderPipeline(object):
    def __init__(self):
        self.file = open('keys.csv', 'wb')

    def process_item(self, item, spider):
        self.file.write(item['consumer_key'] + ',' + item['consumer_secret'] + ',' +
                        item['access_token'] + ',' + item['access_secret'] + '\n')
        return item
