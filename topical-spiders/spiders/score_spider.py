from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.exceptions import DontCloseSpider
from scrapy import signals
from fronteracrawler.classifier.content_processor import ContentProcessor
from fronteracrawler.classifier.classifier import TopicClassifier
from jsonrpc_service import TopicalSpiderWebService
from fronteracrawler.worker.zookeeper import ZookeeperSession


class ScoreSpider(Spider):
    name = 'score'

    def __init__(self, *args, **kwargs):
        super(ScoreSpider, self).__init__(*args, **kwargs)
        self.contentprocessor = ContentProcessor(skip_text=False)
        self.job_config = {'disabled': True}
        self.classifier = None

    def set_process_info(self, process_info):
        self.process_info = process_info
        self.zk.set(process_info)

    def configure(self, job_config):
        self.job_config = job_config
        self.classifier = TopicClassifier.from_keywords(job_config['included'], job_config['excluded']) \
            if 'disabled' not in job_config else None

    # stable branch
    def set_crawler(self, crawler):
        super(ScoreSpider, self).set_crawler(crawler)
        self.crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)
        self.zk = ZookeeperSession(self.settings.get('ZOOKEEPER_LOCATION'), name_prefix='spider')
        self.jsonrpc_server = TopicalSpiderWebService(self, self.settings)
        self.jsonrpc_server.start_listening()


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
        if self.classifier:
            response.meta['p_score'] = self.classifier.score_paragraphs(pc.paragraphs)
        for link in pc.links:
            r = Request(url=link.url)
            r.meta.update(link_text=link.text)
            yield r