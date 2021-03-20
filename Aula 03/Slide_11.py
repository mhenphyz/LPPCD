import pandas as pd
import numpy as np

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])
s2 = pd.Series(s1)
a1 = np.array([9,8,7])

s3 = pd.Series(a1)
s2[0] = 20
s3[0] = 30

print(s1)
print(a1)