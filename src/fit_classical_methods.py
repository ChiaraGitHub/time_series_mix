from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def autoregressive(data, lags=2):
    """
    Auto-Regressive
    """
    
    model = AutoReg(data, lags=lags)
    model_fit = model.fit()

    return model_fit

def arima(data, order):
    """
    Auto-Regressive Integrated Moving Average
    """

    model = ARIMA(data, order=order)
    model_fit = model.fit()

    return model_fit

def sarimax(data, order, seasonal_order):
    
    model = SARIMAX(data, order=order, seasonal_order=seasonal_order)
    model_fit = model.fit(disp=0)

    return model_fit

def holt_winter(data):
    model = ExponentialSmoothing(data)
    model_fit = model.fit()

    return model_fit
