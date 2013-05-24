#-*- coding: utf-8 -*-
# python 3

# given a input dir, rename unix shell scripts by adding suffix “.sh”, if the shebang line indicates it's shell script

# first, copy them to your own dir, like this
# cp -r --dereference --no-clobber --copy-contents /etc/init.d/ ~/Downloads/lang-source-code/linux-shell-scripts/

# 2013-05-24, Xah Lee

import os
import re

inputDir = "/home/xah/Downloads/lang-source-code/linux-shell-scripts/init.d/"

def renameFile(fpath):
    inputFile = open(fpath)
    firstline = ""
    try:
        firstline = inputFile.readline()
        inputFile.close()
    except UnicodeDecodeError:
        print("skipped, decoding error on: 「{}」".format(inputFile))
        pass

    if re.search("(#!/bin/sh)|(#! /bin/sh)|(#!/bin/bash)", firstline):
        os.rename(fpath, fpath + ".sh")
        print(fpath)
    else:
        print("no {}".format(fpath))

inputDir = os.path.normpath(inputDir)
for dirPath, subdirList, fileList in os.walk(inputDir):
    for fpath in fileList:
        fullpath = os.path.join(dirPath, fpath)
        if os.path.isfile(fullpath):
            renameFile(fullpath)
