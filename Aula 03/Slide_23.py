import pandas as pd

data = {'color' : ['blue','green','yellow','red','white'],
'object' : ['ball','pen','pencil','paper','mug'],
'price' : [1.2,1.0,0.6,0.9,1.7]}

frame4 = pd.DataFrame(data)
frame4.index.name = 'id';
frame4.columns.name = 'item'

print(frame4)