# -*- coding: utf-8 -*-
from dbConnet import uploadSpinfo

def setSourcSpToTargetSp(depart,comp,table,targetPicture,spinfo):
    targetSpinfo = setSpinfo(depart, comp, targetPicture,spinfo)
    uploadSpinfo(table, targetSpinfo)
    return targetSpinfo

# 设置写入数据
def setSpinfo(depart,comp,targetPicture,sourceSpinfo):
    #sourceSpinfo = {"_id": ,"comp": ,"spcode": ,"barcode": ,"spname": ,"height": , "width": ,"thickness": ,"format"; ,"paraentcomp": ,}
        sourceSpinfo["operator"] = str(depart)
        sourceSpinfo["depart"] = str(depart)
        sourceSpinfo["comp"] =  str(comp)
        sourceSpinfo["upload"] = 1
        sourceSpinfo["imgPath"] = targetPicture
        return sourceSpinfo

if __name__ == "__main__":
    print setSourcSpToTargetSp("126","2","test",{'0': '\\2\\126\\sp2\\0\\000911.jpg', 'c': '\\2\\126\\sp2\\c\\000911.jpg', 'r': '\\2\\126\\sp2\\r\\000911.jpg','d': '\\2\\126\\sp2\\d\\000911.jpg', 'b': '\\2\\126\\sp2\\b\\000911.jpg', 'imgDir': 'D:\\img'},{u'spcode': u'02134141111212', u'spname': u'C\u6d3b\u6027\u4e73\u9178\u83cc\u996e\u54c1\u539f\u5473Test', u'barcode': u'9851235122', u'thickness': 801, u'height': 233, u'width': 80,  u'spformat': u'', u'_id': u'3cdd199e-3087-11e6-9d74-b7163d1bcb85'})
