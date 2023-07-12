import scrapy

class SavantlynetSpider(scrapy.Spider):
    name = 'savantlynet'
    allowed_domains = ['savantly.net']
    start_urls = ['https://savantly.net']

    def parse(self, response):
        home_section = response.xpath('/html/body/div[1]/div[1]/div/div/div[3]/section[1]')
        about_section = response.xpath('/html/body/div[1]/div[1]/div/div/div[3]/section[2]')
        services_section = response.xpath('/html/body/div[1]/div[1]/div/div/div[3]/section[3]')
        portfolio_section = response.xpath('/html/body/div[1]/div[1]/div/div/div[3]/section[4]')
        contact_section = response.xpath('/html/body/div[1]/div[1]/div/div/div[3]/section[5]')

        extracted_data = {
            'home_section': self.extract_section_data(home_section),
            'about_section': self.extract_section_data(about_section),
            'services_section': self.extract_section_data(services_section),
            'portfolio_section': self.extract_section_data(portfolio_section),
            'contact_section': self.extract_section_data(contact_section),
        }

        yield extracted_data

        # Follow links to other pages on the site
        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, self.parse)

    def extract_section_data(self, section):
        data = {}

        # Extract paragraphs within the section
        paragraphs = section.xpath('.//p//text()').getall()
        data['paragraphs'] = paragraphs

        # Extract headers within the section
        headers = section.xpath('.//h1|.//h2|.//h3|.//h4|.//h5|.//h6').getall()
        data['headers'] = headers

        # Extract links within the section
        links = section.css('a::attr(href)').getall()
        data['links'] = links

        # Extract image URLs within the section
        image_urls = section.css('img::attr(src)').getall()
        data['image_urls'] = image_urls

        # Extract lists within the section
        lists = []
        list_elements = section.css('ul li::text').getall()
        lists.append(list_elements)
        data['lists'] = lists

        return data
