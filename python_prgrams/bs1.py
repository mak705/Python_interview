import urllib
from bs4 import BeautifulSoup
url = raw_input('Enter-')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# print soup.prettify(formatter=None)
tags = soup.findAll('categorypageurl')
#tags = soup.findAll('name')
 print tags
for tag in tags:
    print tag.text
