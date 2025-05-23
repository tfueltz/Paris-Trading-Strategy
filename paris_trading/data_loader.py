import yfinance as yf
import pandas as pd

def download_data(tickers, start_date, end_date):

    """
    This downloads close price data for a stock in a date range
    """

    data = yf.download(tickers, start=start_date, end=end_date)
    data = data["Close"]
    data = data.dropna()
    return data
