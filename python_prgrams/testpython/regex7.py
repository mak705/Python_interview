import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', line) #match @, [^ ] means not blank line, ^ means not inside brackets, * means any of them
z = re.findall('^From .*@([^ ]*)', line)
##.* means any number of charachter
print y
print z

