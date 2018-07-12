from sys import argv
script, filename = argv
#raw_input("what is your filename") 
target = open(filename, 'w')
target.truncate()
line1=raw_input("1:")
target.write(line1)
target.close()
