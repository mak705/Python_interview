## set command I dont know
fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fh = open('romeo.txt')
lst = list()
for line in fh:
    for i in line.split():
        lst.append(i)
        lst.sort()
print list(set(lst))
