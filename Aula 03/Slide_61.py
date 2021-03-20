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
