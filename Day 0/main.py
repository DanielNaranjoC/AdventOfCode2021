import pandas as pd
data = pd.read_csv('input.txt', header=None)
d = data.diff().dropna()
print('Lager: ', (d > 0).sum().iloc[0])

