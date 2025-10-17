import numpy as np

def test_cuped_reduces_standard_error_deterministically():
    rng = np.random.default_rng(12345)
    n = 50000  # big sample = stable CI runs
    x_pre = rng.normal(0, 1, n)              # pre-experiment covariate
    noise = rng.normal(0, 1, n)
    y = 0.5 * x_pre + noise                  # outcome correlated with x_pre (rho≈0.45–0.5)

    # CUPED adjustment: theta = Cov(Y, X_pre)/Var(X_pre)
    theta = np.cov(y, x_pre, ddof=1)[0, 1] / np.var(x_pre, ddof=1)
    y_adj = y - theta * (x_pre - x_pre.mean())

    se_naive = np.std(y, ddof=1) / np.sqrt(n)
    se_cuped = np.std(y_adj, ddof=1) / np.sqrt(n)

    # With rho≈0.5, expected SD reduction ≈ sqrt(1 - rho^2) ≈ 0.87
    # Assert a clear win with slack for numeric noise.
    assert se_cuped <= se_naive * 0.90

