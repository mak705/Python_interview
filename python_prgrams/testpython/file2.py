##using regular expression
import re
hand = open('mul.py')
for line in hand:
 line = line.rstrip()
 if re.search('From', line):
  print line
##if re.search('^From',line): ##starting of the string
