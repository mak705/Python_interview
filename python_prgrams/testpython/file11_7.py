values = []
#fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
with open(fname, 'r') as fh:
    for line in fh.read().split('\n'): #creating a list of lines
        if line.startswith('X-DSPAM-Confidence:'):
            values.append(line.replace('X-DSPAM-Confidence: ', '')) # I don't know whats after the float value

values = [float(i) for i in values] # need to convert the string to floats
print 'Average spam confidence: %f' % float( sum(values) / len(values))
