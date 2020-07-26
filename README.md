# timeseries_LSTM

This implementation predicted a number of timeseries data using LSTM.

# Preprocessing
Preprocessing example shows Hampel filter and Exponential smoothing 
in order to delete outlier.

-original

<img src="https://github.com/ashimy/timeseries_LSTM/blob/master/image/image.png" width="640px">

-Hampel

<img src="https://github.com/ashimy/timeseries_LSTM/blob/master/image/image_hampel.png" width="640px">

-Exponential smoothing

<img src="https://github.com/ashimy/timeseries_LSTM/blob/master/image/image_exponential.png" width="640px">


# Preprocessing
Preprocessed data conducted standarization using MinMaxScaler function. Model's loss function set mean_squared_error
and adam optimizer.
