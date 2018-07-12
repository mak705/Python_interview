from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
current_file = open(input_file)
print_all(current_file)

def rewind(f):
    f.seek(0)
rewind(current_file)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)



#
#The method seek() sets the file's current position at the offset. The whence argument is optional and defaults to 0, which means absolute file positioning, other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end.
#There is no return value. Note that if the file is opened for appending using either 'a' or 'a+', any seek() operations will be undone at the next write.
#If the file is only opened for writing in append mode using 'a', this method is essentially a no-op, but it remains useful for files opened in append mode with reading enabled (mode 'a+').
#If the file is opened in text mode using 't', only offsets returned by tell() are legal. Use of other offsets causes undefined behavior.
#Note that not all file objects are seekable.
