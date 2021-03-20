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