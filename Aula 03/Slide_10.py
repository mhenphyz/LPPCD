import pandas as pd

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])
s1[0] = 12
s1['b'] = 13

print(s1)