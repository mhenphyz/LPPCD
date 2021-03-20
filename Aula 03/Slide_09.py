import pandas as pd

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])
print(s1[2])

print(s1['b'])

print('\n Seguimentar serie \n')

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])

print(s1[0:2])