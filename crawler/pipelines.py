# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter


import json
import requests
import ast


class JsonWriterPipeline:

    # def open_spider(self, spider):
    #     # self.file = open('locationHunters.json', 'w')
    #     # self.file = open('babooshka_1.json', 'w')
    #     # self.file = open('kinolocation.json', 'w')
    #     # self.file = open('kinobank.json', 'w')
    #     self.file = open('kinopartner.json', 'w')
    #
    # def close_spider(self, spider):
    #     self.file.close()

    # def process_item_1(self, item_1, spider):
    #     line_1 = json.dumps(dict(item_1)) + "\n"
    #     r = requests.post("https://cinemalocations.ru/api/token", params={"email": "admin", "password": "123456"})
    #     token = r.json()["token"]
    #
    #     headers = {
    #         "Authorization": "Bearer " + token,
    #         "Content-Type": "application/json"
    #     }
    #     r = requests.post("https://cinemalocations.ru/api/location", json=ast.literal_eval(line_1), headers=headers)
    #
    #     print(r.text)
    #
    #     self.file.write(line_1)
    #     return item_1



    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"


        print (line)
        l = ast.literal_eval(line)
        print (l)

        r = requests.post("https://cinemalocations.ru/api/token", params={"email": "admin", "password": "123456"})
        token = r.json()["token"]

        # location = {
        #     "name": "Номер объекта: 1700",
        #     "description": "Темное пространство .",
        #     "address": "Москва",
        #     "source": "babooshka.pro",
        #     "owner": {
        #         "name": "",
        #         "phone": ""
        #     },
        #     "images": [
        #         {"url": "https://babooshka.pro/bw-themes/babooshka_pro/data/catalog/0/1700/30541_i_big.jpg"},
        #         {"url": "https://babooshka.pro/bw-themes/babooshka_pro/data/catalog/0/1700/30540_i_big.jpg"}
        #     ]
        # }
        # print (location)

        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }
        r = requests.post("https://cinemalocations.ru/api/location?generateTags=1", json=ast.literal_eval(line), headers=headers)
       # r = requests.post("https://cinemalocations.ru/api/location", json=location, headers=headers)

        print(r.text)

        # self.file.write(line)
        return item







