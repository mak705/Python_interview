while 1==1:
    print("enter your choice")
    door = int(input("1 to enter door1 or 2 to enter door2"))
    if( door == 1):
      print("Tell me whether you want to kill bear or beg life")
      dare = int(input("3 to kill bear or 4 to beg life"))
      if(dare == 3):
        print("you are brave person!!")
        coins = int(input("Tell me, how many gold coins you need!!"))
        if(coins <= 50):
         print("Good!! you will get 49 coins")
         break
        else:
          print("Greedy person!!")
          break
      elif(dare==4):
       print("Begging life!! you move to door 2")
       print("Tell me your choice")
       dare = int(input("5 to kill devil or 6 to beg life"))
       if (dare == 5):
        print("you are brave person!!")
        coins = int(input("Tell me, how many gold coins you need!!"))
        if(coins <= 50):
         print("Good!! you will get 49 coins")
        else:
          print("Greedy person!!")
          break
       elif(dare == 6):
           print("You cant beg life, you are already a dad man!!.... sorry!!")
           break
    elif(door == 2):
     print("Tell me whether you want to kill devil or beg life")
     dare = int(input("7 to kill devil or 8 to beg life"))
     if(dare == 7):
       print("you are brave person!!")
       coins = int(input("Tell me, how many gold coins you need!!"))
       if(coins <= 50):
         print("Good!! you will get 49 coins")
         break
       else:
          print("Greedy person!!")
          break
     elif(dare == 8):
       print("You cant beg life, you are already a dad man!!.... sorry!!")
       break

