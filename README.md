# Stochastic Modelling of Financial Derivatives

## Overview

| Script | Key Techniques | What it Demonstrates |
| ------ | -------------- | -------------------- |
| `gbm_option_pricing.py` | Euler–Maruyama, Geometric Brownian Motion (GBM), Monte‑Carlo pay‑off estimation | European option pricing under Black–Scholes dynamics |
| `markov_martingale.py` | Discrete‑time Markov Chains, Martingales | Convergence to steady‑state distribution within 20 iterations |
| `heston_calibration.py` | Heston stochastic volatility model, Monte‑Carlo simulation, least‑squares calibration | Calibrating model parameters to market option prices with <2.5% error |
| `risk_metrics.py` | Historical / Monte‑Carlo simulation | Value‑at‑Risk (VaR) and Expected Shortfall (ES) with 95% confidence |
| `black_scholes_monte_carlo.py` | Analytical Black–Scholes–Merton formula & Monte‑Carlo | Consistency check achieving <3% deviation |
