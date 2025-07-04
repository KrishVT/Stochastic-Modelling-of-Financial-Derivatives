
\"\"\"Markov chain convergence and martingale demonstration.\"\"\"

import numpy as np

def example_transition_matrix():
    \"\"\"Return a simple 3‑state ergodic transition matrix.\"\"\"
    return np.array([[0.7, 0.2, 0.1],
                     [0.1, 0.6, 0.3],
                     [0.2, 0.3, 0.5]])

def steady_state(P, tol=1e-8, max_iter=1000):
    \"\"\"Iterate π_{n+1} = π_n P until convergence (L1 norm).\"\"\"
    n_states = P.shape[0]
    pi = np.ones(n_states) / n_states
    for i in range(max_iter):
        pi_next = pi @ P
        if np.linalg.norm(pi_next - pi, ord=1) < tol:
            return pi_next, i + 1
        pi = pi_next
    raise RuntimeError("Did not converge")

def is_martingale(X):
    \"\"\"Empirical martingale check: E[X_{n+1}] ≈ E[X_n].\"\"\"
    return np.allclose(X[1:].mean(), X[:-1].mean(), atol=1e-2)

if __name__ == "__main__":
    P = example_transition_matrix()
    pi, iters = steady_state(P)
    print(f"Converged to steady‑state in {iters} iterations: {pi}")
    # Simple fair‑game martingale
    X = np.random.choice([-1, 1], size=1000).cumsum()
    print("Sample path martingale check:", is_martingale(X))
