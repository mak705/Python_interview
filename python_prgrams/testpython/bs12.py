import re
import urllib
import bs4
url = 'http://python-data.dr-chuck.net/comments_261564.html' or raw_input('Enter - ')
html = urllib.urlopen(url).read()
print(html)  # let's see what we're working with!
soup = bs4.BeautifulSoup(html)
new_list = []
tags = soup('span')
for tag in tags:
    print('TAG:',tag)
    print('TAG.text:',tag.text)  # It is the tag.text we need to scan for integers.
    for x in re.findall('[0-9]+', tag.text):
        new_list.append(int(x))
print(new_list)
print('Total:', sum(new_list))
total = 0
for itervar in new_list:
    total += itervar
print('Total: ', total)

