thelist = ["add","multiply","divide","subtract"]

def Multiply(x,y):
 print(x * y)

def Divide(x,y):
 x = float(x)
 y = float(y) 
 print(x / y)

def Add(x,y):
 print(x + y)

def Subtract(x,y):
 print(x - y)
 
while True:
    operation = input("What would you like to do? Multiply/Divide/Add/Subtract ")
    if operation in thelist:
        break
    else:
        print "That was not an option.."

if operation == "multiply":
    while True:
            x = int(input("First number: "))
            y = int(input("Second number: "))
            break
    Multiply(x,y)
elif operation == "subtract":
    while True:
            x = int(input("First number: "))
            y = int(input("Second number: "))
    Subtract(x,y)
elif operation == "Add" or operation == "add":
    while True:
            x = int(input("First number: "))
            y = int(input("Second number: "))
    Add(x,y)
elif operation == "Divide" or operation == "divide":
    while True:
            x = int(input("First number: "))
            y = int(input("Second number: "))
    Divide(x,y)
else:
    pass
