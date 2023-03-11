## Time series

<img src="https://render.githubusercontent.com/render/math?math=e^{i \pi} = -1">

AR: Autoregressive

$
y_t=c \color{steelblue} + \sum_{n=1}^p \alpha_n y_{t-n} \color{default}+\epsilon_t
$

MA: Moving Average

$
y_t=c \color{darkgreen} + \sum_{n=1}^q \theta_n \epsilon_{t-n} \color{default}+\epsilon_t
$

ARMA / ARIMA: Autoregressive + Moving Average (+ Integrated part)
The term I refers to how many times the series has been differenced to achieve stationarity.

$
y_t=c \color{steelblue} + \sum_{n=1}^p \alpha_n y_{t-n} \color{darkgreen} + \sum_{n=1}^q \theta_n \epsilon_{t-n} \color{default} +\epsilon_t
$

SARIMA: ARIMA that includes additional autoregressive and moving average components. The lags are offset by the frequency of the seasonaility. 

$
y_t=c \color{steelblue} + \sum_{n=1}^p \alpha_n y_{t-n} \color{darkgreen} +\sum_{n=1}^q \theta_n \epsilon_{t-n} \color{orange} +\sum_{n=1}^P \phi_n y_{t-s n} + \sum_{n=1}^Q \eta_n \epsilon_{t-s n}\color{default} + \epsilon_t
$

ARIMAX / SARIMAX: They take into account exogenous variables.

$
y_t=c \color{steelblue} + \sum_{n=1}^p \alpha_n y_{t-n} \color{darkgreen} + \sum_{n=1}^q \theta_n \epsilon_{t-n} \color{darkred} + \sum_{n=1}^r \beta_n x_{n_t} \color{orange} + \sum_{n=1}^P \phi_n y_{t-s n} + \sum_{n=1}^Q \eta_n \epsilon_{t-s n} \color{default} + \epsilon_t
$


Useful resources:

- https://towardsdatascience.com/time-series-forecasting-with-arima-sarima-and-sarimax-ee61099e78f6