with open(raw_input("Enter file name: ")) as f:
    values = [float(line.split(":")[1]) for line in f.readlines() if line.strip().startswith("X-DSPAM-Confidence")]
    print 'Average spam confidence: %f' % (sum(values)/len(values))
