
\"\"\"Compute VaR and Expected Shortfall using Monte‑Carlo simulation.\"\"\"

import numpy as np

def simulate_returns(mu: float, sigma: float, horizon: float, N: int):
    \"\"\"Simulate log‑returns over the given horizon (in years).\"\"\"
    return np.random.normal(loc=mu * horizon, scale=sigma * np.sqrt(horizon), size=N)

def var_es(returns, alpha=0.95):
    \"\"\"Compute Value‑at‑Risk and Expected Shortfall (in linear % loss).\"\"\"
    losses = -returns  # loss = –return
    var = np.percentile(losses, alpha * 100)
    es = losses[losses >= var].mean()
    return var, es

if __name__ == "__main__":
    simulated = simulate_returns(mu=0.08, sigma=0.2, horizon=1/252, N=100_000)
    var, es = var_es(simulated, alpha=0.95)
    print(f"95% one‑day VaR  = {var*100:.2f}%")
    print(f"95% Expected Shortfall = {es*100:.2f}%")
