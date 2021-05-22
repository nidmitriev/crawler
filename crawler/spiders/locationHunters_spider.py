import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from crawler.items import LocationHuntersItemLoader, LocationHuntersItem, ImagesItem, ImagesItemLoader, \
    OwnerItem, OwnerItemLoader, OriginItem, OriginItemLoader, CoordinatesItem, CoordinatesItemLoader

import requests



# class LocationHuntersSpider(scrapy.Spider):
#     name = 'locationHunters_spider'
#     allowed_domains = ['locationhunters.ru']
#     start_urls = ['https://locationhunters.ru/']


    # def parse(self, response):
    #
    #     print("procesing:"+response.url)
    #     # Извлечение данных с помощью селекторов CSS
    #     # product_name=response.css('.item-title::text').extract()
    #     # price_range=response.css('.price-current::text').extract()
    #     # Извлечение данных с использованием xpath
    #     name=response.xpath('//div[@class="number"]/h2/text()').extract()
    #     description=response.xpath('//div[@class="info-text col-left"]/span[@class="text"]/text()').extract()
    #     source='locationhunters.ru'
    #     address='Москва'
    #
    #     row_data=zip(name,description,source,address)
    #
    #     # извлечение данных строки
    #     for item in row_data:
    #         # создать словарь для хранения извлеченной информации
    #         scraped_info = {
    #             'page': response.url,
    #             'name': item[0],  # item[0] означает продукт в списке и т. д., индекс указывает, какое значение назначить
    #             'description': item[1],
    #             'source': item[2],
    #             'address': item[3],
    #         }
    #
    #         # генерируем очищенную информацию для скрапа
    #         yield scraped_info


class LocationHuntersSpider(CrawlSpider):
    name = 'locationHunters_spider'
    allowed_domains = ['locationhunters.ru']
    start_urls = ['https://locationhunters.ru/new_catalog/']


    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="all-location col-right"]'],
                allow=r'https://locationhunters.ru/new_catalog/\w+\W\w+\W\w+\W\w+$'
            ),
            'parse_item'
        ),
    )

    def getImages(self, response, count):
        selector = Selector(response)
        imagesLoader = ImagesItemLoader(ImagesItem(), selector)
        images = response.xpath('//ul[@class="slider"]/li/img/@src').extract()
        image = ("https://locationhunters.ru" + image + '\t' for image in images)
        image_list = "".join(image).split('\t')
        imagesLoader.add_value('url', image_list[count])
        return dict(imagesLoader.load_item())

    def getOrigin(self, response):
        selector = Selector(response)
        originLoader = OriginItemLoader(OriginItem(), selector)
        originLoader.add_value('source', 'locationhunters.ru')
        originLoader.add_value('owner', self.getOwner(response))
        originLoader.add_value('url', response.url)
        return dict(originLoader.load_item())

    def getOwner(self, response):
        selector = Selector(response)
        ownerLoader = OwnerItemLoader(OwnerItem(), selector)
        ownerLoader.add_value('name', 'LH')
        ownerLoader.add_value('phone', '89999999010')
        return dict(ownerLoader.load_item())

    def getCoordinates(self, response):
        selector = Selector(response)
        coordinatesLoader = CoordinatesItemLoader(CoordinatesItem(), selector)
        coordinatesLoader.add_value('lat', '55.83')
        coordinatesLoader.add_value('lon', '37.59')
        return dict(coordinatesLoader.load_item())


    def parse_item(self, response):
        selector = Selector(response)
        l = LocationHuntersItemLoader(LocationHuntersItem(), selector)
        l.add_xpath('name', '//div[@class="name col-left"]/h2/text()')
        # l.add_xpath('description', '//div[@class="info-text col-left"]/div[@class="text"]/text()')

        l.add_value('description', '')

        # description = response.xpath('//div[@class="info-text col-left"]/div[@class="text"]/text()').extract()
        # description_str = ''.join(description)
        # l.add_value('description', description_str)
        # l.add_value('description', 'ABC')

        l.add_value('address', 'Москва')
        l.add_value('coordinates', self.getCoordinates(response))


        images = response.xpath('//ul[@class="slider"]/li/img/@src').extract()
        count = 0
        for image in images:
            while (count < 5):
                l.add_value('images', self.getImages(response, count))
                count += 1


        # images = response.xpath('//IMG[@src="/upload/iblock/71e/71efbb6010eb6e75da607f2aaf9f11e0.jpg"])[1]').extract()
        # image = ("https://babooshka.pro" + image for image in images)
        # l.add_value('images_url', image)


        # l.add_xpath('images_url', '//ul[@class="slider"]/li/img/@src')


        # l.add_value('url', response.url)



        l.add_value('origin', self.getOrigin(response))


        return l.load_item()


