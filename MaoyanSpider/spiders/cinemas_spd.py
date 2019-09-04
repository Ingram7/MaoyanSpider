# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
from ..items import MaoyanCinemasspiderItem

class CinemasSpdSpider(scrapy.Spider):
    name = 'cinemas_spd'

    start_urls = ['https://maoyan.com/ajax/cities']

    def parse(self, response):
        res = json.loads(response.text)
        data = res.get('letterMap')
        print(data)
        for key in data.keys():
            list = data.get(key)
            for i in list:
                id = i.get('id')
                city_nm = i.get('nm')

                url = 'https://m.maoyan.com/ajax/cinemaList?day=2019-09-03&offset=0&limit=100&cityId={}'.format(id)
                yield Request(url, callback=self.parse_info, meta={'city_nm': city_nm})

    def parse_info(self, response):
        res = json.loads(response.text)
        if res.get('cinemas'):
            city_nm = response.meta['city_nm']
            if 'offset=0' in response.url:
                all_page = (res.get('paging').get('total'))//100
                for page_num in range(1, all_page + 1):
                    page_url = response.url.replace('offset=0', 'offset={}'.format(page_num))
                    yield Request(page_url, self.parse_info, dont_filter=True, meta={'city_nm': city_nm})

            for data in res.get('cinemas'):
                item = MaoyanCinemasspiderItem()
                item['city_nm'] = city_nm
                item['id'] = data.get('id')
                item['nm'] = data.get('nm')
                item['sellPrice'] = data.get('sellPrice')
                item['addr'] = data.get('addr')
                yield item