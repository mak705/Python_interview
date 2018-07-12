string = "X-DSPAM-Confidence: 0.8475"
start_index = string.find(':')
print start_index
num = string[start_index+1:].strip()
print float(num)
