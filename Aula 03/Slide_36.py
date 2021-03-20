import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)
frame.loc['yellow', 'pen'] = 30
print(frame)
print(frame.sort_values(by='pen'))