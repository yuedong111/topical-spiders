from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.exceptions import DontCloseSpider
from scrapy import signals
from fronteracrawler.classifier.content_processor import ContentProcessor


class ScoreSpider(Spider):
    name = 'score'

    def __init__(self, *args, **kwargs):
        super(ScoreSpider, self).__init__(*args, **kwargs)
        self.contentprocessor = ContentProcessor(skip_text=False)

    # stable branch
    def set_crawler(self, crawler):
        super(ScoreSpider, self).set_crawler(crawler)
        self.crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)

    def spider_idle(self):
        self.log("Spider idle signal caught.")
        raise DontCloseSpider

    def make_requests_from_url(self, url):
        r = super(ScoreSpider, self).make_requests_from_url(url)
        return r

    def parse(self, response):
        pc = self.contentprocessor.process_response(response)
        if not pc:
            return
        for link in pc.links:
            r = Request(url=link.url)
            r.meta.update(link_text=link.text)
            yield r