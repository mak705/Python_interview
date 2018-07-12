counts = dict()
names = ['mak','nik','alu','mak','mak']
for name in names:
 counts[name] = counts.get(name,0) + 1
print counts
