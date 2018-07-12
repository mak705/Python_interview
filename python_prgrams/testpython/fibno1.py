#https://www.tutorialgateway.org/python-fibonacci-series-program/
# Python Fibonacci series Program using For Loop
 
# Fibonacci series will start at 0 and travel upto below number
Number = int(input("\nPlease Enter the Range Number: "))
 
# Initializing First and Second Values of a Series
First_Value = 0
Second_Value = 1
           
# Find & Displaying Fibonacci series
for Num in range(0, Number):
           if(Num <= 1):
                      Next = Num
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)

-=========================================================

am = int(raw_input('Give amount: '))

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

a = fib()
a.next()
0
for i in range(am):
    print a.next()
