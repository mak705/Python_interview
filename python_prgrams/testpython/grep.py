import subprocess
from sys import argv
filename = raw_input("enter the filename you want to grep")
file_input='/newshunt/shared/config/%s' %filename
hosts=subprocess.Popen(['grep','categoryPageURL',file_input], stdout= subprocess.PIPE)
print hosts.stdout.read()

