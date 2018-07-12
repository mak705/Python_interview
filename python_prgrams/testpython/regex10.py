import re
hand = open('regex.txt')
newList = list()
for line in hand:
 stuff = re.findall('([0-9]+)', line)
 for i in stuff:
  newList.append(i)
print newList
integer = map(int, newList)
print integer
print sum(integer)
