import pandas as pd
import numpy as np

frame2 = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=None,
    columns=['ball', 'pen', 'pencil', 'paper'])

print(frame2)

frame2.to_csv('arq_02.csv', index=None)