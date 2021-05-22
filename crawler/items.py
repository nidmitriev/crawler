# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json
import requests
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, MapCompose
from scrapy.item import Item, Field
from dataclasses import dataclass

class ImagesItem(scrapy.Item):
    url = scrapy.Field()

class ImagesItemLoader(ItemLoader):
    url_out = TakeFirst()

class OwnerItem(scrapy.Item):
    name = scrapy.Field()
    phone = scrapy.Field()

class OwnerItemLoader(ItemLoader):
    name_out = TakeFirst()
    phone_out = TakeFirst()

class OriginItem(scrapy.Item):
    source = scrapy.Field()
    owner = scrapy.Field()
    url = scrapy.Field()

class OriginItemLoader(ItemLoader):
    source_out = TakeFirst()
    url_out = TakeFirst()
    owner_out = TakeFirst()

class CoordinatesItem(scrapy.Item):
    lat = scrapy.Field()
    lon = scrapy.Field()

class CoordinatesItemLoader(ItemLoader):
    lat_out = TakeFirst()
    lon_out = TakeFirst()

class BabooshkaItem(scrapy.Item):
    name = scrapy.Field()
    # id = scrapy.Field()
    description = scrapy.Field()
    # image_url = scrapy.Field()
    # source = scrapy.Field()
    address = scrapy.Field()
    images = scrapy.Field()
    # url = scrapy.Field()
    origin = scrapy.Field()
    coordinates = scrapy.Field()



class BabooshkaItemLoader(ItemLoader):
    # id_out = TakeFirst()
    description_in = Join()
    description_out = TakeFirst()
    # image_url_out = TakeFirst()
    name_out = TakeFirst()
    # source_out = TakeFirst()
    address_out = TakeFirst()
    # url_out = TakeFirst()
    origin_out = TakeFirst()
    coordinates_out = TakeFirst()


class LocationHuntersItem(scrapy.Item):
    # name = scrapy.Field()
    # # url = scrapy.Field()
    # # id = scrapy.Field()
    # description = scrapy.Field()
    # # images = scrapy.Field()
    # source = scrapy.Field()
    # address = scrapy.Field()

    name = scrapy.Field()
    description = scrapy.Field()
    address = scrapy.Field()
    images = scrapy.Field()
    origin = scrapy.Field()
    coordinates = scrapy.Field()
    # images_url = scrapy.Field()



class LocationHuntersItemLoader(ItemLoader):
    # # url_out = TakeFirst()
    # # id_out = TakeFirst()
    # description_in = Join()
    # description_out = TakeFirst()
    # # images_out = TakeFirst()
    # name_out = TakeFirst()
    # source_out = TakeFirst()
    # address_out = TakeFirst()

    description_in = Join()
    description_out = TakeFirst()
    name_out = TakeFirst()
    address_out = TakeFirst()
    origin_out = TakeFirst()
    coordinates_out = TakeFirst()
    # images_url_out = TakeFirst()

class KinolocationItem(scrapy.Item):
    name = scrapy.Field()
    # id = scrapy.Field()
    description = scrapy.Field()
    # image_url = scrapy.Field()
    # source = scrapy.Field()
    address = scrapy.Field()
    images = scrapy.Field()
    # url = scrapy.Field()
    origin = scrapy.Field()
    coordinates = scrapy.Field()



class KinolocationItemLoader(ItemLoader):
    # id_out = TakeFirst()
    description_in = Join()
    description_out = TakeFirst()
    # image_url_out = TakeFirst()
    name_out = TakeFirst()
    # source_out = TakeFirst()
    address_out = TakeFirst()
    # url_out = TakeFirst()
    origin_out = TakeFirst()
    coordinates_out = TakeFirst()

class KinobankItem(scrapy.Item):
    name = scrapy.Field()
    # id = scrapy.Field()
    description = scrapy.Field()
    # image_url = scrapy.Field()
    # source = scrapy.Field()
    address = scrapy.Field()
    images = scrapy.Field()
    # url = scrapy.Field()
    origin = scrapy.Field()
    coordinates = scrapy.Field()


class KinobankItemLoader(ItemLoader):
    # id_out = TakeFirst()
    description_in = Join()
    description_out = TakeFirst()
    # image_url_out = TakeFirst()
    name_out = TakeFirst()
    # source_out = TakeFirst()
    address_out = TakeFirst()
    # url_out = TakeFirst()
    origin_out = TakeFirst()
    coordinates_out = TakeFirst()

class KinopartnerItem(scrapy.Item):
    name = scrapy.Field()
    # id = scrapy.Field()
    description = scrapy.Field()
    # image_url = scrapy.Field()
    # source = scrapy.Field()
    address = scrapy.Field()
    images = scrapy.Field()
    # url = scrapy.Field()
    origin = scrapy.Field()
    coordinates = scrapy.Field()


class KinopartnerItemLoader(ItemLoader):
    # id_out = TakeFirst()
    description_in = Join()
    description_out = TakeFirst()
    # image_url_out = TakeFirst()
    name_out = TakeFirst()
    # source_out = TakeFirst()
    address_out = TakeFirst()
    # url_out = TakeFirst()
    origin_out = TakeFirst()
    coordinates_out = TakeFirst()











