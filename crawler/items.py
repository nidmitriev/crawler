# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json
import requests
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join

class BabooshkaItem(scrapy.Item):
    name = scrapy.Field()
    # url = scrapy.Field()
    # id = scrapy.Field()
    description = scrapy.Field()
    # images = scrapy.Field()
    source = scrapy.Field()
    address = scrapy.Field()



class BabooshkaItemLoader(ItemLoader):
    # url_out = TakeFirst()
    # id_out = TakeFirst()
    description_in = Join()
    description_out = TakeFirst()
    # images_out = TakeFirst()
    name_out = TakeFirst()
    source_out = TakeFirst()
    address_out = TakeFirst()
















