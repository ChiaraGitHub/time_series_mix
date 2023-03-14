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

def viz_multiple_time_series(data: pd.DataFrame,
                             columns: list,
                             title='', xlabel='', ylabel=''):

    plt.figure(figsize=(10,3))
    for c in columns:
        plt.plot(data[c], label=c)
    plt.legend(columns, loc='best')
    plt.grid()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def plot_forecast(data, column_name, fitted_series, lower_series, upper_series):
    # Plot
    plt.figure(figsize=(13,4))
    plt.plot(data[column_name], '--b')
    plt.plot(fitted_series, '.--g')
    plt.fill_between(lower_series.index, 
                     lower_series, 
                     upper_series, 
                     color='k',
                     alpha=.15) # Transparency

    plt.title("Historical Data and Forecast")
    plt.grid()
    plt.show()