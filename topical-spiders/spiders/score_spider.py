from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.exceptions import DontCloseSpider
from scrapy import signals
from content_processor import ContentProcessor
from classifier import TopicClassifier


class ScoreSpider(Spider):
    name = 'score'

    def __init__(self, topic_dict, features=None, disable_classifier=False, *args, **kwargs):
        super(ScoreSpider, self).__init__(*args, **kwargs)
        self.contentprocessor = ContentProcessor()
        self.featuresoutput = open(features, 'w') if features else None
        self.topicclassifier = TopicClassifier(topic_dict)
        self.disable_classifier = disable_classifier

    # stable branch
    def set_crawler(self, crawler):
        super(ScoreSpider, self).set_crawler(crawler)
        self.crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)

    def spider_idle(self):
        self.log("Spider idle signal caught.")
        raise DontCloseSpider

    def make_requests_from_url(self, url):
        r = super(ScoreSpider, self).make_requests_from_url(url)
        return self.process_request(r)

    def process_request(self, request):
        request.meta['score'] = 1.0
        return request

    def parse(self, response):
        pc = self.contentprocessor.process_response(response)
        if self.featuresoutput:
            obj_str = pc.to_JSON()
            self.featuresoutput.write(str(len(obj_str)))
            self.featuresoutput.write('\n')
            self.featuresoutput.write(obj_str)
            self.featuresoutput.write('\n')

        if self.disable_classifier or self.topicclassifier.classify_paragraphs(pc.paragraphs):
            for link in pc.links:
                r = Request(url=link.url)
                r.meta.update(link_text=link.text)
                yield r