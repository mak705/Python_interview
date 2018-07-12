romeo.txt
-----------------
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
#######################################
mbox-short.txt
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Return-Path: <postmaster@collab.sakaiproject.org>

From: louis@media.berkeley.edu
From zqian@umich.edu Fri Jan  4 16:10:39 2008

#############################################
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print c
###########################################
#list append
stuff = list()
stuff.append('book')
stuff.append('Hi')
stuff.append(99)
print stuff
some=99 in stuff
print some
some='ss' in stuff
print some
some='ss' not in stuff
print some
############################################
#Averaging with in the list
total = 0
count = 0
while True:
 inp = raw_input('Enter a number')
 if inp == 'done':break
 value = float(inp)
 total = total + value
 count = count + 1
average = total/count
print 'Average is', average
numlist = list()
while True:
 inp = raw_input('Enter a number')
 if inp == 'done':break
 value = float(inp)
 numlist.append(value)
average = sum(numlist)/len(numlist)
print "Averag", average
abc = 'With three words'
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]
for w in stuff:
 print w
#################################################
#split looks many spaeces equal to one space
line = 'first:second:third'
thing = line.split(':')
print thing

fhand = open('mbox-short.txt')
for line in fhand:
 line = line.rstrip()
 if not line.startswith('From '):continue
 words = line.split()
 print words[2]
#################################################
#Double split pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
print email
email2 = email.split('@')
print email2
print email2[1]
fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fhand = open('romeo.txt')
for line in fhand:
 words = line.split()
 words.sort()
 print words

#################################################
fname= raw_input("Enter file name: ")
if len(fname) == 0:
    fname = open('romeo.txt')
newList = []
for line in fname:
    words = line.rstrip().split()
    words.sort()
    print words
words=["hi","mak","gd"]
print words[0]
print words[1]
print words[2]

#####################################################
#Appending
fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = open('romeo.txt')
newList = list()
for line in fname:
 words = line.rstrip().split()
 for i in words:
  newList.append(i)
  newList.sort()
print newList


###################################################
##Removing Duplicate lines
fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fh = open('romeo.txt')
newlist = list()                       # list for the desired output
for line in fh:                    # to read every line of file romeo.txt
    word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
    for element in word:           # check every element in word    
        if element in newlist:         # if element is repeated
            continue               # do nothing
        else :                     # else if element is not in the list
            newlist.append(element)    # append     
newlist.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print newlist                          # print the list

###########################################################
##Duplicate lines removal
def openfile():
    fname = raw_input("Enter file name: ")
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh
def listWords(fh):
    lst = []
    for line in fh:
        line = ((line.rstrip()).lstrip()).split()
        for word in line:
            if word not in lst:
                lst.append(word)
    lst.sort()
    return lst
fh = openfile()
result = listWords(fh)
print result
######################################################
##Duplicate lines removal
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
 line = line.rstrip()
 if not line.startswith('From '):continue
 words = line.split()
 print words[1]

#############################################
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
 line = line.rstrip()
 if not line.startswith('From '):continue
 words = line.split()
 print words
 count = count + 1
print "There were", count, "lines in the file with From as"

######################################################

fhand = open('mbox-short.txt')
for line in fhand:
 line = line.rstrip()
 words = line.split()
 if words == []: continue
 if words[0] != ('From '):continue
 print words[2]

#############################################
nums = [1,2,3]
nums.append(4)
print(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums)
words=["python","beautiful"]
index = 1
words.insert(index,"is")
print words
words.sort()
print words
###############################################
