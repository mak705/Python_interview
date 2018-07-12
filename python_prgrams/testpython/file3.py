##counting lines in a file
fhand = open('mul.py')
count = 0
for line in fhand:
 count = count + 1
print 'Line count:', count
