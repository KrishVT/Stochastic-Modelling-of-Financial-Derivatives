
\"\"\"Geometric Brownian Motion option pricing via Euler–Maruyama Monte‑Carlo.\"\"\"

import numpy as np
from scipy.stats import norm

__all__ = ["simulate_gbm", "monte_carlo_call_price", "black_scholes_call_price"]

def simulate_gbm(S0: float, mu: float, sigma: float, T: float, N: int, n_steps: int = 252):
    \"\"\"Simulate N sample paths of GBM using Euler–Maruyama.
    Returns (times, paths) where paths has shape (N, n_steps+1).\"\"\"
    dt = T / n_steps
    times = np.linspace(0, T, n_steps + 1)
    S = np.empty((N, n_steps + 1))
    S[:, 0] = S0
    for t in range(1, n_steps + 1):
        z = np.random.normal(size=N)
        S[:, t] = S[:, t - 1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)
    return times, S

def monte_carlo_call_price(S0: float, K: float, T: float, r: float, sigma: float, n_paths: int = 100_000):
    \"\"\"Estimate European call option price under GBM via Monte‑Carlo.\"\"\"
    _, paths = simulate_gbm(S0, r, sigma, T, n_paths, n_steps=1)  # simulate terminal price directly
    payoff = np.maximum(paths[:, -1] - K, 0)
    discounted_payoff = np.exp(-r * T) * payoff
    return discounted_payoff.mean(), discounted_payoff.std(ddof=1) / np.sqrt(n_paths)

def black_scholes_call_price(S0: float, K: float, T: float, r: float, sigma: float):
    \"\"\"Analytical Black–Scholes call price.\"\"\"
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

if __name__ == "__main__":
    price_mc, se = monte_carlo_call_price(100, 110, 1.0, 0.05, 0.2, n_paths=200_000)
    price_bs = black_scholes_call_price(100, 110, 1.0, 0.05, 0.2)
    print(f"Monte‑Carlo price = {price_mc:.4f}  (SE={se:.4f})")
    print(f"Black–Scholes  price = {price_bs:.4f}")
    print(f"Deviation = {abs(price_mc - price_bs) / price_bs * 100:.2f}%")
