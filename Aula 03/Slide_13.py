import pandas as pd
import numpy as np

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])
s2 = s1 / 2

print(s2)