# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WallStreetJournalItem(scrapy.Item):
    date = scrapy.Field()
    section = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
