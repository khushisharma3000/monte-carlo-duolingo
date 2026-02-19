# monte-carlo-duolingo
A Python simulation exploring potential price paths for DUOL stock.

# Duolingo Monte Carlo Simulation
This project uses Python to simulate 50 potential future price paths for **DUOL** stock over the next year.

## How it works
- **Data Source:** Real historical data from `yfinance`.
- **Model:** Geometric Brownian Motion (GBM).
- **Variables:** Uses current volatility ($\sigma$) and expected return ($\mu$).

## Requirements
`pip install numpy pandas yfinance matplotlib`
