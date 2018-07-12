from sys import argv
script, hi = argv
print "Hi I'm the %s script." %  script
print "Hi I'm the %s script." %  hi
lives = raw_input("where do you live")
likes = raw_input("whome you likes S?")
print """
your script name is %s
Your first arg is %s
you lives in %s
you likes %s very much 
"""%(script, hi, lives, likes)

