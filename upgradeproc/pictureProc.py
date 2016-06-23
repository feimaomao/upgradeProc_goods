# -*- coding: utf-8 -*-
import os
from shutil import copy
from PIL import Image
#将处理成功和未成功spcode写入文件successful.csv


sourcePath = "E:\\HGpicture"
targetPath = "D:\\img"


def getTargetPath(spcode,pos,depart,comp,side,picFormat):
    pathSave = "\\{comp}\\{depart}\\{pos}\\{side}".format(comp=comp, depart=depart, pos=pos, side=side)
    path = targetPath + pathSave
    if os.path.exists(path)==False:
        os.makedirs(path)
    pathSave = pathSave + "\\{spcode}.{picFormat}".format(spcode=spcode, picFormat=picFormat)
    path = targetPath+pathSave
    return path,pathSave


def getSourcePath(spcode,pos,picFormat):
    path = sourcePath + "\\{pos}\\{spcode}.{picFormat}".format(pos=pos, spcode=spcode, picFormat=picFormat)
    if os.path.exists(path):
        return path
    else:
        return None


def copyPicture(sourcePicture,targetPicture):
    try:
        copy(sourcePicture,targetPicture)
    except:
        print sourcePicture,targetPicture
    return True

def copyRotatePic(sourcePicture,targetPicture):
    try:
        img = Image.open(sourcePicture)
        angle = 90
        targetImg = img.rotate(angle)
        targetImg.save(targetPicture)
    except:
        print sourcePicture, targetPicture
    return True

def setPicToTargetPic(spcode,pos,depart,comp,side):
    imgPath  ={side:None}
    if side =="0":
        spco = spcode
        imgPath["r"] = None
    else:
        spco = spcode+side

    picFormatList = ["jpg", "JPG", "png", "gif"]
    for picFormat in picFormatList:
        sourcePicture = getSourcePath(spco,pos,picFormat)
        if sourcePicture:
            targetPicture,targetPathSave = getTargetPath(spcode,pos,depart,comp,side,picFormat)
            copyPicture(sourcePicture,targetPicture)
            imgPath[side] = targetPathSave
            if side =="0" and pos=="sp2":
                side = "r"
                targetPicture,targetPathSave  = getTargetPath(spcode, pos, depart,comp,side,picFormat)
                copyRotatePic(sourcePicture,targetPicture)
                imgPath[side] = targetPathSave
            return imgPath
    return imgPath

def setPicute(spcode,depart,comp):
    imgPathdict = {}
    for side in ["0", "b", "d", "c"]:
        setPicToTargetPic(spcode, "upload", depart, comp, side)
        resultPic = setPicToTargetPic(spcode, "sp2", depart, comp, side)
        resultPic["imgPath"] = targetPath
        imgPathdict = dict(imgPathdict, **resultPic)
    return imgPathdict

if __name__ == "__main__":
    print setPicute("1","126","2")
