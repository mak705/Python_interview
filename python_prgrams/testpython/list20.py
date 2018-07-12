fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = open('romeo.txt')
newList = list()
for line in fname:
 words = line.rstrip().split()
 for i in words:
  print i
  newList.append(i)
  newList.sort()
print newList
