from scrapy.crawler import CrawlerProcess
from spiders.quotes_spider import QuotesSpider
from Analysis import *
import os
import MySQLdb as mySQL
import datetime

db = mySQL.connect(host="localhost",
                             user="root",
                             passwd="",
                             db="cryptocurrency")
cursor = db.cursor(mySQL.cursors.DictCursor)
#need second most recent Date for analysis based on day before
cursor.execute("SELECT DISTINCT Date FROM coinfinance ORDER BY Date DESC LIMIT 1")
data = cursor.fetchall()
db.close()
checkDate = data[0]["Date"]
chenkEnd = datetime.date.today()
dayDifference = (chenkEnd - checkDate).days
# no update is needed
if  dayDifference <= 2:
    print("No update needed")

else:
    # web scraping update
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'file:///C:/Users/lexme/PycharmProjects/CryptoUpdate/tutorial/crawlUpdate.csv'
    })

    process.crawl(QuotesSpider(scrapy.Spider), term = checkDate)
    process.start() # the script will block here until the crawling is finished
    #  analysis
    analysis()

    # files are not needed anymore
    path1 = "C:/Users/lexme/PycharmProjects/CryptoUpdate/tutorial/crawlUpdate.csv"
    if os.path.isfile(path1):
        os.remove(path1)
    # else:
    #     print("Error: %s file not found" % path1)
    # path2 = "C:/Users/lexme/PycharmProjects/CryptoUpdate/tutorial/CryptoData.csv"
    # if os.path.isfile(path2):
    #     os.remove(path2)
    # else:
    #     print("Error: %s file not found" % path2)
