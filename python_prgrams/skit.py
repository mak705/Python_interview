
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


# In[25]:

np.random.seed(10)
population_ages1 = stats.poisson.rvs(loc=18, mu=35, size=150000)
population_ages2 = stats.poisson.rvs(loc=18, mu=10, size=100000)
population_ages = np.concatenate((population_ages1, population_ages2))
print population_ages.mean()
print population_ages2.mean()
print population_ages1.mean()
#in PD µ = np, nof trials * prob of success


# In[26]:


np.random.seed(6)
sample_ages = np.random.choice(a= population_ages,
                               size=500)            # Sample 1000 values

print ( sample_ages.mean() )                         # Show sample mean

print(population_ages.mean() - sample_ages.mean())   # Check difference between means


# In[28]:

# Confidence Interval

np.random.seed(10)

sample_size = 1000
sample = np.random.choice(a= population_ages, size = sample_size)
sample_mean = sample.mean()

z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*

print("z-critical value:")              # Check the z-critical value
print(z_critical)                        

pop_stdev = population_ages.std()  # Get the population standard deviation

margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))

confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)  

print("Confidence interval:")
print(confidence_interval)


# In[31]:

# T distr, without std devidation
np.random.seed(10)

sample_size = 25
sample = np.random.choice(a= population_ages, size = sample_size)
sample_mean = sample.mean()

t_critical = stats.t.ppf(q = 0.90, df=24)  # Get the t-critical value*

print("t-critical value:")                  # Check the t-critical value
print(t_critical)                        

sample_stdev = sample.std()    # Get the sample standard deviation

sigma = sample_stdev/math.sqrt(sample_size)  # Standard deviation estimate
margin_of_error = t_critical * sigma

confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)  

print("Confidence interval:")
print(confidence_interval)


# In[ ]:



