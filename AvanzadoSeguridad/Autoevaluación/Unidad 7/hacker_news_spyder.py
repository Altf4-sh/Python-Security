#!/usr/bin/env python3

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector

class HackerNewsItem(scrapy.Item):
    # define the fields for your item here like
    name = scrapy.xxx()
    link = scrapy.xxx()

class HackerNewsSpyder(xxx):
    name = "hacker_news_spyder"
    allowed_domains = ["xxx"]
    start_urls = ['xxx']
    
    def parse(self, response):
        hxs = Selector(xxx)
        urls = hxs.xxx('//a')
        items=[]
        
        for url in xxx:
            item = xxx()
            item['name'] = url.xxx('text()').xxx()
            item['link'] = url.xxx('@href').xxx()
            if(item['link'].xxx("http")):
                items.xxx(item)

        return xxx    
