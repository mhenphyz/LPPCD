import pandas as pd

s1 = pd.Series([2,5,1,8,1,2,8])
s2 = s1.unique()

print(s1)
print(type(s1))
print(s2)
print(type(s2))