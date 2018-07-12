## * and + push outward in both direction(greedy) to match the largest possible string
import re
x = 'From : Using the : character'
y = re.findall('^F.+:', x)
print y
