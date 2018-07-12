import json
import urllib

url="http://python-data.dr-chuck.net/comments_42.json"
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data

info = json.loads(data)
print 'User count:', len(info)

count = 0
for comment in info["comments"]:
    count += comment["count"]
print 'Total count:', count
