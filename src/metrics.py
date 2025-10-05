import numpy as np
import pandas as pd
from math import sqrt
from scipy.stats import norm

def lift_and_se(df, outcome='y', group='group', treat_label='treatment', ctrl_label='control'):
    g = df.groupby(group)[outcome].agg(['mean','var','count']).rename(
        index={treat_label:'treat', ctrl_label:'ctrl'}
    )
    m_t, v_t, n_t = g.loc['treat']
    m_c, v_c, n_c = g.loc['ctrl']
    lift_abs = m_t - m_c
    se = sqrt(v_t/n_t + v_c/n_c)
    return lift_abs, se

def z_test(df, outcome='y', group='group', treat_label='treatment', ctrl_label='control', alpha=0.05):
    lift, se = lift_and_se(df, outcome, group, treat_label, ctrl_label)
    z = 0.0 if se == 0 else lift / se
    p_two = 2*(1 - norm.cdf(abs(z)))
    ci = (lift - norm.ppf(1-alpha/2)*se, lift + norm.ppf(1-alpha/2)*se)
    return {'lift': lift, 'se': se, 'z': z, 'p': p_two, 'ci': ci}
