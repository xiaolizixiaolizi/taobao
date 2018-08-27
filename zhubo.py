# -*- coding: utf-8 -*-
import scrapy
import json
import re
from  ..items import  TaobaoItem

class ZhuboSpider(scrapy.Spider):
    name = 'zhubo'
    allowed_domains = ['v.taobao.com']
    start_urls = ['https://v.taobao.com/v/content/live?catetype=704&from=taonvlang']

    def start_requests(self):
        base_url='https://v.taobao.com/micromission/req/selectCreatorV3.do?cateType=704&currentPage={}&callback=jsonp116&&_output_charset=UTF-8&_input_charset=UTF-8'

        urls= [base_url.format(str(i)) for i in range(1,26)]
        for url in urls:
            request = scrapy.Request(
                url=url,
                callback=self.parse
            )
            yield request

    def parse(self, response):
        infos=response.text
        infos=re.search(r'({"result":.*}),totalCounts500',infos).group(1)
        # infos=re.search(r'"result":(.*),"totalCounts"',infos).group(1)
        # print(infos)

        infos=json.loads(infos)
        results=infos['result']

        for result in results:
            fansCount=result['fansCount']
            nick = result['nick']
            userId = result['userId']
            titleArray = result['titleArray']
            array = list()
            for titlearray in titleArray:
                array.append(titlearray['value'])
            if len(array) > 5:
                task_num, completion_rate, service_rate, field, agent, producer = array
            else:
                task_num, completion_rate, service_rate, field, producer = array
                agent=None
            item=TaobaoItem(nick=nick,fansCount=fansCount,userId=userId,task_num=task_num,
                            completion_rate=completion_rate,service_rate=service_rate,field=field,agent=agent,producer=producer)


            yield  item





