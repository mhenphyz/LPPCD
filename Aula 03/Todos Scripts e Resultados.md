## Slide_06.py

```python
import pandas as pd

s1 = pd.Series([2,5,1,8])
print(s1)


#### Resultado do script 

0    2
1    5
2    1
3    8
dtype: int64
```
***
## Slide_07.py

```python
import pandas as pd

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])
print(s1)


#### Resultado do script 

a    2
b    5
c    1
d    8
dtype: int64
```
***
## Slide_08.py

```python
import pandas as pd

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])

print(s1,)
print(s1.index,)
print(s1.values)


#### Resultado do script 

a    2
b    5
c    1
d    8
dtype: int64
Index(['a', 'b', 'c', 'd'], dtype='object')
[2 5 1 8]
```
***
## Slide_09.py

```python
import pandas as pd

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])
print(s1[2])

print(s1['b'])

print('\n Seguimentar serie \n')

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])

print(s1[0:2])


#### Resultado do script 

1
5

 Seguimentar serie 

a    2
b    5
dtype: int64
```
***
## Slide_10.py

```python
import pandas as pd

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])
s1[0] = 12
s1['b'] = 13

print(s1)


#### Resultado do script 

a    12
b    13
c     1
d     8
dtype: int64
```
***
## Slide_11.py

```python
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


#### Resultado do script 

a    20
b     5
c     1
d     8
dtype: int64
[30  8  7]
```
***
## Slide_12.py

```python
import pandas as pd
import numpy as np

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])
s2 = s1[s1 > 4]

print(s2)


#### Resultado do script 

b    5
d    8
dtype: int64
```
***
## Slide_13.py

```python
import pandas as pd
import numpy as np

s1 = pd.Series([2,5,1,8], index=['a', 'b', 'c', 'd'])
s2 = s1 / 2

print(s2)


#### Resultado do script 

a    1.0
b    2.5
c    0.5
d    4.0
dtype: float64
```
***
## Slide_14.py

```python
import pandas as pd

s1 = pd.Series([2,5,1,8,1,2,8])
s2 = s1.unique()

print(s1)
print(type(s1))
print(s2)
print(type(s2))


#### Resultado do script 

0    2
1    5
2    1
3    8
4    1
5    2
6    8
dtype: int64
<class 'pandas.core.series.Series'>
[2 5 1 8]
<class 'numpy.ndarray'>
```
***
## Slide_15.py

```python
import pandas as pd
import numpy as np

s2 = pd.Series([5,-3,np.NaN,14])

print(s2.isnull())


#### Resultado do script 

0    False
1    False
2     True
3    False
dtype: bool
```
***
## Slide_16.py

```python
import pandas as pd
import numpy as np

mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
myseries = pd.Series(mydict)

print(myseries)


#### Resultado do script 

red       2000
blue      1000
yellow     500
orange    1000
dtype: int64
```
***
## Slide_19.py

```python
import pandas as pd

data = {
'color' : ['blue','green','yellow','red','white'],
'object' : ['ball','pen','pencil','paper','mug'],
'price' : [1.2,1.0,0.6,0.9,1.7]}

print(data)

df = pd.DataFrame(data)

print(df)


#### Resultado do script 

{'color': ['blue', 'green', 'yellow', 'red', 'white'], 'object': ['ball', 'pen', 'pencil', 'paper', 'mug'], 'price': [1.2, 1.0, 0.6, 0.9, 1.7]}
    color  object  price
0    blue    ball    1.2
1   green     pen    1.0
2  yellow  pencil    0.6
3     red   paper    0.9
4   white     mug    1.7
```
***
## Slide_20.py

```python
import pandas as pd
import numpy as np

matriz = np.arange(16).reshape((4,4))
frame4 = pd.DataFrame(matriz,

index=['red','blue','yellow','white'],
columns=['ball','pen','pencil','paper'])

print(frame4)


#### Resultado do script 

        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
```
***
## Slide_21.py

```python
import pandas as pd

data = {'color' : ['blue','green','yellow','red','white'],
'object' : ['ball','pen','pencil','paper','mug'],
'price' : [1.2,1.0,0.6,0.9,1.7]}

frame4 = pd.DataFrame(data)

print(frame4.columns)
print(frame4.index)
print(frame4.values)
print(frame4['color'][1])


#### Resultado do script 

Index(['color', 'object', 'price'], dtype='object')
RangeIndex(start=0, stop=5, step=1)
[['blue' 'ball' 1.2]
 ['green' 'pen' 1.0]
 ['yellow' 'pencil' 0.6]
 ['red' 'paper' 0.9]
 ['white' 'mug' 1.7]]
green
```
***
## Slide_22.py

