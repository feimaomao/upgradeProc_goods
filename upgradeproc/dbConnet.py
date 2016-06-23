# -*- coding: utf-8 -*-
import pnosql

def getSpinfos(table):
	result = pnosql.conn.getspgoods(table)
	return result

def uploadSpinfo(table,spinfo):
	spinfo = pnosql.conn.updataspgood(table, spinfo)
	return spinfo

def getThespinfo(table,x):
	spinfo = pnosql.conn.getthespgoods(table, x)
	return spinfo

def insertTheSpgood(table, spinfo):
	spinfo = pnosql.conn.insertTheSpgood(table, spinfo)
	return spinfo


if __name__ == "__main__":
	print getSpinfo("test2","111")
	uploadSpinfo("test3",{"spcode":"222"})