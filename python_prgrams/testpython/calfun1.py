def arithematic_expression(a,b):
    arithematic_expression(a,b)
print("enter 1 for addition, 2 for multiplication, 3 for division, 4 for substraction")
print("enter one number to perform arithematic operation")
num = int(input())
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
if (num == 1):
 print ("Addition will be performed")
 print(a+b)

if (num == 2):
 print ("multiplication will be performed")
 print(a * b)
if (num == 3):
 print ("diviison will be performed")
 print(a / b) 
if (num == 4):
 print ("substraction will be performed")
 print(a - b)
else
