import time
import scrapy
from tut.items import CnblogsItem
class AuthorSpider(scrapy.Spider):
    name = 'rmrb'
    i = 'nbs.D110000renmrb_01.htm'
    j=time.strftime("%Y-%m/%d/")
    t='http://paper.people.com.cn/rmrb/html/'+j+i
    start_urls = [t]

    def parse(self, response):
        # follow links to author pages
        for href in response.css('li a[href^="nw"]::attr(href)').extract():
            yield response.follow(href, self.parse_author)


        for href in response.css('div.right_title-name a#pageLink::attr(href)').extract():
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        item = CnblogsItem()
        item['number'] = response.css('meta[name=author]::attr(content)').extract()
        item['title'] = response.css('title::text').extract()
        item['img'] = response.css('TABLE.pci_c IMG::attr(src)').extract()
        item['imgtext'] = response.css('TABLE.pci_c P::text').extract()
        item['text'] = response.css('div#ozoom p::text').extract()
        return item
