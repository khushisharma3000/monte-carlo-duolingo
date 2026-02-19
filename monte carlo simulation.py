import numpy as np 
import matplotlib.pyplot as plt 

S0 = 312
mu = 0.25 
sigma = 0.45
T = 1 
dt = 1/252
N = int(T/dt)
simulations = 50


for i in range(simulations):
    prices = [S0]
    for _ in range(N):
        shock = np.random.normal(loc=(mu*dt), scale=(sigma*np.sqrt(dt)))
        prices.append(prices[-1] * np.exp(shock))
    
    # This plots each individual line to the same background
    plt.plot(prices)

# EVERYTHING BELOW MUST BE OUTDENTED (All the way to the left)
plt.title("Monte Carlo Stock Price Simulation")
plt.xlabel("Days")
plt.ylabel("Price")
plt.show() # This opens the window only after ALL lines are drawn

