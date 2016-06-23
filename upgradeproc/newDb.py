# -*- coding: utf-8 -*-t
import xlrd
from dbConnet import getThespinfo,insertTheSpgood
from sourceSpinfoToTargetSpinfo import targetTable


def newDbFind():
    spinfo = xlrd.open_workbook('dispose.xlsx')
    sh = spinfo.sheet_by_index(0)#返回第几页的对象
    spcodeList =  sh.col_values(0)
    for spcode in spcodeList:
            spinfo = getThespinfo("spgoods",{"spcode":spcode})
            if spinfo:
                insertTheSpgood(targetTable,spinfo)
            else:
                print spcode


if __name__ =="__main__":
    newDbFind()