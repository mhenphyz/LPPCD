import pandas as pd

data = {'color' : ['blue','green','yellow'], 'object' : ['ball','pen','pencil']}

frame4 = pd.DataFrame(data)

print('1a: \n' + str(frame4))

frame4['color'][2] = 'amarelo'

print('\n2a: \n' + str(frame4))

frame4.loc[2,'color'] = 'amarelo2'

print('\n3a: \n' + str(frame4))