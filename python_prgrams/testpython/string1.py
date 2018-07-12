fruit = 'banana Mango'
index = 0
for letter in fruit:
 if letter == 'a':
  index = index + 1
print 'a is repeating', index, 'times'
print fruit[0:3]
print fruit[0:1]
print fruit[0:100]
print fruit[:]
print fruit[1:]
print fruit[::-1]
print fruit[:5]
## string concatenation
t = fruit +'apple'
print t
t1= fruit +' '+'apple'
print t1

