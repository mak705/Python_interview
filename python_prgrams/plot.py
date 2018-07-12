
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt


# In[6]:

plt.plot([1, 3, 2, 4])


# In[7]:

plt.show()


# In[8]:


"""
Created on Sun May  7 11:39:35 2017

@author: makbul
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import scipy.stats as stats
import random
import math
print(stats.norm.__doc__)


# In[10]:

stats.norm.a, stats.norm.b
print dir(stats.norm)


# In[11]:

print(stats.norm.mean())
print(stats.norm.std())
print(stats.norm.var())


# In[24]:

#seed to make the distribuition stattistic
np.random.seed(2)
rn = stats.norm.rvs(size=3)
print(rn)


# In[ ]:




# In[ ]:



