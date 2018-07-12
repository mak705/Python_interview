fname = raw_input("Enter file name: ")
values = []
with open(fname) as f:
    for line in f.readlines():
        if line.strip().startswith("X-DSPAM-Confidence"):
            values.append(float(line.split(":")[1]))

print 'Average spam confidence: %f' % (sum(values)/len(values))
