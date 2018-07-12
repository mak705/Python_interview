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
