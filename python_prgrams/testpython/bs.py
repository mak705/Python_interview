#and we are going to parse the web page, and we're going to look at all the anchor tags and print out the hrefs. That's it, this is the whole thing, thanks to Beautiful Soup

import urllib
from BeautifulSoup import*

url = raw_input('Enter-')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#Retrieve the list of anchor tags
#Each tag like a dictionary of HTML attribuites

tags = soup('a')
for tag in tags:
 print  tag.get('href', None)


#############################################
#https://www.linkedin.com/pulse/python-how-web-scrape-data-from-yellow-pages-hubert-l-
#scrap yellow pages busieness name
import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.yellowpages.com/search?search_terms=Seafood+Restaurants&geo_location_terms=San+Francisco%2CCA')
soup = BeautifulSoup(r.content)
g_data = soup.find_all("div", {"class":"info"})

for item in g_data:
        print item.contents[0].find_all("a",{"class":"business-name"})[0].text


--------------------
import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.yellowpages.com/los-angeles-ca/coffee-shops')
soup = BeautifulSoup(r.content)
print soup
g_data = soup.find_all("div", {"class":"info"})

for item in g_data:
        print item.contents[0].find_all("a",{"class":"business-name"})[0].text
        print item.contents[1].find_all("p",{"class":"addr"})[0].text
        try:
            print item.contents[1].find_all("span",{"itemprop":"addressLocality"})[0].text
        except:
            pass
        try:
            print item.contents[1].find_all("li",{"class":"primary"})[0].text
        except:
            pass
