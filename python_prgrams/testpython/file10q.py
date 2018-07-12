fname = raw_input("Enter file name: ")
if len(fname) == 0:
 fname = 'mul.py'
fh = open(fname)
for line in fh:
 line = line.rstrip().upper()
 print line

