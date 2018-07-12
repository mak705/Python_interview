# -*- coding: utf-8 -*-
"""
Created on Sat May 20 13:19:48 2017

@author: makbul
"""

import pandas as pd
import numpy as np
df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'two', 'two', 'three', 'four'],
                    'b': ['x', 'y', 'x', 'y', 'x', 'x', 'x'],
                    'c': np.random.randn(7)})


print(df2)

print(df2.duplicated('a'))
print df2.duplicated('a',keep = 'last')
#print(df2.duplicated('a', keep=False))
#print(df2.drop_duplicates('a'))
#print(df2.drop_duplicates('a', keep='last'))
#print(df2.drop_duplicates('a', keep=False))