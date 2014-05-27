# -*- coding: utf-8 -*-
# Python 3

# count the number of occurance of each char in lang source code. this is to gather statistics on char frequency for each lang. See

# Computer Languages Character Distribution
# http://xahlee.info/comp/computer_language_char_distribution.html

# Xah Keyboard
# http://xahlee.info/comp/ultimate_keyboard_layout.html

# author: Xah Lee http://xahlee.org/
# created date: 2013-05-23

# TODO
# • all file are read in as utf-8. If error, skip. Seems too much trouble to find out file encoding first.


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
    "/usr/share/perl5",
    "/usr/lib/perl/5.14",
    # "/usr/share/perl/5.14",

     # ruby
     "/usr/lib/ruby/1.9.1/",
     "/home/xah/Downloads/lang-source-code/rails",

       # JavaScript
    "/home/xahDownloads/lang-source-code/yui/",
    "/home/xah/Downloads/lang-source-code/angular",
    "/home/xah/Downloads/lang-source-code/dojo",
    "/home/xah/Downloads/lang-source-code/prototype",
    "/home/xah/Downloads/lang-source-code/backbone",
    "/home/xah/Downloads/lang-source-code/jquery-1.9.1/",

# #     C
# #     lang: c, total:72,987,569;
# #     lang: python, total:23,045;
# #     lang: c++, total:7,892;
# #     lang: perl, total:99,459;
# #     lang: bash, total:18,060
#     "/home/xah/Downloads/lang-source-code/linux",

#     lang: c, total:822,437;
#     lang: python, total:24,988;
#     lang: javascript, total:8,340;
#     lang: perl, total:216,493;
#     lang: bash, total:559,899;
#     lang: php, total:1,158;
#     lang: css, total:2,307
     "/home/xah/Downloads/lang-source-code/git",

# lang: c, total:1,339,141
     "/home/xah/apps/emacs-24.3/src/",

#  lang: c++, total:5,209,059;
#  lang: c, total:3,124,259;
#  lang: python, total:405,890;
#  lang: javascript, total:2,121,674;
#  lang: perl, total:491,182;
#  lang: bash, total:24,445;
#  lang: ruby, total:380;
#  lang: css, total:5,060
  # "/home/xah/Downloads/lang-source-code/node",

    # c++
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/accumulators",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/algorithm",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/archive",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/asio",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/assign",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/atomic",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/bimap",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/bind",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/chrono",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/circular_buffer",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/compatibility",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/concept",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/concept_check",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/config",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/container",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/context",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/coroutine",
"/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/date_time",
 "/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/detail",
 "/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/dynamic_bitset",
 "/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/exception",
 "/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/filesystem",
 "/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/flyweight",
 "/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/format",
 "/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/function",
 "/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/functional",

# "/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/function_types",
# "/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/fusion",
# "/home/xah/Downloads/lang-source-code/boost_1_55_0/boost/geometry",

#     Java
#     lang: java, total:4,106,030;
#     lang: c, total:4,990;
#     lang: python, total:36,669;
#     lang: javascript, total:18,185;
#     lang: c++, total:14,472;
#     lang: bash, total:1,347;
#     lang: css, total:43,472
     # "/home/xah/Downloads/lang-source-code/google-web-toolkit-read-only",
     "/home/xah/Downloads/lang-source-code/google-web-toolkit-read-only/dev",
     "/home/xah/Downloads/lang-source-code/google-web-toolkit-read-only/tools",
     "/home/xah/Downloads/lang-source-code/google-web-toolkit-read-only/build_tools",
     "/home/xah/Downloads/lang-source-code/google-web-toolkit-read-only/elemental",

    # "/home/xah/Downloads/lang-source-code/gwt",

        # PHP
#       lang: php, total:1,845,508;
#       lang: c, total:6,069;
#       lang: bash, total:755;
#       lang: css, total:4,352
       "/home/xah/Downloads/lang-source-code/Symfony",

        # bash
       "/home/xah/Downloads/lang-source-code/linux-shell-scripts/",

]

# only files with these extensions are counted
lang_suffix_map = {
".py": "Python",
".pl": "Perl",
".pm": "Perl",
".perl": "Perl",
".rb": "Ruby",
".c": "C",
".h": "C",
".hpp": "C++",
".cpp": "C++",
".cc": "C++",
".java": "Java",
".php": "PHP",
".js": "JavaScript",
".css": "CSS",
".sh": "BASH",
".el": "Emacs Lisp",
#".sql": "SQL",
#".html": "HTML",
#".xml": "XML",
}


