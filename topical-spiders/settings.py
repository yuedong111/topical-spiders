# -*- coding: utf-8 -*-

# Scrapy settings for topic project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
from scrapy.settings.default_settings import SPIDER_MIDDLEWARES, DOWNLOADER_MIDDLEWARES

BOT_NAME = 'topical-spiders'

SPIDER_MODULES = ['topical-spiders.spiders']
NEWSPIDER_MODULE = 'topical-spiders.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'topic (+http://www.yourdomain.com)'

SPIDER_MIDDLEWARES.update({
    'crawlfrontier.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 1000,
})

DOWNLOADER_MIDDLEWARES.update({
    'crawlfrontier.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 1000,
})

FRONTIER_SETTINGS = 'frontier.settings'

SCHEDULER = 'crawlfrontier.contrib.scrapy.schedulers.frontier.CrawlFrontierScheduler'
SPIDER_MIDDLEWARES.update({
    'crawlfrontier.contrib.scrapy.middlewares.seeds.file.FileSeedLoader': 1,
    'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': None,
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': None,
    'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': None,
    'scrapy.contrib.spidermiddleware.urllength.UrlLengthMiddleware': None
})

#SEEDS_SOURCE = 'seeds.txt'

HTTPCACHE_ENABLED = False
REDIRECT_ENABLED = True
COOKIES_ENABLED = False
DOWNLOAD_TIMEOUT = 120
RETRY_ENABLED = False
DOWNLOAD_MAXSIZE = 10*1024*1024

# auto throttling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = False
AUTOTHROTTLE_MAX_DELAY = 3.0
AUTOTHROTTLE_START_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = False

# concurrency
CONCURRENT_REQUESTS = 512
CONCURRENT_REQUESTS_PER_DOMAIN = 10
DOWNLOAD_DELAY = 0.0

# logging
LOGSTATS_INTERVAL = 10
#EXTENSIONS = {
#    'scrapy_jsonrpc.webservice.WebService': 500
#    }
#JSONRPC_ENABLED = True
#JSONRPC_LOGFILE = 'jsonrpc.log'

from webservice_settings import *
