fhand = open('mul.py')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From') :
        continue
    # Process our 'interesting' line
print line
