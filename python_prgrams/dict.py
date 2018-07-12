purse = dict()
purse['money'] = 120000000
purse['candy'] = 3
purse['tissue'] = 75
purse['tissue'] = purse['tissue'] + 4
print purse


#Dictionaries are like List
#List maintains order and Dictionaries donot maintains order
newlist = list()
newlist.append(28)
newlist.append(22)
print newlist
newlist[0]=23
print newlist

newlist = dict()
newlist['age'] = 28
newlist['course']=22
print newlist
newlist['course']=23
print newlist
##############################################
#As key Value pair
counts = dict()
names = ['mak','nik','alu','mak','mak']
for name in names:
 if name not in counts:
  counts[name] = 1
 else:
  counts[name]= counts[name] + 1
 print counts
#############################################
#as dictioary
counts = dict()
names = ['mak','nik','alu','mak','mak']
for name in names:
 counts[name] = counts.get(name,0) + 1
print counts
#############################################
#Definite Loops and Dictionaries
counts = { 'mak' : 1, 'nik' : 2, 'alu' : 3 }
for key in counts:
 print key, counts[key] 
#############################################
#Key vaue extracion
name = { 'mak' : 1, 'nik' : 2, 'alu' : 3 }
print list(name)
print name.keys()
print name.values()
print name.items()
##python supports 2 iteration
for a,b in name.items():
 print a,b
################################################
##Extracting largest count and value
name = raw_input("Enter a file name")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name,'r')
text = handle.read()
print len(text),text[:40]
words = text.split()
print len(words)
counts = dict()
for word in words:
 counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
 if bigcount is None or count > bigcount:
  bigword = word
  bigcount = count
print bigword,bigcount
##################################################

