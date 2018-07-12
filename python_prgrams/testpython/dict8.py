name = raw_input("Enter a file name")
if len(name) < 1:
    name = "juliet.txt"
handle = open(name,'r')
text = handle.read()
#print len(text)
#print len(text),text[:40]
words = text.split()
#print len(words)
#print words
###############make a Dictionary
counts = dict() 
for word in words:
# print word
# if word in counts:
#  counts[word] = counts[word] + 1
#  print word,"word up",counts[word]
# else:
#  counts[word] = 1
#  print word,"Word",counts[word]
#print counts 
 counts[word] = counts.get(word,0) + 1
#print counts
#print counts.items()
maxVal = None
maxKey = None
for key,val in counts.items():
# if maxVal == None : maxVal = val
 if maxVal == None or maxVal < val:
# if maxVal <= val :
  maxVal = val
  maxKey = key
# print key,val,maxKey,maxVal
print maxKey,maxVal
