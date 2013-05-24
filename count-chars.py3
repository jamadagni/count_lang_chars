# -*- coding: utf-8 -*-
# Python 3

# count the number of occurance of each char in lang source code.
# this is to gather statistics on char frequency for each lang.
# See 〈ErgoEmacs Keyboard〉 http://xahlee.info/comp/ultimate_keyboard_layout.html

# author: Xah Lee http://xahlee.org/
# created date: 2013-05-23

# TODO
# • all file are read in as utf-8. If error, skip. Seems too much trouble to find out file encoding first.
# • The result needs to be normalized. For example, if there's a lot C code, C's use of punct chars will screw the stat.
# • find a  normalization scheme. Maybe based on total num of lines of code, or total file size, or total use of all punc chars. Also, might consider language popularity. For example, C is heavily used, but not tcl. So, when doing normalization, C should have a bigger room.
# • pretty print, in a somewhat matrix format as a report
# • print out to html table.

import os
import sys
import shutil
import datetime
import operator
import re

#print(sys.path)

# if this list is not empty, then only these files will be processed.
# for quick testing purposes.
file_list = [
#r"/home/xah/git/count_lang_chars/countCharStat.py3"
]

# list of dirs to process. All files in these dir will be counted.
input_dirs = [

#     # python
     "/usr/lib/python3.2/",
#     "/home/xah/Downloads/lang-source-code/django/",

#     # perl
      "/usr/lib/perl5",
#      "/usr/lib/perl/5.14",
#      "/usr/share/perl5",
#      "/usr/share/perl/5.14",

#     # ruby
     "/usr/lib/ruby/1.9.1/",
#     "/home/xah/Downloads/lang-source-code/rails",

#     # JavaScript
#      "/home/xah/Downloads/lang-source-code/angular.js",
#     "/home/xah/Downloads/lang-source-code/backbone",
#     "/home/xah/Downloads/lang-source-code/dijit/",
#     "/home/xah/Downloads/lang-source-code/dojo/",
#     "/home/xah/Downloads/lang-source-code/jquery-1.9.1.js",
#     "/home/xah/Downloads/lang-source-code/prototype",
# #    "/home/xah/Downloads/lang-source-code/yui3",

#     # C
#     "/home/xah/Downloads/lang-source-code/git",
#     "/home/xah/Downloads/lang-source-code/node",
#     # "/home/xah/Downloads/lang-source-code/linux",
#     "/home/xah/bin/emacs-24.3/src/",

#     # Java
#      "/home/xah/Downloads/lang-source-code/google-web-toolkit-read-only",

#     # PHP
#      "/home/xah/Downloads/lang-source-code/Symfony",

#     # bash
#     "/home/xah/Downloads/lang-source-code/linux-shell-scripts/"

]

#######################################

# only files with these extensions are counted
langExtMap = {
".py": "python",
".pl": "perl",
".pm": "perl",
".perl": "perl",
".rb": "ruby",
".c": "c",
".h": "c",
".cpp": "c++",
".cc": "c++",
".java": "java",
".php": "php",
".js": "javascript",
".css": "css",
".sh": "bash",
#".sql": "sql",
#".html": "html",
#".xml": "xml",
}

langExtList = langExtMap.keys()

# structure is: {'python': {}, 'c': {}, 'java': {}, 'perl': {}, …}
# in each hash, key is a char, value is count
charData = {}
# init charData
for lExt,lName in langExtMap.items():
    charData[lName] = {
        "(":0,
        ")":0,
        "{":0,
        "}":0,
        "[":0,
        "]":0,
        "!":0,
        '"':0,
        "'":0,
        ",":0,
        "-":0,
        ".":0,
        ":":0,
        ";":0,
        "*":0,
        "+":0,
        "=":0,
        "<":0,
        ">":0,
        "?":0,
        "@":0,
        "/":0,
        "\\":0,
        "^":0,
        "_":0,
        "`":0,
        "|":0,
        "~":0,
        "#":0,
        "$":0,
        "%":0,
        "&":0,
    }

