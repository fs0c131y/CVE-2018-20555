"""
Scraped items models
"""

import scrapy


class KeysItem(scrapy.Item):
    """Description of KeysItem"""
    consumer_key = scrapy.Field()
    consumer_secret = scrapy.Field()
    access_token = scrapy.Field()
    access_secret = scrapy.Field()
