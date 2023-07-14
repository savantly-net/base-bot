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
            'home_section': self.extract_home_section_data(home_section),
            'about_section': self.extract_section_data(about_section),
            'services_section': self.extract_services_section_data(services_section),
            'portfolio_section': self.extract_portfolio_section_data(portfolio_section),
            'contact_section': self.extract_contact_section_data(contact_section),
        }

        yield extracted_data

        # Follow links to other pages on the site
        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, self.parse)

    def extract_home_section_data(self, section):
        data = {}

        service_cols = section.css('.HeroVideo__ServiceCol-sc-14xjoil-8')

        extracted_data = []
        for service_col in service_cols:
            service_data = {}
            service_data['icon'] = service_col.css('.HeroVideo__ServiceIcon-sc-14xjoil-13 img::attr(src)').get()
            service_data['heading'] = service_col.css('.HeroVideo__ServiceHeading-sc-14xjoil-11::text').get()
            service_data['text'] = service_col.css('.HeroVideo__ServiceText-sc-14xjoil-14::text').get()
            extracted_data.append(service_data)

        data['services'] = extracted_data

        return data

    def extract_section_data(self, section):
        data = {}

        paragraphs = section.xpath('.//p//text()').getall()
        data['paragraphs'] = paragraphs

        headers = section.xpath('.//h1|.//h2|.//h3|.//h4|.//h5|.//h6').getall()
        data['headers'] = headers

        links = section.css('a::attr(href)').getall()
        data['links'] = links

        image_urls = section.css('img::attr(src)').getall()
        data['image_urls'] = image_urls

        return data

    def extract_services_section_data(self, section):
        data = {}

        service_elements = section.css('.ServicesOne__ServiceElement-sc-7yiy0k-2')

        extracted_data = []
        for service_element in service_elements:
            service_data = {}
            service_data['icon'] = service_element.css('.ServicesOne__ServiceIcon-sc-7yiy0k-5 img::attr(src)').get()
            service_data['heading'] = service_element.css('.ServicesOne__ServiceHeading-sc-7yiy0k-3::text').get()
            service_data['list_elements'] = service_element.css('.ServicesOne__ServiceList-sc-7yiy0k-6 li::text').getall()
            extracted_data.append(service_data)

        data['services'] = extracted_data

        return data

    def extract_portfolio_section_data(self, section):
        data = {}

        portfolio_items = section.css('.PortfolioItem__Item-sc-2n0fpj-5')

        extracted_data = []
        for portfolio_item in portfolio_items:
            item_data = {}
            item_data['image_url'] = portfolio_item.css('img::attr(src)').get()
            item_data['title'] = portfolio_item.css('.PortfolioItem__Heading-sc-2n0fpj-2::text').get()
            item_data['subheading'] = portfolio_item.css('.PortfolioItem__SubHeading-sc-2n0fpj-3::text').get()
            item_data['link'] = portfolio_item.xpath('.//a/@href').get()
            extracted_data.append(item_data)

        data['portfolio_items'] = extracted_data

        return data

    def extract_contact_section_data(self, section):
        data = {}

        icon_rows = section.css('.ContactCreative__IconRow-sc-kz8tji-4')

        extracted_data = []
        for icon_row in icon_rows:
            info_parts = icon_row.css('.ContactCreative__InfoPart-sc-kz8tji-7')

            for info_part in info_parts:
                info = {}
                icon = info_part.css('.ContactCreative__IconContainer-sc-kz8tji-6 img::attr(src)').get()
                title = info_part.css('.ContactCreative__InfoTitle-sc-kz8tji-9::text').get()
                link = info_part.css('.ContactCreative__InfoLink-sc-kz8tji-12::text').get()

                info['icon'] = icon
                info['title'] = title
                info['link'] = link

                extracted_data.append(info)

        data['contact_info'] = extracted_data

        return data