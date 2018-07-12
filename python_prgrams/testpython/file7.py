##counting lines in a file
fhand = open('mul.py')
for line in fhand:
 line = line.rstrip()
 if not line.startswith('#From'):
  print line
