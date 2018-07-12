import urllib
import re
from bs4 import BeautifulSoup
url = 'http://python-data.dr-chuck.net/comments_287610.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('span')
for tag in tags:
 print tag
