# -*- coding: utf-8 -*-

import scrapy
import sys
from smzdmcloud.items import SmzdmcloudItem


class MySpider(scrapy.spiders.Spider):
    name = "smzdm"
    allowed_domains = []
    start_urls = [
        "http://faxian.smzdm.com/h4s0t0f95c0p1/#filter-block"
    ]

    def parse(self, response):

        reload(sys)
        sys.setdefaultencoding('utf-8')

        for sel in response.xpath('//ul/li'):
            name = sel.xpath('div/h5/a/text()').extract()
            image = sel.xpath('div/div[@class="feed-ver-pic"]/a/img/@src').extract()
            link = sel.xpath('div/div/div/div/div/a/@href').extract()
            worth = sel.xpath('div/div/div/span/a/span/span/text()').extract()

            if len(name) + len(image) + len(link) + len(worth) == 0:
                continue

            item = SmzdmcloudItem()
            item['name'] = name[0].decode('utf-8')
            item['image'] = image[0]
            item['link'] = link[0]
            item['worth'] = int(worth[0])
            yield item
