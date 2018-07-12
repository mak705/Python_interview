import json
import urllib

url="http://python-data.dr-chuck.net/comments_42.json"
uh = urllib.urlopen(url)
data = uh.read()
#print 'Retrieved',len(data),'characters'
#print data

info = json.loads(data)
print 'User count:', len(info)
print len(info["comments"])
print info["comments"]
counts = []
comments = info["comments"]

for comment in comments:
    counts.append(comment['count'])

print "Count: {0}".format(len(counts))
print "Sum: {0}".format(sum(counts))
