
# -*- coding: utf-8 -*-
import scrapy

from urllib import quote

from models import *

import json

origin_game_list = [each[0] for each in select([game_table.c.package_name],bind=ENGINE).execute().fetchall()]

pipe_line = redis_client.pipeline()
for each_game in origin_game_list:
    pipe_line.sadd(DONE_SET, each_game)
pipe_line.execute()

from datetime import datetime

class QQSpider(scrapy.Spider):

    tags = [0, 147, 121, 144, 148, 149, 153, 146, 151]

    qq_url = "http://android.myapp.com/myapp/cate/appList.htm?orgame=2&categoryId=%d&pageSize=1000&pageContext={0}"

    def get_qq_urls(qq_url, tags):
        re_urls = []
        for each_url in [qq_url%each_tag for each_tag in tags]:
            for each_index in xrange(0, 1):
                re_urls.append(each_url.format(each_index))
        return re_urls

    name = "qq"
    allowed_domains = ["myapp.com"]
    start_urls = (
        get_qq_urls(qq_url, tags)
    )

    def parse(self, response):
        update_list = []
        insert_list = []

        game_list = []
        for each_game in json.loads(response.body)["obj"]:
            try:
                if not each_game["pkgName"]:
                    continue

                pic_small = each_game["iconUrl"]
                pic_big = pic_small[:-2] + '256'

                game_list.append({"package_name":each_game["pkgName"],"name":each_game["appName"],"description":each_game["editorIntro"],"apk_mesg":json.dumps({"apkUrl":each_game["apkUrl"], "categoryName":each_game["categoryName"], "images":each_game["images"]}),"game_pic":pic_big,"date_update":datetime.now()})

            except Exception as error:
                print("==","do_with_response() -> json.loads() Error.","==")

        for each_game in game_list:
            if redis_client.sismember(DONE_SET, each_game["package_name"]):
                update_list.append(each_game)
            else:
                insert_list.append(each_game)
                #redis_client.sadd(WAIT_SET,each_game["package_name"])

        if update_list:
            game_update = game_table.update().where(game_table.c.package_name == bindparam('bind_package_name')).values(name=bindparam('name'), description=bindparam('description'), apk_mesg=bindparam('apk_mesg'), game_pic=bindparam('game_pic'), date_update=bindparam('date_update'))

            for each_game in update_list:
                each_game["bind_package_name"] = each_game["package_name"]

            ENGINE.execute(game_update, update_list)

        last_insert_list = []
        for each_game in insert_list:
            if not redis_client.sismember(DONE_SET, each_game["package_name"]):
                redis_client.sadd(DONE_SET,each_game["package_name"])
                last_insert_list.append(each_game)

        if last_insert_list:
            game_table.insert(bind=ENGINE).values(last_insert_list).execute()
