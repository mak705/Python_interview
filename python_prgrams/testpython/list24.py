fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
 line = line.rstrip()
 if not line.startswith('From '):continue
 words = line.split()
 print words[1]
