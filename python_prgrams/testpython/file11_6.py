#try the code below, it is working.
fname = raw_input("Enter file name: ")
count=0
value = 0
sum=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    num = float(line[pos+1:])
    sum=sum+num
    count = count+1    
print "Average spam confidence:", sum/count
