import urllib
from twurl import augment
print '*Calling twitter..'
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
	{'screen_name':'makhus1','count':'2'})
print url
connection = urllib.urlopen(url)
data = connection.read()
print data
headers = connection.info().dict
print headers
