
# -*- coding: utf-8 -*-
import scrapy

from urllib import quote

from models import *

from datetime import datetime

import json

import re

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

origin_game_list = [each[0] for each in select([game_table.c.package_name],bind=ENGINE).execute().fetchall()]

pipe_line = redis_client.pipeline()
for each_game in origin_game_list:
    pipe_line.sadd(DONE_SET, each_game)
pipe_line.execute()

class BaiDuSpider(scrapy.Spider):

    tags = xrange(401,409)

    baidu_url = "http://shouji.baidu.com/game/list?cid={0}&page_num=%d"

    #data_regx = 'data-action="game"\s*.*data-mod=".+"\s*.*data-tj="(.+)"\s*.*data-pos=".+"\s*.*data_type="apk"\s*.*data_url="(.+)"\s*.*data_name="(.+)"\s*.*data_detail_type="app"\s*.*data_package="(.+)"\s*.*data_versionname=".+"\s*.*data_icon="(.+)"\s*.*data_size=".+"'

    data_regx = 'data-action="game"[\s\r\n]*data-mod=".+?"[\s\r\n]*data-tj="(.+)"[\s\r\n]*data-pos=".+?"[\s\r\n]*data_type="apk"[\s\r\n]*data_url="(.+)"[\s\r\n]*data_name="(.+)"[\s\r\n]*data_detail_type="app"[\s\r\n]*data_package="(.+)"[\s\r\n]*data_versionname=".+?"[\s\r\n]*data_icon="(.+)"[\s\r\n]*data_size=".+?"'

    def get_baidu_urls(baidu_url, tags):
        re_urls = []
        for each_url in [baidu_url.format(each_tag) for each_tag in tags]:
            for each_index in xrange(1,9):
                re_urls.append(each_url % each_index)
        return re_urls

    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = (
        get_baidu_urls(baidu_url, tags)
    )

    #rules = [Rule(LinkExtractor(allow=['/game/item?docid=\d+']), 'parse_game')]

    def parse(self, response):

        data_patterm = re.compile(self.data_regx)

        data_list = data_patterm.findall(response.body)

        if data_list:
            for each_game_info in data_list:

                #game_info = {"package_name":each_game_info[3],"name":each_game_info[2],"description":each_game_info[0],"apk_mesg":json.dumps({"apkUrl":each_game_info[1]}),"game_pic":each_game_info[4],"date_update":datetime.now()}
                game_info = {"package_name":each_game_info[3],"name":each_game_info[2],"description":each_game_info[0],"apk_mesg":json.dumps({"apkUrl":each_game_info[1]}),"date_update":datetime.now()}

                if redis_client.sismember(DONE_SET, game_info["package_name"]):
                    game_table.update(bind=ENGINE).where(game_table.c.package_name == game_info["package_name"]).values(**game_info).execute()
                else:
                    redis_client.sadd(DONE_SET, game_info["package_name"])
                    game_table.insert(bind=ENGINE).values(**game_info).execute()
