from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from crawler.items import KinopartnerItem, KinopartnerItemLoader, ImagesItem, ImagesItemLoader, \
    OwnerItem, OwnerItemLoader, OriginItem, OriginItemLoader, CoordinatesItem, CoordinatesItemLoader


class KinopartnerSpider(CrawlSpider):
    name = 'kinopartner_spider'

    allowed_domains = ['kinopartner.ru']
    start_urls = ['https://kinopartner.ru/shop/doma/filter/klass=a-ehlitnye-doma',
                  'https://kinopartner.ru/shop/doma/doma_srednie',
                  'https://kinopartner.ru/shop/doma/filter/klass=c-doma-nizhe-srednego',
                  'https://kinopartner.ru/shop/doma/filter/klass=d-doma-derevenskie-i-istoricheskie',
                  'https://kinopartner.ru/shop/kvartiry/filter/klass=a-ehlitnye-kvartiry',
                  'https://kinopartner.ru/shop/kvartiry/filter/klass=b-srednie-kvartiry',
                  'https://kinopartner.ru/shop/kvartiry/filter/klass=c-kvartiry-nizhe-srednego',
                  'https://kinopartner.ru/shop/kvartiry/filter/klass=d-istoricheskie-stalinki-kommunalki',
                  'https://kinopartner.ru/shop/ofisy/filter/klass=a-ehlitnye-ofisy',
                  'https://kinopartner.ru/shop/ofisy/filter/klass=b-srednie-ofisy',
                  'https://kinopartner.ru/shop/ofisy/filter/klass=c-ofisy-nizhe-srednego',
                  'https://kinopartner.ru/shop/ofisy/filter/klass=d-ofisy-istoricheskie',
                  'https://kinopartner.ru/shop/bolnicy-kliniki-i-medcentry/filter/klass=a-ehlitnye',
                  'https://kinopartner.ru/shop/bolnicy-kliniki-i-medcentry/filter/klass=b-srednie',
                  'https://kinopartner.ru/shop/bolnicy-kliniki-i-medcentry/filter/klass=c-nizhe-srednego',
                  'https://kinopartner.ru/shop/bolnicy-kliniki-i-medcentry/filter/klass=d-istoricheskie',
                  'https://kinopartner.ru/shop/angary-zavody-pavilyony',
                  'https://kinopartner.ru/shop/teatry-dk-koncertnye-zaly',
                  'https://kinopartner.ru/shop/kompleksnye-nalichie-raznykh-lokacij-na-odnom-obekte/filter/klass=a-ehlitnye',
                  'https://kinopartner.ru/shop/kompleksnye-nalichie-raznykh-lokacij-na-odnom-obekte/filter/klass=b-srednie',
                  'https://kinopartner.ru/shop/kompleksnye-nalichie-raznykh-lokacij-na-odnom-obekte/filter/klass=c-nizhe-srednego',
                  'https://kinopartner.ru/shop/kompleksnye-nalichie-raznykh-lokacij-na-odnom-obekte/filter/klass=d-istoricheskie',
                  'https://kinopartner.ru/shop/kafe-i-restorany/filter/klass=a-ehlitnye-kafe-i-restorany',
                  'https://kinopartner.ru/shop/kafe-i-restorany/filter/klass=b-srednie-kafe-i-restorany',
                  'https://kinopartner.ru/shop/kafe-i-restorany/filter/klass=c-kafe-i-restorany-nizhe-srednego',
                  'https://kinopartner.ru/shop/sportivnye',
                  'https://kinopartner.ru/shop/kryshi-i-podvaly',
                  'https://kinopartner.ru/shop/galerei-vystavki-muzei',
                  'https://kinopartner.ru/shop/ehksterery',
                  'https://kinopartner.ru/shop/naturnye',
                  'https://kinopartner.ru/shop/obrazovatelnye-uchrezhdenija-i-detsady',
                  'https://kinopartner.ru/shop/khudozhestvennye-skulpturnye-i-dr-masterskie',
                  'https://kinopartner.ru/shop/otdelenija-policii-izoljatory-tjurmy',
                  'https://kinopartner.ru/shop/salony-krasoty-parikmakherskie',
                  'https://kinopartner.ru/shop/fotostudii-i-studii-zvukozapisi',
                  'https://kinopartner.ru/shop/drugie',
                  'https://kinopartner.ru/shop/loft-prostranstva',
                  'https://kinopartner.ru/shop/magaziny-i-tc',
                  'https://kinopartner.ru/shop/gostinicy-i-obshhezhitija',
                  'https://kinopartner.ru/shop/derevenskie_doma/filter/klass=a-ehlitnye-doma',
                  'https://kinopartner.ru/shop/derevenskie_doma/filter/klass=b-srednie-doma',
                  'https://kinopartner.ru/shop/derevenskie_doma/filter/klass=c-doma-nizhe-srednego',
                  'https://kinopartner.ru/shop/derevenskie_doma/filter/klass=d-doma-derevenskie-i-istoricheskie'
                  ]
    # start_urls = ['https://kinopartner.ru/shop/derevenskie_doma/filter/klass=d-doma-derevenskie-i-istoricheskie']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="goods-list with-clear"]'],
                allow=r'https://kinopartner.ru/shop/\d+/\w+/\S+$'
            ),
            'parse_item'
        ),
    )



    # def getImages(self, response, count):
    #     selector = Selector(response)
    #     imagesLoader = ImagesItemLoader(ImagesItem(), selector)
    #     images = response.xpath('//div[@class="col-4"]/a/img/@src').extract()
    #     image = ("https://kinopartner.ru" + image + '\t' for image in images)
    #     image_list = "".join(image).split('\t')
    #     imagesLoader.add_value('url', image_list[count])
    #     return dict(imagesLoader.load_item())

    def getOrigin(self, response):
        selector = Selector(response)
        originLoader = OriginItemLoader(OriginItem(), selector)
        originLoader.add_value('source', 'kinopartner.ru')
        originLoader.add_value('owner', self.getOwner(response))
        originLoader.add_value('url', response.url)
        return dict(originLoader.load_item())

    def getOwner(self, response):
        selector = Selector(response)
        ownerLoader = OwnerItemLoader(OwnerItem(), selector)
        ownerLoader.add_value('name', 'KP')
        ownerLoader.add_value('phone', '89999990002')
        return dict(ownerLoader.load_item())
    #
    def getCoordinates(self, response):
        selector = Selector(response)
        coordinatesLoader = CoordinatesItemLoader(CoordinatesItem(), selector)
        coordinatesLoader.add_value('lat', '55.62')
        coordinatesLoader.add_value('lon', '37.54')
        return dict(coordinatesLoader.load_item())

    def parse_item(self, response):
        selector = Selector(response)
        l = KinopartnerItemLoader(KinopartnerItem(), selector)
        l.add_xpath('name', '//h1[@class="eTitle"]/text()')
        description = response.xpath('//div[@class="shop-brief"]/text()').extract()
        description_str = ''.join(description).replace('\t', '')
        description_str = description_str.replace('\xa0', '')
        l.add_value('description', description_str.replace('\n', ''))
        l.add_value('address', 'Москва')
        l.add_value('coordinates', self.getCoordinates(response))

        # images = response.xpath('//div[@class="col-4"]/a/img/@class').extract()
        # count = 0
        # for image in images:
        #     l.add_value('images', self.getImages(response, count))
        #     count+=1

        l.add_value('origin', self.getOrigin(response))

        return l.load_item()


