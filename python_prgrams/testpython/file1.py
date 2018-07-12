##Using Find
hand = open('mul.py')
for line in hand:
 line = line.rstrip()
 if line.find('From') > 0:
  print line
##if line.startswith('From'): ##starting of the string
