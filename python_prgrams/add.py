while 1==1:
   print ("Enter a sign to perform mathematical operation")
   sign = raw_input("Enter one sign +, *, -, /")
   if sign == '+':
    print ("Addition will be performed")
    a = float(raw_input("Enter the value of a:"))
    b = float(raw_input("Enter the value of b:"))
    c = a + b
    print c
   else: 
    break
