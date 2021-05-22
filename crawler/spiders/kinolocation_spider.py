from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from crawler.items import KinolocationItem, KinolocationItemLoader, ImagesItem, ImagesItemLoader, \
    OwnerItem, OwnerItemLoader, OriginItem, OriginItemLoader, CoordinatesItem, CoordinatesItemLoader
from crawler.items import LocationHuntersItemLoader, LocationHuntersItem

import json
import requests


class KinolocationSpider(CrawlSpider):
    name = 'kinolocation_spider'
    allowed_domains = ['kinolocation.ru']
    start_urls = ['http://kinolocation.ru/category/objects/apartments/',
                  'http://kinolocation.ru/category/objects/houses/',
                  'http://kinolocation.ru/category/objects/offices/',
                  'http://kinolocation.ru/category/objects/more-objects/aerodrom/',
                  'http://kinolocation.ru/category/objects/more-objects/autoservice-parking/',
                  'http://kinolocation.ru/category/objects/more-objects/business-centre/',
                  'http://kinolocation.ru/category/objects/more-objects/hospital/',
                  'http://kinolocation.ru/category/objects/more-objects/hotel/',
                  'http://kinolocation.ru/category/objects/more-objects/yard/',
                  'http://kinolocation.ru/category/objects/more-objects/dk-art/',
                  'http://kinolocation.ru/category/objects/more-objects/zabroshka/',
                  'http://kinolocation.ru/category/objects/more-objects/roof/',
                  'http://kinolocation.ru/category/objects/more-objects/basement-katakomba/',
                  'http://kinolocation.ru/category/objects/more-objects/factory/',
                  'http://kinolocation.ru/category/objects/more-objects/spaces-loft/',
                  'http://kinolocation.ru/category/objects/more-objects/secure/',
                  'http://kinolocation.ru/category/objects/more-objects/restorant-cafe-club/',
                  'http://kinolocation.ru/category/objects/more-objects/sport/',
                  'http://kinolocation.ru/category/objects/more-objects/mansion/',
                  'http://kinolocation.ru/category/objects/more-objects/education/',
                  'http://kinolocation.ru/category/objects/more-objects/yachts/'
                  ]



    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="content"]'],
                allow=r'http://kinolocation.ru/\d+\D+$'
            ),
            'parse_item'
        ),
    )



    def getImages(self, response, count):
        selector = Selector(response)
        imagesLoader = ImagesItemLoader(ImagesItem(), selector)
        images = response.xpath('//li[@class="blocks-gallery-item"]/figure/a/img/@src').extract()
        image = (image + '\t' for image in images)
        image_list = "".join(image).split('\t')
        imagesLoader.add_value('url', image_list[count])
        return dict(imagesLoader.load_item())

    def getOrigin(self, response):
        selector = Selector(response)
        originLoader = OriginItemLoader(OriginItem(), selector)
        originLoader.add_value('source', 'kinolocation.ru')
        originLoader.add_value('owner', self.getOwner(response))
        originLoader.add_value('url', response.url)
        return dict(originLoader.load_item())



    def getOwner(self, response):
        selector = Selector(response)
        ownerLoader = OwnerItemLoader(OwnerItem(), selector)
        ownerLoader.add_value('name', 'KL')
        ownerLoader.add_value('phone', '89999990000')
        return dict(ownerLoader.load_item())

    def getCoordinates(self, response):
        selector = Selector(response)
        coordinatesLoader = CoordinatesItemLoader(CoordinatesItem(), selector)
        coordinatesLoader.add_value('lat', '55.73')
        coordinatesLoader.add_value('lon', '37.52')
        return dict(coordinatesLoader.load_item())

    def parse_item(self, response):
        selector = Selector(response)
        l = KinolocationItemLoader(KinolocationItem(), selector)
        l.add_xpath('name', '//div[@class="post-wrap post-wrap-page"]/div/h2/text()')
        l.add_value('description', '')
        l.add_value('address', 'Москва')
        l.add_value('coordinates', self.getCoordinates(response))
        images = response.xpath('//li[@class="blocks-gallery-item"]/figure/a/img/@src').extract()
        count = 0
        for image in images:
            l.add_value('images', self.getImages(response, count))
            count+=1
        l.add_value('origin', self.getOrigin(response))

        return l.load_item()


