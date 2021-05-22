from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from crawler.items import BabooshkaItemLoader, BabooshkaItem, ImagesItem, ImagesItemLoader, \
    OwnerItem, OwnerItemLoader, OriginItem, OriginItemLoader, CoordinatesItem, CoordinatesItemLoader
from crawler.items import LocationHuntersItemLoader, LocationHuntersItem

import json
import requests


class BabooshkaSpider(CrawlSpider):
    name = 'babooshka_spider'
    allowed_domains = ['babooshka.pro']
    # start_urls = ['https://babooshka.pro/avia/', 'https://babooshka.pro/avto/avtomoika/', 'https://babooshka.pro/avto/garagi/',
    # 'https://babooshka.pro/avto/dorogi/', 'https://babooshka.pro/avto/zapravki/', 'https://babooshka.pro/avto/parking-in/',
    # 'https://babooshka.pro/avto/parking-out/','https://babooshka.pro/business/art-cluster/', 'https://babooshka.pro/business/banki/',
    # 'https://babooshka.pro/business/offices-open-space/', 'https://babooshka.pro/business/kongress-holli/',
    # 'https://babooshka.pro/business/peregovorki/', 'https://babooshka.pro/business/territories/', 'https://babooshka.pro/business/holli/',
    # 'https://babooshka.pro/ploshadi/', 'https://babooshka.pro/torgovlya/', 'https://babooshka.pro/voda/',
    # 'https://babooshka.pro/gorod/vitrini/', 'https://babooshka.pro/gorod/vhodnie-gruppi/', 'https://babooshka.pro/gorod/dvori/',
    # 'https://babooshka.pro/gorod/gilie-kompleksi/', 'https://babooshka.pro/gorod/konteineri/', 'https://babooshka.pro/gorod/roofs/',
    # 'https://babooshka.pro/gorod/podvali/', 'https://babooshka.pro/gorod/podiezdi', 'https://babooshka.pro/gorod/tonneli-i-mosti',
    # 'https://babooshka.pro/gorodskoi-transport/', 'https://babooshka.pro/gostini4nii-biznes/',
    # 'https://babooshka.pro/gilie-pomesheniya/houses/', 'https://babooshka.pro/gilie-pomesheniya/kvartiri/', 'https://babooshka.pro/zavodi/angari/',
    # 'https://babooshka.pro/promishlennost/zabroshennie-zdaniya/', 'https://babooshka.pro/zavodi/factory/',
    # 'https://babooshka.pro/promishlennost/skladi/', 'https://babooshka.pro/zoo/', 'https://babooshka.pro/kulitura-i-iskusstvo/aktovie-zali/',
    # 'https://babooshka.pro/kulitura-i-iskusstvo/galerei/', 'https://babooshka.pro/kulitura-i-iskusstvo/palaces/',
    # 'https://babooshka.pro/kulitura-i-iskusstvo/halls/', 'https://babooshka.pro/kulitura-i-iskusstvo/muzei/',
    # 'https://babooshka.pro/kulitura-i-iskusstvo/sound-studios/', 'https://babooshka.pro/kulitura-i-iskusstvo/teatri/',
    # 'https://babooshka.pro/medicina/', 'https://babooshka.pro/obrazovanie/biblioteki/', 'https://babooshka.pro/obrazovanie/school/',
    # 'https://babooshka.pro/priroda/forest/', 'https://babooshka.pro/priroda/parks/', 'https://babooshka.pro/pravo/pravoohranitelinie-organi/',
    # 'https://babooshka.pro/razvle4eniya-i-dosug/', 'https://babooshka.pro/restorannii-biznes/banketnie-zali/', 'https://babooshka.pro/restorannii-biznes/bar/',
    # 'https://babooshka.pro/restorannii-biznes/kafe-pekarni-konditerskie/', 'https://babooshka.pro/restorannii-biznes/kitchen/',
    # 'https://babooshka.pro/restorannii-biznes/restaurant/', 'https://babooshka.pro/masterskie/', 'https://babooshka.pro/saloni-krasoti/',
    # 'https://babooshka.pro/sport/basketbol/', 'https://babooshka.pro/sport/pools/', 'https://babooshka.pro/sport/velosport/',
    # 'https://babooshka.pro/sport/play-fields/', 'https://babooshka.pro/sport/ringi/', 'https://babooshka.pro/sport/stadioni-futbolinie/',
    # 'https://babooshka.pro/sport/fitness-klubi/', 'https://babooshka.pro/sport/extreme/']
    start_urls = ['https://babooshka.pro/pravo/pravoohranitelinie-organi/']



    rules = (
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/avia/\w+/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/avto/avtomoika/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/avto/garagi/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/avto/dorogi/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/avto/zapravki/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/avto/parking-in/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/avto/parking-out/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/business/art-cluster/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/business/banki/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/business/offices-open-space/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/business/kongress-holli/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/business/peregovorki/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/business/territories/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/business/holli/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/expo/ploshadi/\d+\S$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/torgovlya/\w+/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/voda/\w+/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gorod/vitrini/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gorod/vhodnie-gruppi/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gorod/dvori/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gorod/gilie-kompleksi/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gorod/konteineri/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gorod/roofs/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gorod/podvali/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gorod/podiezdi/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gorod/tonneli-i-mosti/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gorodskoi-transport/\w+/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gostini4nii-biznes/\w+\S\w+\S\w+/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gilie-pomesheniya/houses/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/gilie-pomesheniya/kvartiri/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/zavodi/angari/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/promishlennost/zabroshennie-zdaniya/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/zavodi/factory/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/promishlennost/skladi/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #
    #
    #
    #
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/zoo/\w+/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/kulitura-i-iskusstvo/aktovie-zali/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/kulitura-i-iskusstvo/galerei/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/kulitura-i-iskusstvo/palaces/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/kulitura-i-iskusstvo/halls/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/kulitura-i-iskusstvo/muzei/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/kulitura-i-iskusstvo/sound-studios/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/kulitura-i-iskusstvo/teatri/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/medicina/\w+/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/obrazovanie/biblioteki/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/obrazovanie/school/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/priroda/forest/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/priroda/parks/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="catalog"]'],
                allow=r'https://babooshka.pro/pravo/pravoohranitelinie-organi/\d+/.\w+$'
            ),
            'parse_item'
        ),
    #
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/razvle4eniya-i-dosug/\w+\S\w+/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/restorannii-biznes/banketnie-zali/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/restorannii-biznes/bar/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #             LinkExtractor(
    #                 restrict_xpaths=['//div[@class="catalog"]'],
    #                 allow=r'https://babooshka.pro/restorannii-biznes/kafe-pekarni-konditerskie/\d+/.\w+$'
    #             ),
    #             'parse_item'
    #         ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/restorannii-biznes/kitchen/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/restorannii-biznes/restaurant/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/masterskie/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/saloni-krasoti/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/sport/basketbol/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/sport/pools/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/sport/velosport/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/sport/play-fields/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/sport/ringi/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/sport/stadioni-futbolinie/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/sport/fitness-klubi/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),
    #     Rule(
    #         LinkExtractor(
    #             restrict_xpaths=['//div[@class="catalog"]'],
    #             allow=r'https://babooshka.pro/sport/extreme/\d+/.\w+$'
    #         ),
    #         'parse_item'
    #     ),


    )

    # rules = (
    #     Rule(LinkExtractor(allow=('https://babooshka.pro/*')), callback='parse_item'),
    # )


    def getImages(self, response, count):
        # imagesLoader = ImagesItemLoader(response=response)
        selector = Selector(response)
        imagesLoader = ImagesItemLoader(ImagesItem(), selector)
        images = response.xpath('//img[@class="owl-lazy"]/@data-src').extract()
        image = ("https://babooshka.pro" + image + '\t' for image in images)
        image_list = "".join(image).split('\t')
        # imagesLoader.add_value('url', "".join(image).split('\t'))
        imagesLoader.add_value('url', image_list[count])
        # return json.dumps(dict(imagesLoader.load_item()))
        return dict(imagesLoader.load_item())

    def getOrigin(self, response):
        selector = Selector(response)
        originLoader = OriginItemLoader(OriginItem(), selector)
        originLoader.add_value('source', 'babooshka.pro')
        originLoader.add_value('owner', self.getOwner(response))
        originLoader.add_value('url', response.url)
        return dict(originLoader.load_item())



    def getOwner(self, response):
        selector = Selector(response)
        ownerLoader = OwnerItemLoader(OwnerItem(), selector)
        ownerLoader.add_value('name', 'F')
        ownerLoader.add_value('phone', '89999999999')
        return dict(ownerLoader.load_item())

    def getCoordinates(self, response):
        selector = Selector(response)
        coordinatesLoader = CoordinatesItemLoader(CoordinatesItem(), selector)
        coordinatesLoader.add_value('lat', '55.83')
        coordinatesLoader.add_value('lon', '37.62')
        return dict(coordinatesLoader.load_item())

    def parse_item(self, response):
        selector = Selector(response)
        l = BabooshkaItemLoader(BabooshkaItem(), selector)
        l.add_xpath('name', '//div[@class="col-lg-8 col-md-8 col-sm-12 col-xs-12"]/h3/text()')
        description = response.xpath('//div[@class="col-lg-8 col-md-8 col-sm-12 col-xs-12"]/p/text()').extract()
        description_str = ''.join(description)
        l.add_value('description', description_str.replace('\t',''))

        # l.add_xpath('id', '//5div[@class="col-lg-8 col-md-8 col-sm-12 col-xs-12"]/h3/text()')
        # images = response.xpath('//img[@class="owl-lazy"]/@data-src').extract()
        # image = ("https://babooshka.pro" + image for image in images)
        # l.add_value('image_url', image)
        # l.add_value('source','babooshka.pro')
        l.add_value('address', 'Москва')
        l.add_value('coordinates', self.getCoordinates(response))
        images = response.xpath('//img[@class="owl-lazy"]/@data-src').extract()
        count = 0
        for image in images:
            l.add_value('images', self.getImages(response, count))
            count+=1


        # l.add_value('url', response.url)

        # origin = OriginItem()
        # origin['source'] = 'babooshka.pro'
        # owner = OwnerItem()
        # owner['name'] = 'F'
        # owner['phone'] = '89999999999'
        # origin['url'] = response.url

        l.add_value('origin', self.getOrigin(response))


        # l_1 = LocationHuntersItemLoader(LocationHuntersItem(), selector)
        # l_1.add_xpath('name', '//div[@class="number"]/h2/text()')
        # l_1.add_xpath('description', '//div[@class="info-text col-left"]/span[@class="text"]/text()')
        # # l.add_value('url', response.url)
        # # l.add_xpath('id', '//5div[@class="col-lg-8 col-md-8 col-sm-12 col-xs-12"]/h3/text()')
        # # l.add_xpath('images', '//img[@class="owl-lazy"]/@data-src')
        # # l.add_value('images', requests.get('https://babooshka.pro/', stream=True))
        # # l.add_value('images', '//a[ends-with(@class="owl-lazy"]/@data-src, ".jpg")]')
        # l_1.add_value('source', 'locationhunters.ru')
        # l_1.add_value('address', 'Москва')
        # items = {'images': [{'url': image} for BabooshkaItem.url in
        #                    zip(image)]}
        # return items

        return l.load_item()


