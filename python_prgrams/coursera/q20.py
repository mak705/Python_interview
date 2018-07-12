from sys import argv
script, input_file = argv
current_file = open(input_file)
print current_file.read()

def rewind(current_file):
    current_file.seek(0)
rewind(current_file)

def print_a_line(current_file):
 print current_file.readline(),

print_a_line(current_file) 
print_a_line(current_file) 
print_a_line(current_file) 
