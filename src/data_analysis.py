import pandas as pd
from statsmodels.tsa.stattools import adfuller

def compute_moving_mean(data, column_name, window):

    moving_mean = data[column_name].rolling(window=window).mean()

    return moving_mean

def compute_moving_std(data, column_name, window):

    moving_std = data[column_name].rolling(window=window).std()

    return moving_std

def adf_test(data, column_name):

    dftest = adfuller(data[column_name], autolag='AIC')
    dfoutput = pd.Series(dftest[0:4],
                         index=['Test Statistic',
                                'p-value',
                                '#Lags Used',
                                'Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    return dfoutput