
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

#print first numpy array
fna = np.array([1,2,3])


# In[3]:

print fna


# In[5]:

#print array with zero
awz = np.zeros([3,3])


# In[6]:

print awz


# In[7]:

#awo
awo = np.ones([3,3])


# In[8]:

print awo


# In[9]:

#array with empty
awe = np.empty([2,3])


# In[10]:

awe


# In[11]:

#array with range method
awr = np.arange(12)


# In[12]:

awr


# In[18]:

#reshape method
awr.reshape(3,4)


# In[20]:

#Linespace for linear ((equal)) spaced elements
ls = np.linspace(1,6,5)


# In[21]:

ls


# In[22]:

#print 1d array
oda = np.arange(15)


# In[23]:

oda


# In[24]:

tda = oda.reshape(3,5)


# In[25]:

tda


# In[26]:

thda = np.arange(27).reshape(3,3,3)


# In[27]:

thda


# In[ ]:



