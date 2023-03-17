from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
 
class MySpider(CrawlSpider):
 
    name = 'dominio.com'
    allowed_domains = ['dominio.com']
    start_urls = ['http://www.example.com']
    rules = (Rule(LxmlLinkExtractor(allow=())))
 
    def parse_item(self, response):
        hxs = Selector(response)
        elemento = Item()
        return elemento