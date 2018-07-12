import urllib
f = urllib.urlopen("http://www.dr-chuck.com")
contents = f.read()
f.close()
print len(contents)
print contents[0:30]

