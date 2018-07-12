from bs4 import BeautifulSoup

soup = BeautifulSoup(open('/newshunt/shared/config/cricket.xml','r'))
print(soup.prettify())
with open("file.txt", "w") as f:
    f.write(soup.prettify())

tags = soup.find_all('categoryPageURL')

