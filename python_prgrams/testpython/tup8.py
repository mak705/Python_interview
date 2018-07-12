#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    word = line.split()
    if not line.startswith('From '): continue
    word_5 = word[5]
    word_5 = word_5.split(':')[0]
#    print word_5
    count[word_5] = count.get(word_5, 0) + 1
#    count[word[5]] = count.get(word[1], 0) + 1
#print count
#for key,value in count.items():
#for t in  count.items():
# print t
x = sorted(count.items())
#print x
for k,v in x:
 print k,v

