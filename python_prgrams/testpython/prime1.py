ctr = 2
num = int(input("Enter a Number :"))
while(ctr <= num -1):
	if(num % ctr == 0):
  	        print("Number is not prime!")
		break;
	ctr = ctr + 1
print("End of the program")
