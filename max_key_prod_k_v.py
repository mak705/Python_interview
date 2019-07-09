#How to find the max of key which has the max of key value product
a = [3,4,5,5,6,6,6,7,7]
c = set(a)
counts = {}
for i in a:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] =1
#counts
t = [k*v for k,v in counts.items()]
max_index = t.index(max(t))
list(c)[max_index]

################################################

from collections import Counter

a = [3,4,5,5,6,6,6,7,7]
c = Counter(a)

m = sorted(c.items(),key= lambda x: x[0]*x[1], reverse = True)
print(m[0][0])

#################################################
a = [3,4,5,5,6,6,6,7,7]
counts = {}
for i in a:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] =1
key, value = max(counts.items(), key=lambda x:x[1])
key
