names = ['mark', 'henry', 'matthew', 'paul',
         'luke', 'robert', 'joseph', 'carl', 'michael']

d = {}
for name in names:
 key = len(name)
 if key not in d:
   d[key] = []
   d[key].append(name)
print d
# result: d = {4: ['mark', 'paul', 'luke', 'carl'], 
#              5: ['henry'], 6: ['robert', 'joseph'], 7: ['matthew', 'michael']}
