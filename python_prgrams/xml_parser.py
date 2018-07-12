#!/usr/bin/python
import os
import string
import glob
import libxml2
from xpath_my import *

os.chdir("/templates")
print (os.getcwd())
#list the files in directory
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("/templates") if isfile(join("/templates", f))]
file_path = "/templates"
###print (file_path)
aList = list(onlyfiles) # created the list of file avaliable in directory
tuple1=tuple(aList)
        #for name in aList:
#               doc = libxml2.parseFile('aList')
#       for name in range(len(aList)):
Category_url="http://newshunt.com/fetchdata/nativeadd/nativeadd.xml"
for name in range(len(aList)):
###     print(aList[name])
        fullfile_name = file_path + aList[name]

###     print(fullfile_name)
        xpath(fullfile_name,Category_url)

