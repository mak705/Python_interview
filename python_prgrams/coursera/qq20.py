from sys import argv
script,input_file = argv

def print_all(current_file):
    print current_file.read()
current_file = open(input_file)

def print_a_line(count, current_file):
 print count,current_file.readline()

def rewind(current_file):
    current_file.seek(0)

print "Let's print the file"
print_all(current_file)

print "Lets rewind the file"
rewind(current_file)

count=1
print_a_line(count,current_file)
count= count + 1
print_a_line(count,current_file)
count = count + 1
print_a_line(count,current_file)
