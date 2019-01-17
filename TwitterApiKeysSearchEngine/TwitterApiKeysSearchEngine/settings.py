# -*- coding: utf-8 -*-

# Scrapy settings for TwitterApiKeysSearchEngine project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'TwitterApiKeysSearchEngine'

SPIDER_MODULES = ['TwitterApiKeysSearchEngine.spiders']
NEWSPIDER_MODULE = 'TwitterApiKeysSearchEngine.spiders'

ITEM_PIPELINES = {'TwitterApiKeysSearchEngine.pipelines.SespiderPipeline': 300}

USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

DEPTH_LIMIT = 1

DOWNLOAD_DELAY = 30