# structure is: {'python': ‹total char count›, 'c': ‹total char count›, …}
charTotalData = {}
# charTotalData
for lExt,lName in langExtMap.items():
    charTotalData[lName] = 0

# list of tuples. Each tuples is (lange name, count). Sorted by count. Highest count first.
sortedTotalCharList = []

# sum of all chars counts in all langs
charSumTotal = 0

# total num of files
totalFileCount = 0



def countThisFile(fpath):
    "add char count to charData"
#    print("reading:{}".format(fpath))

    inputFile = open(fpath)
    fileContent = ""
    try:
        fileContent = inputFile.read()
        inputFile.close()
    except UnicodeDecodeError:
        print("skipped, decoding error on: 「{}」".format(inputFile))
        pass

    global totalFileCount
    totalFileCount += 1
    langName = langExtMap[(os.path.splitext(fpath))[1]]
    for thisChar in fileContent:
        if thisChar in charData[langName]:
            charData[langName][thisChar] += 1

# langName is a string in langExtMap
# hashTable is a element in charData. Key is a char, value is a integer.
def prettyPrint(langName, hashTable):
    if (charTotalData[langName] == 0):
        pass
    else:
        sortedChars = sorted(hashTable.items(), key=operator.itemgetter(1), reverse=True)
        print("lang: {}, total:{:,}".format(langName, charTotalData[langName] ))
        for charr, cnt in sortedChars:
            print(" {}  {:.1%}".format(charr, cnt/float(charTotalData[thisLang]) ))
        print("\n")

#────────── ────────── ────────── ────────── ──────────
# main

# if file_list has element, just count those files. Else, all files in input_dirs
if (len(file_list) != 0):
   for fpath in file_list:
       fileName, fileExtension = os.path.splitext(fpath)
       if fileExtension in langExtList:
           countThisFile(os.path.normpath(fpath) )
else:
    for inputDir in input_dirs:
        inputDir = os.path.normpath(inputDir)
        for dirPath, subdirList, fileList in os.walk(inputDir):
            for fpath in fileList:
                fileName, fileExtension = os.path.splitext(fpath)
                if (fileExtension in langExtList):
                    fullpath = os.path.join(dirPath, fpath)
                    if os.path.isfile(fullpath) and (not os.path.islink(fullpath)):
                        countThisFile(fullpath)

#print( "charData ", charData)

charDataCombined = {}
for thisLang, thisLangCharData in charData.items():
    charTotalData[thisLang] = sum(thisLangCharData.values()) # compute total
    for thisChar, thisCount in thisLangCharData.items():
        if thisChar in charDataCombined:
            charDataCombined[thisChar] += thisCount
        else:
            charDataCombined[thisChar] = thisCount
#print("charDataCombined", charDataCombined)

charSumTotal = sum(charTotalData.values())

sortedTotalCharList = sorted(charTotalData.items(), key=operator.itemgetter(1), reverse=True)

######################################

print("\n")

# print overall summery
print("Total num of files processed: {:,}".format(totalFileCount))
print("Total num of punc chars counted: {:,}".format(charSumTotal))
for lname, cnt in sortedTotalCharList:
    print("{:.1%} {} ".format(cnt/float(charSumTotal), lname))
print("{}\n".format(sortedTotalCharList))

# print all lang's combined stat
sortedChars = sorted(charDataCombined.items(), key=operator.itemgetter(1), reverse=True)
print("All Languages")
for charr, cnt in sortedChars:
    print(" {}  {:.1%}".format(charr, cnt/float(charSumTotal) ))
print("\n")

# print each lang's stat
for thisLang, thisLangCharData in charData.items():
    prettyPrint(thisLang, thisLangCharData)

# (0 if (charTotalData[langName] == 0) else (charTotalData[langName]/float(charSumTotal)) )
