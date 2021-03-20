import pandas as pd
import numpy as np

matriz = np.arange(16).reshape((4,4))
frame4 = pd.DataFrame(matriz,

index=['red','blue','yellow','white'],
columns=['ball','pen','pencil','paper'])

print(frame4)