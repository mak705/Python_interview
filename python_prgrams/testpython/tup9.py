fhand = open('romeo.txt')
counts = dict()
for line in fhand:
 words = line.split()
# print words
 for word in words:
  wrd = word.lower()
  counts[wrd] = counts.get(wrd,0) + 1
 print counts
print counts.items()

flipped = list()
for key,val in counts.items():
# print key,val
 newtup = (val, key)
# print newtup
 flipped.append(newtup)
#print flipped
flipped.sort(reverse=True)
#print flipped[:5]
for keynew, valnew in flipped[:5]:
 print keynew, valnew
