
# coding: utf-8

# In[1]:

import matplotlib.pyplot as pit


# In[17]:

import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
boston_dataset = load_boston()
print boston_dataset['feature_names']
#store data into data frame
df_boston = pd.DataFrame(boston_dataset.data)
df_boston.columns = boston_dataset.feature_names


# In[16]:

df_boston.head()


# In[18]:

print boston_dataset.data.shape
print boston_dataset.target.shape


# In[19]:

print boston_dataset.target


# In[ ]:



