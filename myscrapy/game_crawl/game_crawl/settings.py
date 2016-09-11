# -*- coding: utf-8 -*-

# Scrapy settings for game_crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'game_crawl'

SPIDER_MODULES = ['game_crawl.spiders']
NEWSPIDER_MODULE = 'game_crawl.spiders'

AUTOTHROTTLE_ENABLED = True

LOG_FILE = "game_spider.log"

LOG_LEVEL = "ERROR"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'game_crawl (+http://www.yourdomain.com)'
