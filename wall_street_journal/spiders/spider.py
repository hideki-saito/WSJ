# -*- encoding: utf-8 -*-

import scrapy
from scrapy.spider import BaseSpider

from wall_street_journal.items import WallStreetJournalItem

class WSJ_Spider(BaseSpider):
    name = "spider"
   #allowed_domains = ["dmoz.org"]
    start_urls = []
    pageNo = 675
    for i in range(1, pageNo+1):
        url = "http://www.wsj.com/search/term.html?KEYWORDS=&min-date=2016/01/01&max-date=2016/12/31&page=" + str(i) + "&isAdvanced=true&daysback=90d&andor=AND&sort=date-asc&source=wsjarticle"
        start_urls.append(url)
#    start_urls.reverse()

    def  make_requests_from_url(self, url):
        return scrapy.Request(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'})

    def parse(self, response):
        host = "http://www.wsj.com"
        sels = response.xpath('//ul[@class="items hedSumm"]/li')
        print len(sels)
        for sel in response.xpath('//ul[@class="items hedSumm"]/li'):
            print sel
            item = WallStreetJournalItem()
            item['date'] = sel.xpath('descendant::time/text()').extract()[0]
            try:
                item['section'] = sel.xpath('descendant::li/a/text()').extract()[0]
            except Exception:
                item['section'] = ""
            item['title'] = sel.xpath('descendant::h3/a/text()').extract()[0]
            item['url'] = host + sel.xpath('descendant::h3/a/@href').extract()[0]
            yield item