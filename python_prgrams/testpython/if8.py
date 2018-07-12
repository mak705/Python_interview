name = raw_input('What is your name? ')

if name.endswith('mak'):
    if name.startswith('Mr.'):
        print 'Hello, Mr. Hussain' 
    elif name.startswith('Mrs.'):
        print 'Hello, Mrs. Beautiful' 
    else: 
        print 'Hello, handsome'
else: 
    print 'Hello, stranger'

