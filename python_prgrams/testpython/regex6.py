#Fine tuning
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
print y
z = re.findall('^From (\S+@\S+)',x)
t = re.findall('\S+@\S+' ,x) #'\S+?@\S+' ,x
print z
print t 

