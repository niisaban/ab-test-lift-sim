import numpy as np
import pandas as pd

def simulate_ab(n=10000, p_ctrl=0.10, lift_abs=0.01, seed=42, cov_effect=0.15):
    """Simulate an A/B test with a binary conversion.
    Adds a pre-experiment covariate X_pre correlated with outcome (for CUPED).
    - n: total samples split 50/50.
    - p_ctrl: baseline conversion prob in control.
    - lift_abs: absolute lift added to treatment prob.
    - cov_effect: correlation strength between X_pre and Y.
    Returns: DataFrame with columns [group, X_pre, y].
    """
    rng = np.random.default_rng(seed)
    group = rng.choice(['control','treatment'], size=n, p=[0.5,0.5])
    x_pre = rng.normal(0, 1, size=n)

    p_treat = p_ctrl + lift_abs
    p = np.where(group=='control', p_ctrl, p_treat)

    # introduce correlation between X_pre and Y by shifting logits
    # map x_pre -> small prob shift via logistic link
    logits = np.log(p/(1-p)) + cov_effect * x_pre
    p_adj = 1/(1+np.exp(-logits))

    y = rng.binomial(1, p_adj, size=n)
    return pd.DataFrame({'group': group, 'X_pre': x_pre, 'y': y})
