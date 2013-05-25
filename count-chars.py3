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


# config

# if this list is not empty, then only these files will be processed.
# for quick testing purposes.
file_list = [

]

# list of dirs to process. All files in these dir will be counted.
input_dirs = [

      # python
    "/usr/lib/python3.2/",
    "/home/xah/Downloads/lang-source-code/django/",

      # perl
     "/usr/lib/perl5",
     "/usr/lib/perl/5.14",
     "/usr/share/perl5",
     "/usr/share/perl/5.14",

    # #  # ruby
      "/usr/lib/ruby/1.9.1/",
      "/home/xah/Downloads/lang-source-code/rails",

      # JavaScript
#      "/home/xah/Downloads/lang-source-code/yui3", # lang: javascript, total:8,821,561 ;  lang: css, total:104,421; lang: php, total:1,846 ;
    "/home/xah/Downloads/lang-source-code/angular.js", # javascript, total:842,260
      "/home/xah/Downloads/lang-source-code/dojo/", # lang: javascript, total:534,967
      "/home/xah/Downloads/lang-source-code/dijit/", # lang: javascript, total:219,828
      "/home/xah/Downloads/lang-source-code/prototype", # lang: javascript, total:129,838
      "/home/xah/Downloads/lang-source-code/backbone", # lang: javascript, total:95,989
    "/home/xah/Downloads/lang-source-code/jquery-1.9.1/", # lang: javascript, total:39,089

       # C
#     "/home/xah/Downloads/lang-source-code/linux", # lang: c, total:72,987,569; lang: python, total:23,045; lang: c++, total:7,892; lang: perl, total:99,459; lang: bash, total:18,060

      "/home/xah/Downloads/lang-source-code/node", # lang: c, total:3,124,259; lang: python, total:405,890; lang: javascript, total:2,121,674; lang: c++, total:5,209,059; lang: perl, total:491,182; lang: bash, total:24,445; lang: ruby, total:380; lang: css, total:5,060

#      "/home/xah/bin/emacs-24.3/src/", # lang: c, total:1,339,141

      "/home/xah/Downloads/lang-source-code/git", # lang: c, total:822,437; lang: python, total:24,988; lang: javascript, total:8,340; lang: perl, total:216,493; lang: bash, total:559,899; lang: php, total:1,158; lang: css, total:2,307

       # Java
      "/home/xah/Downloads/lang-source-code/google-web-toolkit-read-only", # lang: java, total:4,106,030; lang: c, total:4,990; lang: python, total:36,669; lang: javascript, total:18,185; lang: c++, total:14,472; lang: bash, total:1,347; lang: css, total:43,472

       # PHP
      "/home/xah/Downloads/lang-source-code/Symfony", # lang: php, total:1,845,508; lang: c, total:6,069; lang: bash, total:755; lang: css, total:4,352

       # bash
      "/home/xah/Downloads/lang-source-code/linux-shell-scripts/"

]

# only files with these extensions are counted
langSuffixMap = {
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


import os
import sys
import shutil
import datetime
import operator
import re



langExtList = langSuffixMap.keys()

# structure is: {'python': {}, 'c': {}, 'java': {}, 'perl': {}, …}
# in each hash, key is a char, value is count
charData = {}

# init charData
for lExt,lName in langSuffixMap.items():
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

# key is a char, value is count
charDataCombined = {}

# structure is: {'python': ‹total char count›, 'c': ‹total char count›, …}
charTotalData = {}

# init charTotalData
for lExt,lName in langSuffixMap.items():
    charTotalData[lName] = 0

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
    langName = langSuffixMap[(os.path.splitext(fpath))[1]]
    for thisChar in fileContent:
        if thisChar in charData[langName]:
            charData[langName][thisChar] += 1

# langName is a string in langSuffixMap
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


# print

print("\n")

# print overall summery
print("Total num of files processed: {:,}".format(totalFileCount))
print("Total num of punc chars counted: {:,}".format(charSumTotal))
sortedLangCharTotal = sorted(charTotalData.items(), key=operator.itemgetter(1), reverse=True)
for lname, cnt in sortedLangCharTotal:
    print("{:.1%} {} ".format(cnt/float(charSumTotal), lname))
print("{}\n".format(sortedLangCharTotal))

# print all lang's combined stat
sortedChars = sorted(charDataCombined.items(), key=operator.itemgetter(1), reverse=True)
print("All Languages")
for charr, cnt in sortedChars:
    print(" {}  {:.1%}".format(charr, cnt/float(charSumTotal) ))
print("\n")

# print each lang's stat
for thisLang, thisLangCharData in charData.items():
    prettyPrint(thisLang, thisLangCharData)

