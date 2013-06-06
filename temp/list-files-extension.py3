# -*- coding: utf-8 -*-
# Python 3

# a temp script to find out what extensions are there in a big source code repository
# 2013-05-23

import os
import sys
import shutil
import datetime
import operator
import re

langSuffix = [
".py",
".pl",
".pm",
".perl",
".rb",
".c",
".h",
".java",
".php",
".js",
".css",
".sh",

".json",
".html",

".png",
".jpg",
".gif",
".tiff",

".txt",
".md",
".pdf",

".mustache",

]

inputDir = "/home/xah/Downloads/lang-source-code/"

inputDir = os.path.normpath(inputDir)

for dirPath, subdirList, fileList in os.walk(inputDir):
    for fpath in fileList:
        fullpath = os.path.join( dirPath ,fpath)
        fileName, fileExtension = os.path.splitext(fpath)
        if (fileExtension not in langSuffix) and (not re.search("/\.git/", fullpath)) and (not re.search("/\.svn/", fullpath)):
            print(fullpath)

print("Done.")
