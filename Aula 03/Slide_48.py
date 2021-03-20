import pandas as pd

csv_arq_01 = pd.read_table('arq_01.csv', sep=',')

print(csv_arq_01)
print(type(csv_arq_01))