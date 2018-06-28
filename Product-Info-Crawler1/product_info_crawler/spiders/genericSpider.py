# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
import re


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    raw_html.encode('ascii', 'ignore')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantext = cleantext.strip()
    cleantext = re.sub('\s+', ' ', cleantext)
    return cleantext




class GenericSpider(CrawlSpider):
    name = 'spider'


    def __init__(self, product='apple',  *args, **kwargs):
        super(GenericSpider, self).__init__(*args, **kwargs)
        self.product_name = product.lower()
        self.product_name = re.sub("[^ a-zA-Z0-9]+", "", self.product_name)
        print("Enter the domain if it is not there or the search url):"),
        domain = input(" domain")

        #url = domain
        self.search_url = "https://" + domain + "/" + self.product_name
        print(self.search_url)
        # self.allowed_domains = domain
        self.start_urls = "https://" +domain
        print(domain)

    rules = (
        Rule(LinkExtractor(allow=(), tags=('a'), attrs=('href'), restrict_css=('.pagnNext',)),
             callback="parse_items",
             follow=True),)

    def start_requests(self):
        print('started')
        yield scrapy.Request(self.search_url, callback=self.parse_items)



    def parse_items(self, response):
        print('Processing...', response.url)
        title = []
        image = []
        price = []
        for item in response.css("div.product-productMetaInfo"):

            item_title = item.css("h4.product-product::text").extract_first()
            item_image = item.css("img.s-access-image::attr(src)").extract_first()
            item_price = item.css("div.product-price").extract_first()

            if item_title and item_image and item_price:
                title.append(cleanhtml(item_title))
                image.append(cleanhtml(item_image))
                price.append('Rs. ' + cleanhtml(item_price))

        print('Result Counts: ', len(title))

        for item in zip(title, price, image):
            scraped_info = {
                'product_name': item[0],
                'price': item[1],
                'image_url': item[2],


            }
            yield scraped_info
