import scrapy

from scrapy.spiders import Spider
from TwitterApiKeysSearchEngine.common.SearchResultPages import SearchResultPages
from TwitterApiKeysSearchEngine.common.SearchEngines import SearchEngineResultSelectors
from TwitterApiKeysSearchEngine.items import KeysItem
from scrapy.selector import Selector


class TwitterApiKeysSpider(Spider):
    name = 'TwitterApiKeysSpider'
    allowed_domains = ['bing.com', 'google.com', 'baidu.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None

    def __init__(self, keyword, se='bing', pages=1, *args, **kwargs):
        super(TwitterApiKeysSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        page_urls = SearchResultPages(keyword, se, int(pages))
        for url in page_urls:
            self.start_urls.append(url)

    def parse(self, response):
        for url in Selector(response).xpath(self.selector).extract():
            if 'wp-content' in url:
                if '?1=' in url and '&2=' in url and '&3=' in url and '&4=' in url:
                    consumer_key = url.split("?1=")[1].split('&')[0]
                    consumer_secret = url.split("&2=")[1].split('&')[0]
                    access_token = url.split("&3=")[1].split('&')[0]
                    access_secret = url.split("&4=")[1]
                    yield KeysItem(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_secret=access_secret)
