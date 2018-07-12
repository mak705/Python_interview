#Averaging with in the list
total = 0
count = 0
print "done to over"
while True:
 inp = raw_input('Enter a number')
 if inp == 'done':break
 value = float(inp)
 total = total + value
 count = count + 1
average = total/count
print 'Average is', average
