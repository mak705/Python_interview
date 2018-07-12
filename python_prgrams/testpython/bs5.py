##http://newbiestartingtocode.blogspot.in/2016/07/using-python-to-access-web-data-week-4.html 

# Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Lana.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# # Hint: The first character of the name of the last page that you will load is: L

import urllib  
 from BeautifulSoup import *  
 url = raw_input('Enter URL ')  
 count = raw_input('Enter count: ')  
 count = int(count)  
 pos = raw_input('Enter position: ')  
 pos = int(pos)-1  
 html = urllib.urlopen(url).read()  
 seq = ''  
 for i in range(0,count):  
   soup = BeautifulSoup(html)  
   tags = soup('a')  
#   print tags[pos]
#   print tags[pos].contents[0]
   seq = seq + tags[pos].contents[0]+' '  
   html = urllib.urlopen(tags[pos].get('href', None)).read()  
 print"Sequence of names- ", seq  
 print 'Last name in sequence -', tags[pos].contents[0]  
#####################################################################
#from bs4 import BeautifulSoup
#import requests
#import pprint
#import re

#urls = ['http://python-data.dr-chuck.net/known_by_Lana.html', 'http://python-data.dr-chuck.net/known_by_Lana.html']
#scrape elements
#for url in urls:
#    response = requests.get(url)
#    soup = BeautifulSoup(response.content, "html.parser")

    #print titles only
#    h1 = soup.find("h1")
#   print h1.contents
#   print h1.contents[0]
#####################################################################################
# import urllib
# import re
# from bs4 import BeautifulSoup
# url = 'http://python-data.dr-chuck.net/known_by_Lana.html  '
# count = 1
# count = int(count)  
# pos = 18
# pos = int(pos)-1  
# html = urllib.urlopen(url).read()  
# seq = ''  
# for i in range(0,count):  
#     soup = BeautifulSoup(html)  
#     tags = soup('a')  
#     seq = seq + tags[pos].contents[0]+' '  
#     html = urllib.urlopen(tags[pos].get('href', None)).read()  
# print"Sequence of names- ", seq  
# print 'Last name in sequence -', tags[pos].contents[0] 

