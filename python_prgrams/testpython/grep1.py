def grep(pattern, filenames):
    for f in filenames:
        for line in open(f):
            if pattern in line:
                print line
