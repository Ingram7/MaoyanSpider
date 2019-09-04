# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class MaoyanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'movie'

    cat = Field()      # 类型
    dir = Field()      # 导演
    dur = Field()      # 时长
    id = Field()       # 电影id
    nm = Field()       # 片名
    sc = Field()       # 评分
    star = Field()     # 主演
    img = Field()
    fra = Field()
    frt = Field()
    pubDesc = Field()
    rt = Field()

class MaoyanReviewspiderItem(scrapy.Item):
    collection = 'review'

    approve = Field()
    avatarurl = Field()
    cityName = Field()
    content = Field()
    id = Field()       # 评论id
    movieId = Field()  # 电影id
    nick = Field()
    nickName = Field()
    score = Field()
    startTime = Field()
    time = Field()
    userId = Field()   # 用户id


class MaoyanCinemasspiderItem(scrapy.Item):
    collection = 'cinemas'

    city_nm = Field()
    id = Field()
    nm = Field()
    sellPrice = Field()
    addr = Field()