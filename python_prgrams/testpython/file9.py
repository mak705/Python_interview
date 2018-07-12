fname = raw_input('Enter file name')
try:
 fhand = open(fname)
except:
 print "File cannot be opened",fname
exit()
count = 0
for line in fhand:
 if line.startswith('#From'):
  count = count + 1
  print 'There is', count, 'From lines', fname
