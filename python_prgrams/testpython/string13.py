text = "X-DSPAM-Confidence:    0.8475";
spacePos = text.find(" ")
print spacePos
number = text[spacePos::1]
print number
#not really necessary but since we are just learning and playing
strippedNumber = number.lstrip();
print strippedNumber
result = float(strippedNumber)
print result
def reprint(printed):
    print printed  

reprint(result)
