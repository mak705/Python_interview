# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

#Let's break down the first function, print_two, which is the most similar to what you already know from making scripts:

#First we tell Python we want to make a function using def for "define".
#On the same line as def we give the function a name. In this case we just called it "print_two" but it could also be "peanuts". It doesn't matter, except that your function should have a short name that says what it does.
#Then we tell it we want *args (asterisk args) which is a lot like your argv parameter but for functions. This has to go inside () parentheses to work.
#Then we end this line with a : colon, and start indenting.
#After the colon all the lines that are indented four spaces will become attached to this name, print_two. Our first indented line is one that unpacks the arguments the same as with your scripts.
#To demonstrate how it works we print these arguments out, just like we would in a script.
#The problem with print_two is that it's not the easiest way to make a function. In Python we can skip the whole unpacking arguments and just use the names we want right inside (). That's what print_two_again does.

#After that you have an example of how you make a function that takes one argument in print_one.

#Finally you have a function that has no arguments in print_none.


