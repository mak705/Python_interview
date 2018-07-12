fhand = open('mbox-short.txt')
for line in fhand:
 line = line.rstrip()
# print "+", line
# if line == '': continue
 words = line.split()
# print words
 if words == []: continue
#or if len(words)<1: continue
 if words[0] != ('From '):continue
 print words[2]
