from scrapy.crawler import CrawlerProcess
from spiders.TodaySpider import *
import MySQLdb

#truncate today coin table before scraping
conn = MySQLdb.connect('localhost', 'root', '',
                                    'cryptocurrency', charset="utf8",
                                    use_unicode=True)
cursor = conn.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("TRUNCATE TABLE cointoday")
cursor.execute("SELECT * FROM coinname ORDER BY Name_Id")
data = cursor.fetchall()
nameToId = {}
for item in data:
    nameToId[item["Name"]] = item["Name_Id"]

def getNameToId(name):
    return nameToId[name]

conn.close()
# web scraping update
process = CrawlerProcess()

process.crawl(TodaySpider(scrapy.Spider), nameHash = nameToId)
process.start() # the script will block here until the crawling is finished




