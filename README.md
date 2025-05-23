# Paris-Trading-Strategy
Mean-reversion strategy using pairs trading on KO and PEP

This project uses a simple mean reversion paris trading strategy using KO and PEP due to their relation

This project uses:
- Historical data from the yfinace api
- statistical regression to estimate hedge ratio
- Z-Score to idetify trading signals
- Backtesting to simulate performance
- Matplotlib plots for price, z-score, and equity curve

Strategy:
- Long KO, short PEP when spread z-score < 1
- Short KO, long PEP when z-score > -1
- Exit or hold when = 0

Performance:
- With backtesting this strategy with KO and PEP made profit while earlier testing with NVDA and AMD lost

Main script:
- run_paris_trading.py

paris_trading/
- data_loader.py # Fetch historical prices
- signal_generator.py # Spread, beta, z-score, signals
- backtester.py # Strategy returns and equity curve

Dependencies:
- pandas
- numpy
- yfinance
- matplotlib
- scikit-learn
