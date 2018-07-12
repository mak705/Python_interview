#sort Values according to value not key
x = { 'a':3, 'r':4, 'c':5, 'z':1}
tmp = list()
for k,v in x.items():
 tmp.append((v,k))
print tmp
tmp.sort(reverse=True)
print tmp
