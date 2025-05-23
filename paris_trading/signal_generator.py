import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def calculate_spread_zscore(data):
    """
    Calculates hedge ratio (beta), spread, and z-score between two stocks.
    """
    stock1 = data.columns[0]
    stock2 = data.columns[1]

    X = data[stock2].values.reshape(-1, 1)
    y = data[stock1].values

    model = LinearRegression().fit(X, y)
    beta = model.coef_[0]

    spread = data[stock1] - beta * data[stock2]
    zscore = (spread - spread.mean()) / spread.std()

    result = pd.DataFrame({
        stock1: data[stock1],
        stock2: data[stock2],
        "Spread": spread,
        "ZScore": zscore
    })

    return result, beta

def generate_signals(zscore_series, entry_threshold=1.0, exit_threshold=0.5):
    """
    Generates trading signals based on z-score thresholds.
    1 = Long stock1 / Short stock2
    -1 = Short stock1 / Long stock2
     0 = Exit or hold
    """
    signals = []
    position = 0

    for z in zscore_series:
        if z > entry_threshold and position != -1:
            signals.append(-1)  # Short stock1, long stock2
            position = -1
        elif z < -entry_threshold and position != 1:
            signals.append(1)   # Long stock1, short stock2
            position = 1
        elif abs(z) < exit_threshold:
            signals.append(0)   # Exit
            position = 0
        else:
            signals.append(position)  # Hold

    return signals
