
# coding: utf-8

# In[1]:

x = 1
y = 2
x + y


# In[2]:

x


# In[3]:

def add_numbers(x, y):
    return x + y

add_numbers(1, 2)


# In[4]:

def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))


# In[5]:

def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
    
print(add_numbers(1, 2, flag=True))


# In[6]:

def add_numbers(x,y):
    return x+y

a = add_numbers
a(1,2)


# In[7]:

x = (1, 'a', 2, 'b')
type(x)


# In[8]:

x = [1, 'a', 2, 'b']
type(x)


# In[9]:

x.append(3.3)
print(x)


# In[10]:

for item in x:
    print(item)


# In[11]:

i=0
while( i != len(x) ):
    print(x[i])
    i = i + 1


# In[12]:

[1,2] + [3,4]


# In[13]:

[1]*3


# In[14]:

1 in [1, 2, 3]


# In[15]:

x = 'This is a string'
print(x[0]) #first character
print(x[0:1]) #first character, but we have explicitly set the end character
print(x[0:2]) #first two characters


# In[16]:

x[-1]


# In[19]:

x[-4:-2] #This will return the slice starting from the 4th element from the end and stopping before the 2nd element from the end.


# In[18]:

x[:3]


# In[21]:

firstname = 'Christopher'
lastname = 'Brooks'

print(firstname + ' ' + lastname)
print(firstname*3)
print('Chris' in firstname)


# In[24]:

'Chris' + 2


# In[25]:

'Chris' + str(2)


# In[26]:

x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
x['Christopher Brooks'] # Retrieve a value by using the indexing operator


# In[27]:

x['Kevyn Collins-Thompson'] = None
x['Kevyn Collins-Thompson']


# In[28]:

for name in x:
    print(x[name])


# In[ ]:



