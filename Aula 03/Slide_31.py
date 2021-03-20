import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

print(frame)
print(frame.sum())
print(frame.mean())