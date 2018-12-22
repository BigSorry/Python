import scrapy
from ..spiders.Coin import Coin



class QuotesSpider(scrapy.Spider):
    name = "crypto"
    start_urls = [
        'https://coinmarketcap.com/'
    ]

    def parse(self, response):
        links = response.xpath('//a[@class="currency-name-container link-secondary"]')
        for link in links:
            yield response.follow(link, self.goToHistory)


    def goToHistory(self, response):
        # we always need the 5th element
        li = response.xpath('//ul[@class="nav nav-tabs text-left"]/li')[4]
       # dateParam = "?start=20130428&end=20180716"
        # only need first result
        linkHis = li.xpath('a/@href')[0].extract() #+ dateParam
        yield response.follow(linkHis, callback = self.getData)

    def getData(self, response):
        rows = response.xpath('//tbody/tr')
        for row in rows:
            items = row.xpath("td/text()")
            coin = {}
            coin['Name'] = response.xpath('//h1[@class="details-panel-item--name"]/img/@alt').extract()
            coin['Date'] = items[0].extract()
            #coin['Open'] = items[1].extract()
            #coin['High'] = items[2].extract()
            #coin['Low'] = items[3].extract()
            coin['Close'] = items[4].extract()
            coin['Volume'] = items[5].extract()
            coin['Market_Cap'] = items[6].extract()
            yield coin


