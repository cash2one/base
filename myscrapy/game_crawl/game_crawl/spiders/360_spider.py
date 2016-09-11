
# -*- coding: utf-8 -*-
import scrapy

from urllib import quote

from datetime import datetime

from models import *

import json

import re

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

origin_game_list = [each[0] for each in select([game_table.c.package_name],bind=ENGINE).execute().fetchall()]

pipe_line = redis_client.pipeline()
for each_game in origin_game_list:
    pipe_line.sadd(DONE_SET, each_game)
pipe_line.execute()

class _360Spider(CrawlSpider):

    tags = xrange(1,200)

    _360_url = "http://zhushou.360.cn/list/index/cid/2/?page=%d"

    data_regx = "return[\s\r\n]*{[\s\r\n]*'sid'\s*:\s*(\d+),[\s\r\n]*'sname'\s*:\s*'(.+)',[\s\r\n]*'type'\s*:\s*'game',[\s\r\n]*'cid1'\s*:\s*\d+,[\s\r\n]*'cid2'\s*:\s*\d+,[\s\r\n]*'pname'\s*:\s*'(.+)',[\s\r\n]*'downloadUrl'\s*:\s*'(.+)',[\s\r\n]*'filemd5'\s*:\s*'\w+',[\s\r\n]*'vcode'\s*:\s*'\d+',[\s\r\n]*'baike_name\s*':\s*'(.+)'[\s\r\n]*}"

    def get_360_urls(_360_url, tags):
        re_urls = []
        for each_url in [_360_url%each_tag for each_tag in tags]:
            re_urls.append(each_url)
        return re_urls

    name = "360"
    allowed_domains = ["360.cn"]
    start_urls = (
        get_360_urls(_360_url, tags)
    )

    rules = [Rule(LinkExtractor(allow=['/detail/index/soft_id/\d+']), 'parse_game')]

    def parse_game(self, response):

        data_patterm = re.compile(self.data_regx)

        data_list = data_patterm.findall(response.body)

        if not data_list:
            return

        game_info = data_list[0]

        game_info = {"package_name":game_info[2],"name":game_info[1],"description":game_info[4],"apk_mesg":json.dumps({"apkUrl":game_info[3]}), "date_update":datetime.now()}

        if redis_client.sismember(DONE_SET, game_info["package_name"]):
            game_table.update(bind=ENGINE).where(game_table.c.package_name == game_info["package_name"]).values(**game_info).execute()
        else:
            redis_client.sadd(DONE_SET,game_info["package_name"])
            game_table.insert(bind=ENGINE).values(**game_info).execute()




