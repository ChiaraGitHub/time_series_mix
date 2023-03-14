## Time series

### AR: Autoregressive
The parameter p determines the number of past samples that we consider.
AR(0): the series is just white noise.
AR(1): the series is a random walk if $\alpha$ is 1. If it is between 0 and 1 the time series
exhibits mean reversion.

$$y_t=c \color{blue} + \sum_{n=1}^{p} \alpha_n y_{t-n} \color{black} + \epsilon_t$$

### MA: Moving Average
The parameter q is the number of previous white noise terms considered.

$$y_t=c \color{green} + \sum_{n=1}^q \theta_n \epsilon_{t-n} \color{black}+\epsilon_t$$

### ARMA / ARIMA: Autoregressive + Moving Average (+ Integrated part)
The term I refers to how many times the series has been differenced to achieve stationarity.
An ARIMA model is simply an ARMA model on the differenced time series.

$$y_t=c \color{blue} + \sum_{n=1}^p \alpha_n y_{t-n} \color{green} + \sum_{n=1}^q \theta_n \epsilon_{t-n} \color{black} +\epsilon_t$$

### SARIMA
ARIMA that includes additional autoregressive and moving average components. 
These additional lags are offset by the frequency of the seasonaility (sn). 

$$y_t=c \color{blue} + \sum_{n=1}^p \alpha_n y_{t-n} \color{green} +\sum_{n=1}^q \theta_n \epsilon_{t-n} \color{orange} +\sum_{n=1}^P \phi_n y_{t-s n} + \sum_{n=1}^Q \eta_n \epsilon_{t-s n}\color{black} + \epsilon_t$$

### ARIMAX / SARIMAX
They take into account exogenous variables.

$$y_t=c \color{blue} + \sum_{n=1}^p \alpha_n y_{t-n} \color{green} + \sum_{n=1}^q \theta_n \epsilon_{t-n} \color{red} + \sum_{n=1}^r \beta_n x_{n_t} \color{orange} + \sum_{n=1}^P \phi_n y_{t-s n} + \sum_{n=1}^Q \eta_n \epsilon_{t-s n} \color{black} + \epsilon_t$$

### Augmented Dickey-Fuller (ADF) Test
To determine if the time series is stationary. For the data to be stationary (so to
reject the null hypothesis) the ADF test should have a p-value <= a significance value
to be set.
Null Hypothesis: The data is not stationary.
Alternative Hypothesis: The data is stationary.

### Useful Plots
- The standard residual plot: should have mean zero and uniform variance
- Histogram and KDE estimate: the KDE estimate should be close to the normal distribution
- Normal q-q: most of the points should lie on the straight line
- Correlogram / ACF plot: for lag > 0, 95% of the correlations should not be significant

Useful resources:

- https://towardsdatascience.com/time-series-forecasting-with-arima-sarima-and-sarimax-ee61099e78f6
- https://sailajakarra.medium.com/time-series-predictions-using-arima-sarimax-e6724844cae0