import os
import sys
import shutil
import datetime
import operator
import re
import json
import pprint



# char_data is the primary data
# structure is: {'python': {}, 'c': {}, 'java': {}, 'perl': {}, …}
# in each hash, key is a char, value is count
char_data = {}

# init char_data
for lang_ext,lang_name in lang_suffix_map.items():
    char_data[lang_name] = {
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

        "0":0,
        "1":0,
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
        "7":0,
        "8":0,
        "9":0,

    }

# key is a char, value is count
print_debug = False

# key is a char, value is count
all_langs_char_data_merged = {}

# structure is: {'python': ‹total char count›, 'c': ‹total char count›, …}
all_langs_char_count = {}

# init all_langs_char_count
for lang_ext,lang_name in lang_suffix_map.items():
    all_langs_char_count[lang_name] = 0

# sum of all chars counts in all langs
char_sum_total = 0

# total num of files
num_of_file_processed = 0



def count_this_file(fpath):
    "add char count to char_data"
    # print("reading:{}".format(fpath))

    inputFile = open(fpath)
    fileContent = ""
    try:
        fileContent = inputFile.read()
        inputFile.close()
    except UnicodeDecodeError:
        if print_debug:
            print("skipped, decoding error on: 「{}」".format(inputFile))
        pass

    global num_of_file_processed
    num_of_file_processed += 1

    langName = lang_suffix_map[(os.path.splitext(fpath))[1]]
    for thisChar in fileContent:
        if thisChar in char_data[langName]:
            char_data[langName][thisChar] += 1

# langName is a string in lang_suffix_map
# hashTable is a element in char_data. Key is a char, value is a integer.
def pretty_print(langName, hashTable):
    if (all_langs_char_count[langName] == 0):
        pass
    else:
        sortedChars = sorted(hashTable.items(), key=operator.itemgetter(1), reverse=True)
        print("lang: {}, total:{:,}".format(langName, all_langs_char_count[langName] ))
        for charr, cnt in sortedChars:
            print(" {}  {:.1%}".format(charr, cnt/float(all_langs_char_count[thisLang]) ))
        print("\n")

def compute_merged_char_data(char_data):
    merged_data = {}
    for thisLang, thisLangCharData in char_data.items():
        for thisChar, thisCount in thisLangCharData.items():
            if thisChar in merged_data:
                merged_data[thisChar] += thisCount
            else:
                merged_data[thisChar] = thisCount
    return merged_data;

def compute_langs_char_counts():
    for thisLang, thisLangCharData in char_data.items():
        all_langs_char_count[thisLang] = sum(thisLangCharData.values()) # compute total


# main

# if file_list has element, just count those files. Else, all files in input_dirs
if (len(file_list) != 0):
   for fpath in file_list:
       fileName, fileExtension = os.path.splitext(fpath)
       if fileExtension in lang_suffix_map:
           count_this_file(os.path.normpath(fpath) )
else:
    for inputDir in input_dirs:
        inputDir = os.path.normpath(inputDir)
        for dirPath, subdirList, fileList in os.walk(inputDir):
            for fpath in fileList:
                fileName, fileExtension = os.path.splitext(fpath)
                if (fileExtension in lang_suffix_map):
                    fullpath = os.path.join(dirPath, fpath)
                    if os.path.isfile(fullpath) and (not os.path.islink(fullpath)):
                        count_this_file(fullpath)

all_langs_char_data_merged = compute_merged_char_data(char_data)

compute_langs_char_counts()

char_sum_total = sum(all_langs_char_count.values())


# print

print("\n")

# print overall summery
print("Total num of files processed: {:,}".format(num_of_file_processed))
print("Total num of punc chars counted: {:,}".format(char_sum_total))

sorted_lang_char_total = sorted(all_langs_char_count.items(), key=operator.itemgetter(1), reverse=True)
for lname, cnt in sorted_lang_char_total:
    print("{:.1%} {} ".format(cnt/float(char_sum_total), lname))

print(json.dumps (sorted_lang_char_total))

print("\n")

# print all lang's combined stat
sortedChars = sorted(all_langs_char_data_merged.items(), key=operator.itemgetter(1), reverse=True)
print("All Languages")
for charr, cnt in sortedChars:
    print(" {}  {:.1%}".format(charr, cnt/float(char_sum_total) ))
print("\n")

print(json.dumps (sortedChars))
print("\n")

# print each lang's stat
for thisLang, thisLangCharData in char_data.items():
    pretty_print(thisLang, thisLangCharData)

print(json.dumps (char_data))
