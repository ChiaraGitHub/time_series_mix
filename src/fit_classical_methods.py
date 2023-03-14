from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import pmdarima as pm
import pandas as pd

def autoregressive(data, column_name, lags=2):
    """
    Auto-Regressive
    """
    
    model = AutoReg(data[column_name], lags=lags)
    model_fit = model.fit()

    return model_fit

def arima(data, column_name, order):
    """
    Auto-Regressive Integrated Moving Average
    """

    model = ARIMA(data[column_name], order=order)
    model_fit = model.fit()

    return model_fit

def sarimax(data, column_name, order, seasonal_order):
    
    model = SARIMAX(data[column_name], order=order, seasonal_order=seasonal_order)
    model_fit = model.fit(disp=0)

    return model_fit

def holt_winter(data, column_name):
    model = ExponentialSmoothing(data[column_name])
    model_fit = model.fit()

    return model_fit

def auto_arima(data, column_name):
    
    ARIMA_model = pm.auto_arima(data[column_name], 
                        start_p=1, 
                        start_q=1,
                        test='adf', # use adftest to find optimal 'd'
                        max_p=3,
                        max_q=3, # maximum p and q
                        m=1, # frequency of series (if m==1, seasonal is set to FALSE automatically)
                        d=None,# let model determine 'd'
                        seasonal=False, # No Seasonality for standard ARIMA
                        trace=False, #logs 
                        error_action='warn', #shows errors ('ignore' silences these)
                        suppress_warnings=True,
                        stepwise=True)
    return ARIMA_model

def auto_sarima(data, column_name):

    # Seasonal - fit stepwise auto-ARIMA
    SARIMA_model = pm.auto_arima(
                                data[column_name],
                                start_p=1,
                                start_q=1,
                                test='adf',
                                max_p=3,
                                max_q=3, 
                                m=12, #12 is the frequncy of the cycle
                                start_P=0, 
                                seasonal=True, #set to seasonal
                                d=None, 
                                D=1, #order of the seasonal differencing
                                trace=False,
                                error_action='ignore',  
                                suppress_warnings=True, 
                                stepwise=True)
    return SARIMA_model

def auto_sarimax(data, column_name):

    #adding exogenous variable
    data['index'] = data.index.month

    # SARIMAX Model
    SARIMAX_model = pm.auto_arima(
                                data[[column_name]], 
                                exogenous=data[['index']], # New
                                start_p=1,
                                start_q=1,
                                test='adf',
                                max_p=3,
                                max_q=3,
                                m=12,
                                start_P=0,
                                seasonal=True,
                                d=None,
                                D=1, 
                                trace=False,
                                error_action='ignore',  
                                suppress_warnings=True, 
                                stepwise=True)
    
    return SARIMAX_model

def forecast(data, column_name, model, n_periods=24, exogenous=None):
    
    # Forecast
    fitted, confidence_interval = model.predict(n_periods=n_periods,
                                                return_conf_int=True,
                                                exogenous=exogenous)
    # Future dates
    index_of_fc = pd.date_range(data.index[-1] + pd.DateOffset(months=1), 
                                periods=n_periods,
                                freq='MS')

    # Create series for plotting purpose
    fitted_series = pd.Series(fitted, index=index_of_fc)
    lower_series = pd.Series(confidence_interval[:, 0], index=index_of_fc)
    upper_series = pd.Series(confidence_interval[:, 1], index=index_of_fc)

    return (fitted_series, lower_series, upper_series)