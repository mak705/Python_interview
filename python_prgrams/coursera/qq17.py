from sys import argv
from os.path import exists
script, filename = argv
print "Does the %r output file exist? %r" % (filename, exists(filename))
