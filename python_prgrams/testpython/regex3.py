#Matching and extraction the data
#re.search() returns a false/tru statement depending on the string matches
#for extraction we use re.findall()
#Here output is python list
import re
x = 'My fav sport number is 10, My last ph number is 49'
y = re.findall('[0-9]+',x)
z = re.findall('[0-9]',x)
print y
print z
a = re.findall('[AEIOU]+', x)
print a
