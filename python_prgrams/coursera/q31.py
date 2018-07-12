print "you entered in a dark room with 2 door, Do you go through  1 or  2"

door = raw_input("> ")
if door == "1":
	print "There is giant beer is inside, what you will do?"
        print "1. Take the Cake"
        print "2. Run away"
	
 	beer = raw_input(">")
	
 	if beer == "1":
 		print "Good Try, Bear will roar on you"
 	elif beer == "2":
 		print "Good Decission, Better to avoid Risk"
elif door == "2":
 	print "Welcome to Garden, Which one you will select?"
	print "1 for Bluberries"
 	print "2 for Carrot"
	print "3 for Beetroot"
 
 	insanity = raw_input(">")
 
 	if insanity == "1" or insanity == "2":
  		print "Blueberries are also awesome"
 		print "Carrot is Vitamin C"
 	elif insanity == "3":
 		print "Beetroor is always good"
 	else:
 		print "Your Number is wrong"
 	
else:
 	print "Dark is always right, Wont You feel ?"

