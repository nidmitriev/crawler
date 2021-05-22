from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from crawler.items import KinobankItem, KinobankItemLoader, ImagesItem, ImagesItemLoader, \
    OwnerItem, OwnerItemLoader, OriginItem, OriginItemLoader, CoordinatesItem, CoordinatesItemLoader


class KinobankSpider(CrawlSpider):
    name = 'kinobank_spider'
    allowed_domains = ['kino-bank.com']
    # start_urls = ['https://kino-bank.com/listing-category/moskva/hotels/gostinitsy-oteli/', 'https://kino-bank.com/listing-category/moskva/hotels/obshchezhitiya/',
    # 'https://kino-bank.com/listing-category/moskva/hotels/doma-otdykha-pansionaty/', 'https://kino-bank.com/listing-category/moskva/hotels/pionerskie-lagerya/',
    # 'https://kino-bank.com/listing-category/moskva/decorations/interernye/', 'https://kino-bank.com/listing-category/moskva/decorations/eksterernye/',
    # 'https://kino-bank.com/listing-category/moskva/theatres/kinoteatry/', 'https://kino-bank.com/listing-category/moskva/theatres/doma-kultury/',
    # 'https://kino-bank.com/listing-category/moskva/stations/zh-d/', 'https://kino-bank.com/listing-category/moskva/stations/avia/',
    # 'https://kino-bank.com/listing-category/moskva/stations/avto/', 'https://kino-bank.com/listing-category/moskva/animals/',
    # 'https://kino-bank.com/listing-category/moskva/abandoned/', 'https://kino-bank.com/listing-category/moskva/country/sovremennye/',
    # 'https://kino-bank.com/listing-category/moskva/country/derevyannye/', 'https://kino-bank.com/listing-category/moskva/country/khay-tek/',
    # 'https://kino-bank.com/listing-category/moskva/country/pentkhausy/', 'https://kino-bank.com/listing-category/moskva/country/derevenskie/',
    # 'https://kino-bank.com/listing-category/moskva/country/dachi/', 'https://kino-bank.com/listing-category/moskva/country/dvortsy/',
    # 'https://kino-bank.com/listing-category/moskva/country/istoricheskie-professorskie-dachi/', 'https://kino-bank.com/listing-category/moskva/historical/deystvuyushchie/',
    # 'https://kino-bank.com/listing-category/moskva/historical/zabroshennye/', 'https://kino-bank.com/listing-category/moskva/apartments/pentkhausy/',
    # 'https://kino-bank.com/listing-category/moskva/apartments/apartamenty-khaytek/', 'https://kino-bank.com/listing-category/moskva/apartments/kvartiry-epokhi-sssr/',
    # 'https://kino-bank.com/listing-category/moskva/apartments/professorskie/', 'https://kino-bank.com/listing-category/moskva/apartments/prostye-kvartiry/',
    # 'https://kino-bank.com/listing-category/moskva/apartments/kommunalki/', 'https://kino-bank.com/listing-category/moskva/apartments/bez-otdelki/',
    # 'https://kino-bank.com/listing-category/moskva/apartments/vyselenki/', 'https://kino-bank.com/listing-category/moskva/apartments/lofty/',
    # 'https://kino-bank.com/listing-category/moskva/apartments/masterskaya-khudozhnika/', 'https://kino-bank.com/listing-category/moskva/apartments/obshchezhitiya/',
    # 'https://kino-bank.com/listing-category/moskva/apartments/sovremennye-kvartiry/', 'https://kino-bank.com/listing-category/moskva/roofs/',
    # 'https://kino-bank.com/listing-category/moskva/culture/vystavochnye-zaly-galerei/', 'https://kino-bank.com/listing-category/moskva/culture/muzei-masterskie/',
    # 'https://kino-bank.com/listing-category/moskva/kuhni-kulinarnye-studii/', 'https://kino-bank.com/listing-category/moskva/lofts/',
    # 'https://kino-bank.com/listing-category/moskva/education/shkoly/',
    # 'https://kino-bank.com/listing-category/moskva/education/instituty/',
    # 'https://kino-bank.com/listing-category/moskva/hospitals/bolnitsy/',
    # 'https://kino-bank.com/listing-category/moskva/hospitals/morgi/',
    # 'https://kino-bank.com/listing-category/moskva/hospitals/apteki/',
    # 'https://kino-bank.com/listing-category/moskva/water/',
    # 'https://kino-bank.com/listing-category/moskva/office/open-space/',
    # 'https://kino-bank.com/listing-category/moskva/office/ofisy/',
    # 'https://kino-bank.com/listing-category/moskva/office/peregovornye-komnaty/',
    # 'https://kino-bank.com/listing-category/moskva/office/kabinety-sssr/',
    # 'https://kino-bank.com/listing-category/moskva/office/biznes-tsentry/',
    # 'https://kino-bank.com/listing-category/moskva/paviloni-type/semochnye-pavilony/',
    # 'https://kino-bank.com/listing-category/moskva/paviloni-type/tsiklorama/',
    # 'https://kino-bank.com/listing-category/moskva/paviloni-type/fotostudiya/',
    # 'https://kino-bank.com/listing-category/moskva/paviloni-type/telestudii/',
    # 'https://kino-bank.com/listing-category/moskva/parks/',
    # 'https://kino-bank.com/listing-category/moskva/production/deystvuyushchie/',
    # 'https://kino-bank.com/listing-category/moskva/production/zabroshennye-/',
    # 'https://kino-bank.com/listing-category/moskva/other/',
    # 'https://kino-bank.com/listing-category/moskva/special-objects/voennye/',
    # 'https://kino-bank.com/listing-category/moskva/special-objects/ovd/',
    # 'https://kino-bank.com/listing-category/moskva/special-objects/sudy-tyurmy/',
    # 'https://kino-bank.com/listing-category/moskva/religion/',
    # 'https://kino-bank.com/listing-category/moskva/bars/',
    # 'https://kino-bank.com/listing-category/moskva/salons/',
    # 'https://kino-bank.com/listing-category/moskva/sport/',
    # 'https://kino-bank.com/listing-category/moskva/studio/',
    # 'https://kino-bank.com/listing-category/moskva/market/',
    # 'https://kino-bank.com/listing-category/moskva/transport/']
    start_urls = ['https://kino-bank.com/listing-category/moskva/abandoned/']


    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="col-lg-10 col-md-9 col-sm-9 col-xs-12 content-bar"]'],
                allow=r'https://kino-bank.com/listings/\D+$'
            ),
            'parse_item'
        ),
    )



    def getImages(self, response, count):
        selector = Selector(response)
        imagesLoader = ImagesItemLoader(ImagesItem(), selector)
        images = response.xpath('//div[@class="row row-img"]/div/a/@href').extract()
        image = ("https://kino-bank.com" + image + '\t' for image in images)
        image_list = "".join(image).split('\t')
        imagesLoader.add_value('url', image_list[count])
        return dict(imagesLoader.load_item())

    def getOrigin(self, response):
        selector = Selector(response)
        originLoader = OriginItemLoader(OriginItem(), selector)
        originLoader.add_value('source', 'kino-bank.com')
        originLoader.add_value('owner', self.getOwner(response))
        originLoader.add_value('url', response.url)
        return dict(originLoader.load_item())

    def getOwner(self, response):
        selector = Selector(response)
        ownerLoader = OwnerItemLoader(OwnerItem(), selector)
        ownerLoader.add_value('name', 'KB')
        ownerLoader.add_value('phone', '89999990001')
        return dict(ownerLoader.load_item())

    def getCoordinates(self, response):
        selector = Selector(response)
        coordinatesLoader = CoordinatesItemLoader(CoordinatesItem(), selector)
        coordinatesLoader.add_value('lat', '55.81')
        coordinatesLoader.add_value('lon', '37.60')
        return dict(coordinatesLoader.load_item())

    def parse_item(self, response):
        selector = Selector(response)
        l = KinobankItemLoader(KinobankItem(), selector)
        l.add_xpath('name', '//div[@class="item-top"]/h1/text()')
        description = response.xpath('//div[@class="tab-pane active"]/text()').extract()
        description_str = ''.join(description).replace('\t', '')
        l.add_value('description', description_str.replace('\n', ''))
        l.add_value('address', 'Москва')
        l.add_value('coordinates', self.getCoordinates(response))
        images = response.xpath('//div[@class="row row-img"]/div/a/@href').extract()
        count = 0
        for image in images:
            l.add_value('images', self.getImages(response, count))
            count+=1
        l.add_value('origin', self.getOrigin(response))

        return l.load_item()


