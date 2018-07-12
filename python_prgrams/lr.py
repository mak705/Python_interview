
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
iris_dataset = load_iris()


# In[3]:

type(iris_dataset)


# In[5]:

print iris_dataset.DESCR


# In[6]:

print iris_dataset.feature_names


# In[7]:

print iris_dataset.target


# In[8]:

print iris_dataset.data.shape


# In[9]:

X_feature = iris_dataset.data


# In[10]:

Y_target = iris_dataset.target


# In[11]:

print X_feature.shape
print Y_target.shape


# In[12]:

from sklearn.neighbors import KNeighborsClassifier


# In[13]:

knn = KNeighborsClassifier(n_neighbors=1)


# In[14]:

print knn


# In[15]:

knn.fit(X_feature,Y_target)


# In[16]:

X_new = [[3,5,4,1],[5,3,4,2]]


# In[17]:

knn.predict(X_new)


# In[18]:

from sklearn.linear_model import LogisticRegression


# In[19]:

logReg = LogisticRegression()


# In[20]:

logReg.fit(X_feature,Y_target)


# In[21]:

logReg.predict(X_new)


# In[ ]:



