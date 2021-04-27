from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from crawler.items import BabooshkaItemLoader, BabooshkaItem

import requests


class BabooshkaSpider(CrawlSpider):
    name = 'babooshka_spider'
    allowed_domains = ['babooshka.pro']
    start_urls = ['https://babooshka.pro/avia/']
    # start_urls = ['https://babooshka.pro/']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="catalog"]'],
                allow=r'https://babooshka.pro/avia/\w+/\d+/.\w+$'
            ),
            'parse_item'
        ),
        # Rule(
        #     LinkExtractor(
        #         restrict_xpaths=['//div[@class="catalog"]'],
        #         allow=r'https://babooshka.pro/avto/\w+/\d+/.\w+$'
        #     ),
        #     'parse_item'
        # ),
    )

    # rules = (
    #     Rule(LinkExtractor(allow=('https://babooshka.pro/*')), callback='parse_item'),
    # )

    def parse_item(self, response):
        selector = Selector(response)
        l = BabooshkaItemLoader(BabooshkaItem(), selector)
        l.add_xpath('name', '//div[@class="col-lg-8 col-md-8 col-sm-12 col-xs-12"]/h3/text()')
        l.add_xpath('description', '//div[@class="col-lg-8 col-md-8 col-sm-12 col-xs-12"]/p/text()')
       # l.add_value('url', response.url)
        # l.add_xpath('id', '//5div[@class="col-lg-8 col-md-8 col-sm-12 col-xs-12"]/h3/text()')
        # l.add_xpath('images', '//img[@class="owl-lazy"]/@data-src')
        # l.add_value('images', requests.get('https://babooshka.pro/', stream=True))
        # l.add_value('images', '//a[ends-with(@class="owl-lazy"]/@data-src, ".jpg")]')
        l.add_value('source','babooshka.pro')
        l.add_value('address', 'Москва')
        return l.load_item()


