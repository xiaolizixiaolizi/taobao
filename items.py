# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):

    nick=scrapy.Field()
    fansCount=scrapy.Field()
    userId=scrapy.Field()
    task_num=scrapy.Field()
    completion_rate=scrapy.Field()
    service_rate=scrapy.Field()
    agent=scrapy.Field()
    producer=scrapy.Field()
    field=scrapy.Field()

