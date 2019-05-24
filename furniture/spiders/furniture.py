import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request

from furniture.config import SPACE_TYPE
from furniture.items import FurnitureItem


class FurnitureSpiderManager(scrapy.Spider):
    name = 'furniture'
    allowed_domains = ['homekoo.com']
    base_url = 'http://www.homekoo.com/'
    bedroom = SPACE_TYPE['bedroom']
    study_room = SPACE_TYPE['study_room']
    teenager_room = SPACE_TYPE['teenager_room']
    kitchen = SPACE_TYPE['kitchen']
    dining_room = SPACE_TYPE['dining_room']
    space_list = [bedroom, study_room, teenager_room, kitchen, dining_room]

    def start_requests(self):
        for page in range(1, 10):
            paging_url = '-p{}-fen_num_desc'.format(page)
            for space in self.space_list:
                request_url = self.base_url + space + paging_url
                yield Request(request_url, self.parse)

    def parse(self, response):
        print(response.text)
