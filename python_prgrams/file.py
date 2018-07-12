import re
hand = open('file.txt', 'rw')
#hand = "26-09-2016 23:59 : [AutoFetchCommon.java2488]: {pk:57989252,titleUni"
f = open("stuff.txt", "w")
for line in hand:
# line = line.rstrip()
 a = re.findall("\{(.*)$", line)
# print unicode(a)

 f.write("{"+a[0]+"}")
f.close()