```python
import pandas as pd

data = {'color' : ['blue','green','yellow','red','white'],
'object' : ['ball','pen','pencil','paper','mug'],
'price' : [1.2,1.0,0.6,0.9,1.7]}

frame4 = pd.DataFrame(data)

print(frame4['color'])
print(frame4.loc[2])


#### Resultado do script 

0      blue
1     green
2    yellow
3       red
4     white
Name: color, dtype: object
color     yellow
object    pencil
price        0.6
Name: 2, dtype: object
```
***
## Slide_23.py

```python
import pandas as pd

data = {'color' : ['blue','green','yellow','red','white'],
'object' : ['ball','pen','pencil','paper','mug'],
'price' : [1.2,1.0,0.6,0.9,1.7]}

frame4 = pd.DataFrame(data)
frame4.index.name = 'id';
frame4.columns.name = 'item'

print(frame4)


#### Resultado do script 

item   color  object  price
id                         
0       blue    ball    1.2
1      green     pen    1.0
2     yellow  pencil    0.6
3        red   paper    0.9
4      white     mug    1.7
```
***
## Slide_24.py

```python
import pandas as pd

data = {'color' : ['blue','green','yellow'], 'object' : ['ball','pen','pencil']}

frame4 = pd.DataFrame(data)

print('1a: \n' + str(frame4))

frame4['color'][2] = 'amarelo'

print('\n2a: \n' + str(frame4))

frame4.loc[2,'color'] = 'amarelo2'

print('\n3a: \n' + str(frame4))


#### Resultado do script 

1a: 
    color  object
0    blue    ball
1   green     pen
2  yellow  pencil

2a: 
     color  object
0     blue    ball
1    green     pen
2  amarelo  pencil

3a: 
      color  object
0      blue    ball
1     green     pen
2  amarelo2  pencil
```
***
## Slide_28.py

```python
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)
print(np.sqrt(frame))


#### Resultado do script 

        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
            ball       pen    pencil     paper
red     0.000000  1.000000  1.414214  1.732051
blue    2.000000  2.236068  2.449490  2.645751
yellow  2.828427  3.000000  3.162278  3.316625
white   3.464102  3.605551  3.741657  3.872983
```
***
## Slide_29.py

```python
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)

f = lambda x: x.max() - x.min()

print(frame.apply(f))


#### Resultado do script 

        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
ball      12
pen       12
pencil    12
paper     12
dtype: int64
```
***
## Slide_30.py

```python
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)

f = lambda x: x.max() - x.min()

print(frame.apply(f, axis=1))


#### Resultado do script 

        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
red       3
blue      3
yellow    3
white     3
dtype: int64
```
***
## Slide_31.py

```python
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)
print(frame.sum())
print(frame.mean())


#### Resultado do script 

        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
ball      24
pen       28
pencil    32
paper     36
dtype: int64
ball      6.0
pen       7.0
pencil    8.0
paper     9.0
dtype: float64
```
***
## Slide_32.py

```python
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)
print(frame.sum(axis=1))
print(frame.mean(axis=1))


#### Resultado do script 

        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
red        6
blue      22
yellow    38
white     54
dtype: int64
red        1.5
blue       5.5
yellow     9.5
white     13.5
dtype: float64
```
***
## Slide_33.py

```python
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)
print(frame.describe())


#### Resultado do script 

        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
            ball        pen     pencil      paper
count   4.000000   4.000000   4.000000   4.000000
mean    6.000000   7.000000   8.000000   9.000000
std     5.163978   5.163978   5.163978   5.163978
min     0.000000   1.000000   2.000000   3.000000
25%     3.000000   4.000000   5.000000   6.000000
50%     6.000000   7.000000   8.000000   9.000000
75%     9.000000  10.000000  11.000000  12.000000
max    12.000000  13.000000  14.000000  15.000000
```
***
## Slide_34.py

```python
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)
print(frame.sort_index())


#### Resultado do script 

        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
        ball  pen  pencil  paper
blue       4    5       6      7
red        0    1       2      3
white     12   13      14     15
yellow     8    9      10     11
```
***
## Slide_35.py

```python
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)
print(frame.sort_index(axis=1))


#### Resultado do script 

        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
        ball  paper  pen  pencil
red        0      3    1       2
blue       4      7    5       6
yellow     8     11    9      10
white     12     15   13      14
```
***
## Slide_36.py

```python
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)
frame.loc['yellow', 'pen'] = 30
print(frame)
print(frame.sort_values(by='pen'))


#### Resultado do script 

        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8   30      10     11
white     12   13      14     15
        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
white     12   13      14     15
yellow     8   30      10     11
```
***
## Slide_37.py

