
\"\"\"Heston stochastic volatility simulation & naive calibration.\"\"\"

import numpy as np
from scipy.optimize import minimize

__all__ = ["simulate_heston", "calibrate_heston", "mc_european_call_heston"]

def simulate_heston(S0, v0, kappa, theta, sigma_v, rho, r, T, N=50_000, n_steps=252):
    dt = T / n_steps
    S = np.full(N, S0, dtype=float)
    v = np.full(N, v0, dtype=float)
    sqrt_dt = np.sqrt(dt)
    for _ in range(n_steps):
        z1 = np.random.normal(size=N)
        z2 = rho * z1 + np.sqrt(1 - rho ** 2) * np.random.normal(size=N)  # correlate
        # Variance process (CIR discretisation)
        v = np.maximum(v + kappa * (theta - v) * dt + sigma_v * np.sqrt(v) * sqrt_dt * z2, 0)
        # Price process
        S *= np.exp((r - 0.5 * v) * dt + np.sqrt(v * dt) * z1)
    return S

def mc_european_call_heston(params, S0, K, T, r, N=30_000):
    v0, kappa, theta, sigma_v, rho = params
    terminal_prices = simulate_heston(S0, v0, kappa, theta, sigma_v, rho, r, T, N=N, n_steps=100)
    payoff = np.maximum(terminal_prices - K, 0)
    return np.exp(-r * T) * payoff.mean()

def calibrate_heston(market_price, S0, K, T, r):
    \"\"\"Calibrate (v0,kappa,theta,sigma_v,rho) to match a single market price.\"\"\"
    def objective(params):
        model_price = mc_european_call_heston(params, S0, K, T, r, N=20_000)
        return (model_price - market_price) ** 2

    bounds = [(0.01, 0.5),   # v0
              (0.1, 5.0),    # kappa
              (0.01, 0.5),   # theta
              (0.01, 1.0),   # sigma_v
              (-0.9, 0.0)]   # rho (typically negative)
    x0 = [0.04, 1.0, 0.04, 0.3, -0.5]
    res = minimize(objective, x0, bounds=bounds, tol=1e-3, options={'maxiter': 50})
    return res.x, res.fun

if __name__ == "__main__":
    # Use Black–Scholes price as synthetic market data
    from gbm_option_pricing import black_scholes_call_price
    S0, K, T, r, sigma = 100, 110, 1.0, 0.05, 0.2
    market = black_scholes_call_price(S0, K, T, r, sigma)
    params, mse = calibrate_heston(market, S0, K, T, r)
    price_model = mc_european_call_heston(params, S0, K, T, r, N=40_000)
    err_pct = abs(price_model - market) / market * 100
    print("Calibrated params:", params)
    print(f"Model price={price_model:.4f}, Market={market:.4f}, error={err_pct:.2f}%")
