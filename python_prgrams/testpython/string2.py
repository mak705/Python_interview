fruit = 'banana Mango'
if 'a' in fruit:
 print "found it"
#Capitalise Important because of searching we can change 
#everything to lower and do; easy for searching
print fruit.lower()
print fruit.upper()
print type(fruit)

####Finding the postion
position = fruit.find('na')
print 'the postion of na is ', position
print fruit.find('Z')

#replace
rep = fruit.replace('Mango','Apple')
print rep
print fruit.replace('a','X')
print fruit.startswith('b')
print fruit.startswith('p')
