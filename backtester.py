import pandas as pd

def run_backtest(df: pd.DataFrame, stock1: str, stock2: str, capital: float = 10000):
    df = df.copy()  # FIXED bug

    df["Return1"] = df[stock1].pct_change()
    df["Return2"] = df[stock2].pct_change()
    df["Position"] = df["Signal"].shift()

    df["StrategyReturn"] = df["Position"] * (df["Return1"] - df["Return2"])
    df["CumulativeReturn"] = (1 + df["StrategyReturn"].fillna(0)).cumprod() * capital

    return df[["StrategyReturn", "CumulativeReturn"]]
