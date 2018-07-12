fhand = open('1.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('Hi') :
        continue
    # Process our 'interesting' line
    print line
