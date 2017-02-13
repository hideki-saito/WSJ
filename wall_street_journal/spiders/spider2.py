# -*- encoding: utf-8 -*-

import scrapy
from scrapy.spider import BaseSpider

from wall_street_journal.items import WallStreetJournalItem

class WSJ_Spider(BaseSpider):
    name = "spider2"
   #allowed_domains = ["dmoz.org"]
    start_urls = ['https://3000030000.net/user/index_player.php']

    # def  make_requests_from_url(self, url):
    #     return scrapy.Request(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'})

    def start_requests(self):
        cf_requests = []
        for url in self.start_urls:
            token, agent = cfscrape.get_tokens(url, USER_AGENT)
            #token, agent = cfscrape.get_tokens(url)
            cf_requests.append(scrapy.Request(url=url, cookies={'__cfduid': token['__cfduid']}, headers={'User-Agent': agent}))
            print "useragent in cfrequest: " , agent
            print "token in cfrequest: ", token
        return cf_requests

    def parse(self, response):
        pass
        # host = "http://www.wsj.com"
        # sels = response.xpath('//ul[@class="items hedSumm"]/li')
        # print len(sels)
        # for sel in response.xpath('//ul[@class="items hedSumm"]/li'):
        #     print sel
        #     item = WallStreetJournalItem()
        #     item['date'] = sel.xpath('descendant::time/text()').extract()[0]
        #     try:
        #         item['section'] = sel.xpath('descendant::li/a/text()').extract()[0]
        #     except Exception:
        #         item['section'] = ""
        #     item['title'] = sel.xpath('descendant::h3/a/text()').extract()[0]
        #     item['url'] = host + sel.xpath('descendant::h3/a/@href').extract()[0]
        #     yield item