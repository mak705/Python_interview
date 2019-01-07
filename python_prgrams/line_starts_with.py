f = '''
>abc
AAA
AAA
>dfgg
BBBBB
BBBBB
BB
>zzz
CCCCC
CCC'''
currentline = ""
for line in f:
    if line.startswith('>'):
        line = line.rstrip('\n')
        if currentline != "":
            print (currentline)
        #print (line)
        currentline = ""
    else:
        line = line.rstrip('\n')
        currentline = currentline + line
print (currentline)
