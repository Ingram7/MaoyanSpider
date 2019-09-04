# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
from ..items import MaoyanspiderItem, MaoyanReviewspiderItem


class MovieSpdSpider(scrapy.Spider):
    name = 'movie_spd'

    def start_requests(self):
        for cat in range(1, 14):
            for n in range(36):
                offset = n * 10
                url = 'http://api.meituan.com/mmdb/search/movie/category/list.json?tp=3&cat={}&offset={}&limit=10&__vhost=api.maoyan.com&utm_term=2.1.0&utm_source=MoviePro_yyb&utm_medium=android'.format(cat, offset)
                yield Request(url, callback=self.parse)

    def parse(self, response):
        res = json.loads(response.text)
        if res.get('list'):
            for data in res.get('list'):
                item = MaoyanspiderItem()
                item['cat'] = data.get('cat')
                item['dir'] = data.get('dir')
                item['dur'] = data.get('dur')
                item['id'] = data.get('id')
                item['nm'] = data.get('nm')
                item['sc'] = data.get('sc')
                item['star'] = data.get('star')
                item['img'] = data.get('img')
                item['fra'] = data.get('fra')
                item['frt'] = data.get('frt')
                item['pubDesc'] = data.get('pubDesc')
                item['rt'] = data.get('rt')
                yield item

                id = item['id']
                for n in range(101):
                    offset = n * 10
                    url_review = 'http://m.maoyan.com/mmdb/comments/movie/{}.json?_v_=yes&offset={}&limit=10'.format(id, offset)
                    yield Request(url_review, callback=self.parse_review)

    def parse_review(self, response):
        res = json.loads(response.text)
        if res.get('total') != 0 and res.get('cmts'):
            if 'offset=0' in response.url:
                for data in res.get('hcmts'):
                    item = MaoyanReviewspiderItem()
                    item['approve'] = data.get('approve')
                    item['avatarurl'] = data.get('avatarurl')
                    item['cityName'] = data.get('cityName')
                    item['content'] = data.get('content')
                    item['id'] = data.get('id')
                    item['movieId'] = data.get('movieId')
                    item['nick'] = data.get('nick')
                    item['nickName'] = data.get('nickName')
                    item['score'] = data.get('score')
                    item['startTime'] = data.get('startTime')
                    item['time'] = data.get('time')
                    item['userId'] = data.get('userId')

                    yield item

            for data in res.get('cmts'):
                item = MaoyanReviewspiderItem()
                item['approve'] = data.get('approve')
                item['avatarurl'] = data.get('avatarurl')
                item['cityName'] = data.get('cityName')
                item['content'] = data.get('content')
                item['id'] = data.get('id')
                item['movieId'] = data.get('movieId')
                item['nick'] = data.get('nick')
                item['nickName'] = data.get('nickName')
                item['score'] = data.get('score')
                item['startTime'] = data.get('startTime')
                item['time'] = data.get('time')
                item['userId'] = data.get('userId')

                yield item


