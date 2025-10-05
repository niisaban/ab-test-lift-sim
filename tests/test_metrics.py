import pandas as pd
from src.simulate import simulate_ab
from src.metrics import z_test

def test_z_test_runs():
    df = simulate_ab(n=2000, seed=0)
    res = z_test(df)
    assert 'lift' in res and 'se' in res and 'p' in res
    assert 0 <= res['p'] <= 1
