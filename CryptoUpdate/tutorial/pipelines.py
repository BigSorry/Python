# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import tutorial.StartMarket.getNameToId
import MySQLdb


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class MySqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', '',
                                    'cryptocurrency', charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            query = """INSERT INTO cointoday (`Name_Id`, `Date`, `Market_Cap`,`Market_Cap_Yesterday`, `Gain`) VALUES ('{}', {}, {}, {}, {})""".format(
                spider.nameHash[item["Name"]], item["Date"], item["Market_Cap"], item["Market_Cap_Yesterday"], item["Gain"])
            self.cursor.execute(query)
            self.conn.commit()
        except MySQLdb.Error as e:
            print("Error: ", e)
        return item


