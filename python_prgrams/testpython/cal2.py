#!/usr/bin/python
"""This is a simple calculator program  """

def addition( val1 , val2 ):
    """This function adds two numbers and returns result"""
    return val1 + val2

def subtraction( val1, val2 ):
    """This function subtracts two numbers and returns result"""
    return val1 – val2

def multiply(val1 , val2):
    """This function multiplies two numbers and returns result"""
    return val1 * val2

def division(val1 , val2):
    """This function divides two numbers and returns result"""
    return val1 / val2

VALUE1 = int(raw_input("enter the first number    "))
VALUE2 = int(raw_input("enter the second number   "))
OPTION = int(raw_input("enter the OPTION \n 1.addition \n \
2.subtraction \n 3.multiplication \n 4.Division\n \n"))

if OPTION == 1:
    print "Result = ",addition(VALUE1 , VALUE2)
elif OPTION == 2:
    print "Result = ",subtraction(VALUE1 , VALUE2)
elif OPTION == 3:
    print "Result = ",multiply(VALUE1 , VALUE2)
elif OPTION == 4:
    print "Result = ",division(VALUE1 , VALUE2)
else:
    print "invalid input, sorry try again"
