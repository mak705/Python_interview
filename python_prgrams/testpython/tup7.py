#sort Values according to value not key
x = { 'a':3, 'r':4, 'c':5, 'z':1}
print sorted( [ (v,k) for k,v in x.items() ] )
