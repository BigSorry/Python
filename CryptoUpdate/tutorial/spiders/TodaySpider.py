import scrapy
import datetime

class TodaySpider(scrapy.Spider):
    name = "TodayCrypto"
    start_urls = [
        'https://coinmarketcap.com/'
    ]

    custom_settings = {
        'ITEM_PIPELINES': {'pipelines.MySqlPipeline': 300}
    }

    def parse(self, response):
        links = response.xpath('//a[@class="currency-name-container link-secondary"]')
        for link in links:
            yield response.follow(link, self.goToHistory)

    def goToHistory(self, response):
        # we always need the 5th element
        li = response.xpath('//ul[@class="nav nav-tabs text-left"]/li')[4]
        # only need first result
        linkHis = li.xpath('a/@href')[0].extract()
        yield response.follow(linkHis, callback = self.getData)

    def getData(self, response):
        # only need yesterday
        row = response.xpath('//tbody/tr')[0]
        items = row.xpath("td/text()")
        coin = {}
        coin['Name'] = response.xpath('//h1[@class="details-panel-item--name"]/img/@alt')[0].extract()
        coin['Date'] = datetime.date.today().strftime("%Y%m%d")
        coin['Market_Cap'] = response.xpath("//span[@data-currency-value = '']/text()")[1].extract()
        coin['Market_Cap'] = int(coin['Market_Cap'].replace(",", ""))
        coin['Market_Cap_Yesterday'] = int(items[6].extract().replace(",", ""))
        coin["Gain"] = ((coin["Market_Cap"] - coin["Market_Cap_Yesterday"]) / coin["Market_Cap_Yesterday"]) * 100
        yield coin


