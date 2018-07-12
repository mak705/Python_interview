import re
x = 'We have just recieved rupees $10.00 for cookies'
y = re.findall('\$[0-9.]+', x)
print y
