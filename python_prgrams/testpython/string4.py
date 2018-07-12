data = 'eternoreports@verse.in Thu, Jun 16, 2016 at 9:40 PM'
atpos = data.find('@')
print atpos
#sppos = data.find(' ',atpos)
sppos = data.find(' ')
print sppos
host = data[atpos+1 :sppos]
print host
