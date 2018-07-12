thelist = ["add","multiply","divide","subtract"]
while True:
    operation = raw_input("What would you like to do? multiply/divide/add/subtract ")
    if operation in thelist:
        break
    else:
        print("That was not an option..")

if operation == "multiply":
            x = int(input("First number: "))
            y = int(input("Second number: "))
            print(x * y)
elif operation == "subtract":
            x = int(input("First number: "))
            y = int(input("Second number: "))
            print(x - y)
elif operation == "add":
            x = int(input("First number: "))
            y = int(input("Second number: "))
            z = x + y
            print z
elif operation == "divide":
            x = int(input("First number: "))
            y = int(input("Second number: "))
            print(x / y)
else:
    pass
