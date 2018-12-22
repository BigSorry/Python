from scrapy import cmdline
command = "scrapy crawl crypto -o crawlTest.csv".split()

cmdline.execute(command)

