numbers = ('1','2','3','4','5','6','7','8','9','0')
letters = ('a','b','c','d','e','f')
punct = ('.', '!', '?')
charSetDict = {numbers:[], letters:[], punct:[]}
cSet = raw_input("Insert characters: ")
for c in cSet:
    for x in charSetDict.keys():
        if c in x:
            charSetDict[x].append(c)
            break;
charSetDict["Special"] = ['%', '$', '#']
charSetDict["Special"] = '><'
