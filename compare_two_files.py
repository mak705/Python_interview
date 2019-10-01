from io import StringIO
f = StringIO('''1
2
5
6''')
next_number = 0
for n in range(11):
    if n == next_number:
        next_number = int(next(f, 0))
    else:
        print(n)
        
3
4
7
8
9
10

############################

prev = 0
with open('numbers.txt','r') as f:
    for line in f:
        value = int(line.strip())
        for i in range(prev, value-1):
            print('missing:', i+1)
    prev = value
# output numbers that are missing at the end of the file (see comment by @blhsing)
for i in range(prev, 1000000000000):
    print('missing:', i+1)
