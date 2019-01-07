from csv import DictReader
with open("C:\\Users\\makbulhussain.k\\Downloads\\name.csv") as f:
    a1 = [row["value"] for row in DictReader(f)]

from collections import Counter
counts = Counter(stri)

for word in a1:
    stri = (word[0])
    counts.update(list((word[0])))
    del counts[' ']
print (counts)
dda = sorted(counts.items(), key=lambda v:v[1], reverse=True)
ddb = sorted(dda, key = lambda k: (-k[1],k[0]))
for el in ddb:
    print (el[0] + ' '+ str(el[1]))
   
