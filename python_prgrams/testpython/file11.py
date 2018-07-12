fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.strip()
    print line

pos = line.find(':')
num = float(line[20:])
print num
