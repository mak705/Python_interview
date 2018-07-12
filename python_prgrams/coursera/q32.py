elements = [0,1,2,3,4,5,6,7,8,9,10]

elements[3:5] = range(10,12) # replace indexes 3 and 4 with 10 and 11.

#elements[3:7:2] = range(100,201,100) replace indexes 3 and 5 with 100 and 200

#elements[:] = range(4) # replace entire list with [0,1,2,3]
for i in range(0, 6):
    print "Adding %d to the list." % i    # line 23
    # append is a function that lists understand
    elements.append(i)

for i in elements:
    print "Element was: %d" % i

