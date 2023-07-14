import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.linkextractors import LinkExtractor
from scrapy.settings import Settings
from scrapy.spiders import CrawlSpider, Spider, Rule
from scrapy.exporters import JsonLinesItemExporter
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

    custom_settings = {
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': 'output.jsonl'
    }

    def __init__(self, start_url=None, *args, **kwargs):
        super(GenericSpider, self).__init__(*args, **kwargs)
        if start_url:
            self.start_urls = [start_url]

    def parse(self, response):
        scraped_page = ScrapedPage()
        scraped_page['url'] = response.url
        scraped_page['status'] = response.status
        scraped_page['headers'] = response.headers
        scraped_page['text'] = '\n'.join(response.xpath('//body//text()').getall())
        scraped_page['links'] = [link.url for link in LinkExtractor(allow_domains=self.allowed_domains).extract_links(response)]
        yield scraped_page
