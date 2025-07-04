
\"\"\"Black–Scholes analytical vs Monte‑Carlo pricing comparison.\"\"\"

from gbm_option_pricing import monte_carlo_call_price, black_scholes_call_price

if __name__ == "__main__":
    S0, K, T, r, sigma = 100, 110, 1.0, 0.05, 0.2
    price_mc, se = monte_carlo_call_price(S0, K, T, r, sigma, n_paths=200_000)
    price_bs = black_scholes_call_price(S0, K, T, r, sigma)
    print(f"Monte‑Carlo price = {price_mc:.4f}  (SE={se:.4f})")
    print(f"Black–Scholes  price = {price_bs:.4f}")
    print(f"Deviation = {abs(price_mc - price_bs) / price_bs * 100:.2f}%")
