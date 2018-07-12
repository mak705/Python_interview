fhand = open('romeo.txt')
counts = dict()
for line in fhand:
 words = line.split()
# print words
 for word in words:
  counts[word] = counts.get(word,0) + 1
# print counts
newlist = list()
for key,val in counts.items():
 newlist.append((val,key))
#print newlist
newlist.sort(reverse=True)

for val,key in newlist[:11]:
 print key,val
