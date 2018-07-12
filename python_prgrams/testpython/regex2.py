#re.search like startswith 
import re
hand = open('mbox-short.txt')
for line in hand:
 line = line.rstrip()
# if line.startswith('From:'):
 if re.search('^From:', line):
  print line
