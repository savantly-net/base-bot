# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule


# class SavantlynetSpider(CrawlSpider):
#     name = "savantlynet"
#     allowed_domains = ["savantly.net"]
#     start_urls = ["https://savantly.net"]

#     rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

#     def parse_item(self, response):
#         item = {}
#         #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
#         #item["name"] = response.xpath('//div[@id="name"]').get()
#         #item["description"] = response.xpath('//div[@id="description"]').get()
#         return item

import scrapy

class MySpider(scrapy.Spider):
    name = 'savantlynet'
    allowed_domains = ['savantly.net']
    start_urls = ['http://savantly.net/']

    def parse(self, response):
        # Extract data using XPath or CSS selectors
        extracted_data = {}

        # Extract text content from paragraphs
        paragraphs = response.xpath('//p//text()').getall()
        extracted_data['paragraphs'] = paragraphs

        # Extract links
        links = response.css('a::attr(href)').getall()
        extracted_data['links'] = links

        # Extract image URLs
        image_urls = response.css('img::attr(src)').getall()
        extracted_data['image_urls'] = image_urls

        # Extract form field names
        form_fields = response.css('form input::attr(name)').getall()
        extracted_data['form_fields'] = form_fields

        # Extract headings
        headings = response.css('h1, h2, h3, h4, h5, h6').getall()
        extracted_data['headings'] = headings

        yield extracted_data

        # Follow links to other pages on the site
        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, self.parse)
