import subprocess
from sys import argv
filename = raw_input("enter the filename you want to grep")
file_input='/newshunt/shared/config/%s' %filename
hosts=subprocess.Popen(['grep','categoryPageURL',file_input], stdout= subprocess.PIPE)
print hosts.stdout.read()


===================================================

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('/newshunt/shared/config/cricket.xml','r'))
print(soup.prettify())
with open("file.txt", "w") as f:
    f.write(soup.prettify())

tags = soup.find_all('categoryPageURL')


========================================================

import urllib
from bs4 import BeautifulSoup
url = raw_input('Enter-')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# print soup.prettify(formatter=None)
tags = soup.findAll('categorypageurl')
#tags = soup.findAll('name')
# print tags
for tag in tags:
    print tag.text

