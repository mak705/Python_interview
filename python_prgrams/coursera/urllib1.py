#URllib is an application layer library, Since HTTP is so common we have a library that does all the socket work for us and make web pages look like a file
# Uurllib is the library and urlopen is method
import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhand:
 print line.strip()
