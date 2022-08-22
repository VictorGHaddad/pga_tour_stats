## get data from https://www.espn.com/golf/stats/player

import scrapy
from pga_tour_stats.items import PgaTourStatsItem
from scrapy.loader import ItemLoader


class PlayersSpider(scrapy.Spider):
    name = 'players'
    allowed_domains = ['www.espn.com']
    start_urls = ['https://www.espn.com/golf/stats/player']

    def parse(self, response):
        # get data from table
        table = response.xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div[1]')
        # get data from table rows
        rows = table.xpath('.//tr')
        # iterate through rows
        for row in rows:
            # create loader for each row
            loader = ItemLoader(item=PgaTourStatsItem(), selector=row)
            # get ranking
            loader.add_xpath('ranking', './/td[1]/text()')
            # get name
            loader.add_xpath('name', './/td[2]/div/a/text()')
            # get age
            loader.add_xpath('age', './/td[3]/div/text()')
            # get earnings
            loader.add_xpath('earnings', './/td[1]/text()')
            # get cup
            loader.add_xpath('cup', './/td[2]/text()')
            # get events
            loader.add_xpath('events', './/td[3]/text()')
            # get rounds
            loader.add_xpath('rounds', './/td[4]/text()')
            # get cuts
            loader.add_xpath('cuts', './/td[5]/text()')
            # get top10
            loader.add_xpath('top10', './/td[6]/text()')
            # get wins
            loader.add_xpath('wins', './/td[7]/text()')
            # get score
            loader.add_xpath('score', './/td[8]/text()')
            # get ddis
            loader.add_xpath('ddis', './/td[9]/text()')
            # get dacc
            loader.add_xpath('dacc', './/td[10]/text()')
            # get gir
            loader.add_xpath('gir', './/td[11]/text()')
            # get putts
            loader.add_xpath('putts', './/td[12]/text()')
            # get sand
            loader.add_xpath('sand', './/td[13]/text()')
            # get birdies
            loader.add_xpath('birdies', './/td[14]/text()')
            # yield loader.load_item()
            yield loader.load_item()

        