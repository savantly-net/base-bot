import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.linkextractors import LinkExtractor
from scrapy.settings import Settings
from scrapy.spiders import CrawlSpider, Spider, Rule
from scrapy.http import Response
import os
from twisted.internet.asyncioreactor import install
install()

import twisted.internet.reactor

PROJECT_DIRECTORY = f"{os.path.dirname(os.path.realpath(__file__))}/../../.."

DOCS_PATH = f"{PROJECT_DIRECTORY}/data/docs"


class ScrapedPage(scrapy.Item):
    url = scrapy.Field()
    status = scrapy.Field()
    headers = scrapy.Field()
    text = scrapy.Field()
    links = scrapy.Field()

class GenericSpider(scrapy.Spider):
    name = "generic"
    allowed_domains = ["savantly.net"]
    start_urls = ["https://savantly.net"]

    def parse(self, response):
        item = {
            'url': response.url,
            'status': response.status,
            'text': '\n'.join(response.xpath('//body//text()').getall()),
        }
        yield item
    