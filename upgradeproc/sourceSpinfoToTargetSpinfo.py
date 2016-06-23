# -*- coding: utf-8 -*-
from spProc import setSourcSpToTargetSp
from dbConnet import getSpinfos
from pictureProc import setPicute
depart = "131"
comp = "4"
targetTable = "spgoods_"+comp


def sourceSpToTargetSp(targetTable,depart,comp):
	resultList = []
	for spinfo in getSpinfos(targetTable):
		imgPathdict = setPicute(spinfo["spcode"],depart,comp)
# {'0': '\\2\\126\\sp2\\0\\000911.jpg', 'c': '\\2\\126\\sp2\\c\\000911.jpg', 'r': '\\2\\126\\sp2\\r\\000911.jpg','d': '\\2\\126\\sp2\\d\\000911.jpg', 'b': '\\2\\126\\sp2\\b\\000911.jpg', 'imgPath': 'D:\\img'}
		result = setSourcSpToTargetSp( depart, comp,targetTable, imgPathdict, spinfo)
		resultList.append(result)
	return resultList

if __name__ =="__main__":
	resultList = sourceSpToTargetSp(targetTable,depart,comp)








# if __name__=="__main__":
# 	# sourceSpToTargetSp(["001",])
# 	resultList = sourceSpToTargetSp(spcodeList)
# 	with open('result.csv', 'wb') as csvfile:
# 		spamwriter = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
# 		for result in resultList:
# 			spamwriter.writerow([result])
# 	sourceSpToTargetSp(["111","000911","01"])