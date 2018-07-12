#Double split pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print words
email = words[1]
print email
email2 = email.split('@')
print email2
print email2[1]
