##counting lines in a file
fhand = open('mul.py')
for line in fhand:
 line = line.rstrip()
 if line.startswith('#From'):
  print line
