import pandas as pd
import numpy as np

s2 = pd.Series([5,-3,np.NaN,14])

print(s2.isnull())