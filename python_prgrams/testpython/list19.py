fname= raw_input("Enter file name: ")
if len(fname) == 0:
    fname = open('romeo.txt')
#newList = []
for line in fname:
    words = line.rstrip().split()
    words.sort()
    print words
