import yfinance as yf
import pandas as pd

def load_fb_close_stock_price():
    
    data = yf.download('META', start='2011-1-1', end='2021-1-1')
    
    return data[["Close"]]

def load_air_passangers_data():

    data = pd.read_csv("https://raw.githubusercontent.com/AileenNielsen/TimeSeriesAnalysisWithPython/master/data/AirPassengers.csv")

    #string to date format
    data['Month'] = pd.to_datetime(data['Month'], infer_datetime_format=True)
    data = data.set_index(['Month'])
    
    return data
