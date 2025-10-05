import numpy as np
import pandas as pd

def cuped_adjust(df, outcome='y', covariate='X_pre'):
    x = df[covariate].values
    y = df[outcome].values
    theta = np.cov(y, x, ddof=1)[0,1] / np.var(x, ddof=1)
    y_adj = y - theta * (x - x.mean())
    out = df.copy()
    out[outcome + '_adj'] = y_adj
    return out, theta
