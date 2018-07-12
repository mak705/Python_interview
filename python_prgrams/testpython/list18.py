fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fhand = open('romeo.txt')
for line in fhand:
 print line
 words = line.split()
 words.sort()
 print words