```python
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)
print(frame.rank())
print(frame['ball'].rank())


#### Resultado do script 

        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
        ball  pen  pencil  paper
red      1.0  1.0     1.0    1.0
blue     2.0  2.0     2.0    2.0
yellow   3.0  3.0     3.0    3.0
white    4.0  4.0     4.0    4.0
red       1.0
blue      2.0
yellow    3.0
white     4.0
Name: ball, dtype: float64
```
***
## Slide_47.py

```python
import pandas as pd

csv_arq_01 = pd.read_csv('arq_01.csv')

print(csv_arq_01)
print(type(csv_arq_01))


#### Resultado do script 

   white  red  blue  green animal
0      1    5     2      3    cat
1      2    7     8      5    dog
2      3    3     6      7  horse
3      2    2     8      3   duck
4      4    4     2      1  mouse
<class 'pandas.core.frame.DataFrame'>
```
***
## Slide_48.py

```python
import pandas as pd

csv_arq_01 = pd.read_table('arq_01.csv', sep=',')

print(csv_arq_01)
print(type(csv_arq_01))


#### Resultado do script 

   white  red  blue  green animal
0      1    5     2      3    cat
1      2    7     8      5    dog
2      3    3     6      7  horse
3      2    2     8      3   duck
4      4    4     2      1  mouse
<class 'pandas.core.frame.DataFrame'>
```
***
## Slide_50.py

```python
import pandas as pd
import numpy as np

frame2 = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=None,
    columns=['ball', 'pen', 'pencil', 'paper'])

print(frame2)

frame2.to_csv('arq_02.csv', index=None)


#### Resultado do script 

   ball  pen  pencil  paper
0     0    1       2      3
1     4    5       6      7
2     8    9      10     11
3    12   13      14     15
```
***
## Slide_51.py

```python
import pandas as pd

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ranking = pd.read_html('http://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/')

print(ranking[0])


#### Resultado do script 

     Unnamed: 0        Member  Points  Levels
0             1   BrunoOrsini    2075     NaN
1             2     Berserker     700     NaN
2             3  albertosallu     275     NaN
3             4           Jon     180     NaN
4             5          Mr.Y     180     NaN
..          ...           ...     ...     ...
110         111  Gigi Bertana       5     NaN
111         112       p.barut       5     NaN
112         113  Indri4Africa       5     NaN
113         114     ghirograf       5     NaN
114         115  Marco Corbet       5     NaN

[115 rows x 4 columns]
```
***
## Slide_55.py

```python
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

frame = pd.DataFrame( np.arange(20).reshape(4,5),
    columns=['white','red','blue','black','green'])

engine = create_engine('sqlite:///foo.db')

frame.to_sql('colors',engine)

cores = pd.read_sql('colors',engine)

print(engine)
print(cores)


#### Resultado do script 

Engine(sqlite:///foo.db)
   index  white  red  blue  black  green
0      0      0    1     2      3      4
1      1      5    6     7      8      9
2      2     10   11    12     13     14
3      3     15   16    17     18     19
```
***
## Slide_61.py

```python
import pandas as pd
import numpy as np

frame1 = pd.DataFrame({
    'id': ['ball', 'pencil', 'pen', 'mug', 'ashtray'],
    'price': [12.33, 11.44, 33.21, 13.23, 33.62],
})

frame2 = pd.DataFrame({
    'id': ['pencil', 'pencil', 'ball', 'pen'],
    'color': ['white', 'red', 'red', 'black']
})

frame3 = pd.merge(frame1, frame2)

print(frame1)
print(frame2)
print(frame3)



#### Resultado do script 

        id  price
0     ball  12.33
1   pencil  11.44
2      pen  33.21
3      mug  13.23
4  ashtray  33.62
       id  color
0  pencil  white
1  pencil    red
2    ball    red
3     pen  black
       id  price  color
0    ball  12.33    red
1  pencil  11.44  white
2  pencil  11.44    red
3     pen  33.21  black
```
***
## Slide_64.py

```python
import pandas as pd

frame1 = pd.DataFrame({
    'id': ['pencil', 'mug', 'ball', 'pen'],
    'price': [2, 4, 3.4, 1.1]
})

print(frame1, end='\n\n')

frame2 = pd.DataFrame({
    'id': ['pencil', 'mug', 'ball', 'pen'],
    'price': [5, 7, 8.4, 9.1]
})

print(frame2, end='\n\n')

print(pd.concat([frame1, frame2]))



#### Resultado do script 

       id  price
0  pencil    2.0
1     mug    4.0
2    ball    3.4
3     pen    1.1

       id  price
0  pencil    5.0
1     mug    7.0
2    ball    8.4
3     pen    9.1

       id  price
0  pencil    2.0
1     mug    4.0
2    ball    3.4
3     pen    1.1
0  pencil    5.0
1     mug    7.0
2    ball    8.4
3     pen    9.1
```
***
