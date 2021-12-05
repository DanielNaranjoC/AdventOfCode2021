import pandas as pd


def count_one(data_read: pd.DataFrame):
    d = data.diff().dropna()
    return (d > 0).sum().iloc[0]


def count_measurement(data_read: pd.DataFrame, measure=3):
    measurement = []
    for j in range(len(data) - measure + 1):
        measurement.append(data.iloc[j:j + measure, 0].sum())
    measurement = pd.Series(measurement)
    d1 = measurement.diff().dropna()
    return (d1 > 0).sum()


data = pd.read_csv('input.txt', header=None)
print('Individual lager: ', count_one(data))
print('Three-measurement lager: ', count_measurement(data))
