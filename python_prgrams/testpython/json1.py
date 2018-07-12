import json
data = '''{
"name" : "mak",
"phone" : {
 "type" : "intl",
 "number": "9809285619"
},
 "email": {
  "hide" : "yes"
}
}'''
info = json.loads(data)
print 'Name:',info["name"]
print 'Hide:',info["email"]["hide"]
