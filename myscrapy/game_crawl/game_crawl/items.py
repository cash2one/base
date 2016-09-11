# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scr/en/latest/topics/items.html

import scrapy


class GameCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # narapy.Field()
    name = scrapy.Field()
    package_name = scrapy.Field()
    apk_mesg = scrapy.Field()
    game_pic = scrapy.Field()
    description = scrapy.Field()
    android_url = scrapy.Field()
