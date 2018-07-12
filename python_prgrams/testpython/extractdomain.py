fname = raw_input('Enter file name: ')  # prompt for file name
if ( len(fname) < 1 ) : fname = 'mboxtest.txt'
fh = open(fname)  # file handler
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]   # email part
    print email
    domain_split = email.split("@") # break up email to separate out org name
    print domain_split
    org = domain_split[1]
    print org

