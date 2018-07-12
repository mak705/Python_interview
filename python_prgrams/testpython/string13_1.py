text = "X-DSPAM-Confidence:            0.8475";
print text
pos = text.find(":")
print pos
print text[pos::pos+1]
print text[pos+1:]
print text[pos+1:].lstrip()
print float(text[pos+1:].lstrip())
print type(float(text[pos+1:].lstrip()))
