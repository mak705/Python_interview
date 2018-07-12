print ("add=1")
print ("substract=2")
print ("multiply=3")
print ("divide=4")
print ("exit=5")

num1 = int(input("Enter the number"))
num2 = int(input("Enter the number"))

user_input  =int(input("Enter the number for operation"))
if user_input == 1:
 def add(num1,num2):
     print(num1 + num2)
 add(num1,num2)
elif user_input == 2:
 def substract(num1,num2):
     print(num1 - num2)
 substract(num1,num2)
elif user_input == 3:
 def multiply(num1,num2):
     print(num1 * num2)
 multiply(num1,num2)
elif user_input == 4:
 def divide(num1,num2):
     print(num1 / num2)
 divide(num1,num2)
else:
    print("Enter the correct number for operation")
