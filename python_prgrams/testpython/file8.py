fname = raw_input('Enter file name')
fhand = open(fname)
count = 0
for line in fhand:
 if line.startswith('#From'):
  count = count + 1
print 'There is', count, 'From lines', fname