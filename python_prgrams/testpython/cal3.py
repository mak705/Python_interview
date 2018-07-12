print("1: ADDITION")
print("2: SUBTRACTION")
print("3: MULTIPLICATION")
print("4: DIVISION")
print("5: quit")
CHOICE = raw_input("Enter the Numbers:")
if CHOICE == "1":
    a = float(raw_input("Enter the value of a:"))
    b = float(raw_input("Enter the value of b:"))
    c = a + b
    print c

elif CHOICE == "2":
    a = float(raw_input("Enter the value of a:"))
    b = float(raw_input("Enter the value of b:"))
    c = a - b
    print c

elif CHOICE == "3":
    a = float(raw_input("Enter the value of a:"))
    b = float(raw_input("Enter the value of b:"))
    c = a * b
    print c

elif CHOICE == "4":
    a = float(raw_input("Enter the value of a:"))
    b = float(raw_input("Enter the value of b:"))
    c = a / b
    print c
else: 
  print "Invalid Number"
  print "\n"

