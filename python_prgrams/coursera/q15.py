from sys import argv
script, filename = argv #arg declaration
txt = open(filename) # opening file to read
print txt.read() # reading file
filenew = raw_input("enter another filename")
txtnew = open(filenew)
print txtnew.read()

