import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
 line = line.rstrip()
 stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)#. is not wild card inside brackets since to match 0.97 etc 
 if len(stuff) != 1: continue
 num = float(stuff[0])
 numlist.append(num)
 print num
 print numlist
print 'Maximum:', max(numlist)
 
#Now, remember that find all gives you back a list. And so the way I tell whether I actually found something on this line that did any matching. 
#The way I do is I ask, is the list that I got back, is there one or more? Actually, in this case I'm saying I only want ones where there's exactly one match. So, it goes in and pulls the thing out I want, and I get one match. That's the length of that thing that returns set of matches is not one. I continue, which means I'm skipping all the lines that don't start with it and have a number. And if not, I just pull the zeroth one out, which actually pulls that number out. And then I append it, and then I do my max, and I do my other things. And so this here is a way of, well, when I combine these two lines together, these two lines are both selecting and extracting, all in one statement.  
