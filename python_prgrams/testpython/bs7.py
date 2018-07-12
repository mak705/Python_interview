import urllib

from BeautifulSoup import *

url = raw_input("Enter URL: ")
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))

names = []

while count > 0:
    print "retrieving: {0}".format(url)
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page)
    tag = soup('a')
    name = tag[position-1].string
    names.append(name)
    url = tag[position-1]['href']
    count -= 1

print names[-1]

# import urllib
# from bs4 import BeautifulSoup
# url = 'http://python-data.dr-chuck.net/known_by_Lana.html'
# count = 1
# position = 1

# names = []

# while count > 0:
#     print "retrieving: {0}".format(url)
#     page = urllib.urlopen(url)
#     soup = BeautifulSoup(page)
#     tag = soup('a')
#     name = tag[position-1].string
#     names.append(name)
#     url = tag[position-1]['href']
#     count -= 1

# print names[-1]
