from src.simulate import simulate_ab
from src.cuped import cuped_adjust
from src.metrics import z_test

def test_cuped_reduces_se_on_avg():
    df = simulate_ab(n=5000, seed=123, cov_effect=0.25)
    naive = z_test(df)
    df2, _ = cuped_adjust(df)
    cuped = z_test(df2.rename(columns={'y_adj':'y'}))
    # CUPED should not increase SE materially; allow tiny numerical wiggle
    assert cuped['se'] <= naive['se'] * 1.02 + 1e-9

