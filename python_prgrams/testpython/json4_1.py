import json
import urllib
add = list()
inp = raw_input('Enter a URL: ')

url = urllib.urlopen(inp)
data = url.read()
print len(data)

try:
    js = json.loads(data)
except:
    js = None

comments = js['comments']
for counts in comments:
    add.append(counts['count'])

print sum(add)

