from src.simulate import simulate_ab
from src.metrics import z_test
from src.cuped import cuped_adjust
from src.power import required_sample_size

def main():
    df = simulate_ab(n=20000, p_ctrl=0.12, lift_abs=0.008, seed=7, cov_effect=0.20)
    print("=== Naive analysis ===")
    res = z_test(df)
    print(res)

    print("\n=== CUPED-adjusted analysis ===")
    df2, theta = cuped_adjust(df)
    res2 = z_test(df2.rename(columns={'y_adj':'y'}))  # reuse function by renaming
    print({"theta": theta, **res2})

    print("\n=== Power / sample size (per group) ===")
    n_a, n_b = required_sample_size(p_ctrl=0.12, lift_abs=0.008, alpha=0.05, power=0.8)
    print({"control": n_a, "treatment": n_b})

if __name__ == "__main__":
    main()
