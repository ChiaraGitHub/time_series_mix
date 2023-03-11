def compute_moving_mean(data, column_name, window):

    moving_mean = data[column_name].rolling(window=window).mean()

    return moving_mean

def compute_moving_std(data, column_name, window):

    moving_std = data[column_name].rolling(window=window).std()

    return moving_std