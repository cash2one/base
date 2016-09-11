
# -*- coding: utf-8 -*-
import scrapy

from urllib import quote

from models import *

import json

from datetime import datetime

origin_game_list = [each[0] for each in select([game_table.c.package_name],bind=ENGINE).execute().fetchall()]

pipe_line = redis_client.pipeline()
for each_game in origin_game_list:
    pipe_line.sadd(DONE_SET, each_game)
pipe_line.execute()

class WDJSpider(scrapy.Spider):

    tags = [
            '休闲时间','切东西','找茬','减压','宠物','答题','音乐节奏','益智','解谜','宝石消除','方块',
            '宝石','连连看','祖玛','泡泡龙','卡通','动作射击','横版','射击','3D','飞行','坦克','狙击',
            '儿童益智','拼图','识字','智力开发','数学','体育格斗','街机','篮球','足球','网球','台球',
            '其他球类','经营策略','纸牌','战棋','经营','历史','战争','DOTA','跑酷竞速','跑酷','赛车',
            '摩托','赛艇','飞机','网络游戏','RPG','动作竞技','策略','卡牌','经营模拟','扑克棋牌','斗地主',
            '棋类','麻将','桌游','德州扑克','塔防守卫','闯关','抢滩登陆','角色扮演','回合制','即时战斗',
            '养成','武侠','魔幻','动漫','三国','修仙'
        ]

    wdj_url = "http://apps.wandoujia.com/api/v1/apps?ads_count=0&tag=%s&max=60&start={}&opt_fields=apps.likesCount,apps.reason,apps.ad,apps.title,apps.packageName,apps.apks.size,apps.icons.px68,apps.apks.superior,apps.installedCountStr,apps.description,apps.apks.versionCode"

    def get_wdj_urls(wdj_url, tags):
        re_urls = []
        for each_url in [wdj_url%quote(each_tag) for each_tag in tags]:
            for each_index in xrange(0, 1000, 60):
                re_urls.append(each_url.format(each_index))
        return re_urls

    name = "wdj"
    allowed_domains = ["wandoujia.com"]
    start_urls = (
        get_wdj_urls(wdj_url, tags)
    )

    def parse(self, response):
        update_list = []
        insert_list = []

        game_list = []
        for each_game in json.loads(response.body)[0]["apps"]:
            try:
                if not each_game["packageName"]:
                    continue

                pic_small = each_game["icons"]["px68"]
                pic_big = pic_small.replace("68_68.png","256_256.png")

                game_list.append({"package_name":each_game["packageName"],"name":each_game["title"],"description":each_game["description"],"apk_mesg":json.dumps(each_game["apks"]),"game_pic":pic_big,"date_update":datetime.now()})

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
