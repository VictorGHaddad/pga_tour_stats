# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PgaTourStatsItem(scrapy.Item):
    # define the fields for your item here like:
    ranking = scrapy.Field()
    name = scrapy.Field()
    age = scrapy.Field()
    earnings = scrapy.Field()
    cup = scrapy.Field()
    events = scrapy.Field()
    rounds = scrapy.Field()
    cuts = scrapy.Field()
    top10 = scrapy.Field()
    wins = scrapy.Field()
    score = scrapy.Field()
    ddis = scrapy.Field()
    dacc = scrapy.Field()
    gir = scrapy.Field()
    putts = scrapy.Field()
    sand = scrapy.Field()
    birdies = scrapy.Field()
