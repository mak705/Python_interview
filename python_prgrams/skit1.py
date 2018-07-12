# -*- coding: utf-8 -*-
"""
Created on Wed May  3 06:04:26 2017

@author: makbul
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
boston_dataset = load_boston()
df_boston = pd.DataFrame(boston_dataset.data)
df_boston.columns = boston_dataset.feature_names
df_boston['Price'] = boston_dataset.target