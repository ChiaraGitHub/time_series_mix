import pandas as pd
import matplotlib.pyplot as plt

def viz_time_series(data: pd.DataFrame,
                    title='', xlabel='', ylabel=''):

    plt.figure(figsize=(10,3))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(data)
    plt.grid()
    plt.show()