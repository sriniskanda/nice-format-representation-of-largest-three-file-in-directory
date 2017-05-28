# this code is used to find the larget file in directory
import os, glob, sys
import math
from tabulate import tabulate

def byteConv(byteSize):
    if byteSize == 0:
        return "0 B"
    sizeNames = ["B","KB","MB","GB","TB","EB"]
    logPower = math.floor(math.log(byteSize,1024))
    p = math.pow(1024,logPower)
    s = round(byteSize/p,2)
    sizeNamePair = str(s) + " " + sizeNames[logPower]
    return sizeNamePair 


def large_top3_files(dirname):
    allFileSize = []
    for (dirhere, subDir,fileHere) in os.walk(dirname):
        for each_file in fileHere:
            filesize = os.path.getsize(os.path.join(dirhere,each_file))
            allFileSize.append((filesize,each_file,dirhere))
    allFileSize.sort(reverse=True)
    convFile= [(byteConv(i[0]),i[1],i[2]) for i in allFileSize[0:3]]
    return convFile

if __name__ == "__main__":
    p = sys.argv
    #print(type(p))
    top3Filelist = large_top3_files(" ".join(p[1:]))
    print("top three files " + "\n\n")
    print(tabulate((top3Filelist),headers=["File name","Size","Location"]))




