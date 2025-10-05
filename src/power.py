from math import sqrt
from scipy.stats import norm

def required_sample_size(p_ctrl=0.10, lift_abs=0.01, alpha=0.05, power=0.8, allocation=0.5):
    """Two-sample proportions test (normal approx), equal variance pooling skipped for simplicity.
    Returns per-group sample size.
    """
    z_alpha = norm.ppf(1 - alpha/2)
    z_beta = norm.ppf(power)
    p_t = p_ctrl + lift_abs
    var = p_ctrl*(1-p_ctrl) + p_t*(1-p_t)
    n = ((z_alpha + z_beta)**2 * var) / (lift_abs**2)
    # split by allocation (default 50/50)
    return int(n * allocation), int(n * (1-allocation))
