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
