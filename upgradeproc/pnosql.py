# -*- coding: utf-8 -*-
from pymongo import MongoClient

class nosql:    
    def __init__(self,host, port, db):#主机地址，端口，数据库名称
        self.conn = MongoClient(host= host, port=port)
        self.db = self.conn[db]#连接指定数据库

    def getthespgoods(self,table,x):
        spdata = self.db[table].find_one(x)
        return spdata


    def insertTheSpgood(self,table,spinfo):
        spdata = self.db[table].insert(spinfo)
        return spdata


    def getspgoods(self,table):
        spdata = self.db[table].find()
        return spdata

    def updataspgood(self, col,spinfo):
        self.db[col].update({"_id": spinfo["_id"]},spinfo)
        return True

conn = nosql('localhost', 27017, 'goods')

if __name__ == "__main__":
    for spinfo in conn.getspgoods("spgoods_4"):
        print spinfo
    # print conn.getthespgood("test2",{"spcode":"111"})
