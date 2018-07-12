#http://stackoverflow.com/questions/33437657/urllib-urlopen-runs-only-once
import urllib
from BeautifulSoup import *
url = raw_input('Enter URL: ')
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/known_by_Lockey.html "
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: ')) - 1
taglist = list()
urllist = list()
urllist.append(url)

print 'Retrieving: ', urllist[0]
for i in range(count):
  html = urllib.urlopen(url).read()
  soup = BeautifulSoup(html)
  tags = soup('a')
  for tag in tags:
    taglist.append(tag)
  url = taglist[pos-1].get('href', None)
  print 'Retrieving: ', url
  urllist.append(url)
  taglist = list()
print 'Last Url: ', urllist[-1]
####################################################################################
## import urllib
# from bs4 import BeautifulSoup
# url = raw_input('Enter URL: ')
# if len(url) < 1:
#     url = "http://python-data.dr-chuck.net/known_by_Lockey.html "
# count = 3
# pos = 1
# urllist = list()
# urllist.append(url)
# print 'Retrieving: input is', urllist[0]
# for i in range(count):
#     html = urllib.urlopen(url).read()
#     soup = BeautifulSoup(html)
#     tags = soup('a')
#     url = taglist[pos-1].get('href', None)
#     print 'Retrieving: ', url
#     urllist.append(url)
#     taglist = list()
#     for tag in tags:
#         taglist.append(tag)
#     print taglist[0]
# print 'Last Url: ', urllist[-1]
