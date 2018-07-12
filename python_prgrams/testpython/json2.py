import json
input = '''[
 { "id": "001",
   "x" : "2",
   "name" : "Mak"
 },
 { "id" : "002",
   "x"  : "7",
   "name": "sh"
 }
]'''
info = json.loads(input)
print 'User Count:', len(info)
for item in info:
 print 'Name',item['name']
 print 'Id', item['id']
 print 'Attribuite', item['x']
