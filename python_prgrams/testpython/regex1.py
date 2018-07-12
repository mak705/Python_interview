#string matching using re.search like find
import re
hand = open('mbox-short.txt')
for line in hand:
 line = line.rstrip()
# if line.find('From:') >= 0:
 if re.search('From:', line):
  print line
