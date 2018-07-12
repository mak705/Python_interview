text = "X-DSPAM-Confidence:    0.8475";
atpos = text.find(":")
print atpos
sppos = text.find(' ',atpos)
host = float(text[atpos + 1:])
print host
#sppos = data.find(' ',atpos)
#print sppos
#host = data[atpos+1 :sppos]
#print host

