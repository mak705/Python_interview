def count(string, letter):
    x = 0
    for i in string:
        if i == letter:
            x += 1
    print "The letter "+letter+" appears " +str(x)+" times in the string: "+string
    
count("This is a test","s")


#def count(string, letter):
#    x = 0
#    for i in letter:
#            x += 1
#    print "The letter "+letter+" appears " +str(x)+" times in the string: "+string
#
#count("This is a test","z")

