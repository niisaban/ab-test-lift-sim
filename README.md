[![CI](https://github.com/niisaban/ab-test-lift-sim/actions/workflows/ci.yml/badge.svg)](https://github.com/niisaban/ab-test-lift-sim/actions/workflows/ci.yml)


# A/B Test Lift — Simulation & Analysis

**A/B = "A versus B", aka controlled online experiment**.  
This mini‑project lets you **simulate** experiments, run **power analyses**, apply **CUPED** (Controlled Pre‑Experiment Data) variance reduction, and compute **lift** with statistical tests.

## Why this repo
- Practice end‑to‑end: simulate → analyze → interpret → write up.
- Show **reproducible** DS craft (tests, CI, clean `src/`).
- Prep for interviews: power, guardrails, CUPED, heterogeneity.

## Quickstart
```bash
# (Recommended) Python 3.11+
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run a small demo (simulate + analyze)
python scripts/run_demo.py

# Run tests
pytest -q
```
### Run tests locally

#### Windows (PowerShell, current session)
```powershell
# Expose repo root to Python for this shell session
$env:PYTHONPATH = (Get-Location).Path
pytest -q --maxfail=1 -ra

# Expose repo root to Python for this shell session
export PYTHONPATH="$PWD"
pytest -q --maxfail=1 -ra

:: Expose repo root to Python for this CMD session
set PYTHONPATH=%CD%

:: Run tests (quiet; stop early; show failure summary)
pytest -q --maxfail=1 -ra


## Project Structure
```
ab-test-lift-sim/
├─ src/
│  ├─ simulate.py         # traffic & conversions generator (+ covariate for CUPED)
│  ├─ metrics.py          # lift, SE, z-test / Welch t-test
│  ├─ cuped.py            # CUPED theta, adjusted outcome
│  └─ power.py            # sample-size & detectable-effect calculators
├─ scripts/
│  └─ run_demo.py         # CLI demo tying it all together
├─ tests/
│  ├─ test_metrics.py
│  └─ test_cuped.py
├─ data/
│  └─ README.md
├─ requirements.txt
├─ .github/workflows/ci.yml
└─ README.md
```

## Concepts (expanded)
- **Lift**: difference in mean outcome between Treatment and Control (absolute or relative).
- **Power analysis**: probability of detecting a true effect; trades off effect size, variance, alpha, and sample size.
- **CUPED**: variance reduction using a pre‑experiment covariate `X_pre`:  
  θ = Cov(Y, X_pre) / Var(X_pre), and `Y_adj = Y - θ(X_pre - mean(X_pre))`.
- **Guardrail metrics**: KPIs you ensure don’t degrade (e.g., latency, cancellation rate).

## What to practice / document
- State a **clear hypothesis** and primary metric.
- Check **randomization balance**; monitor **SRM** (sample‑ratio mismatch).
- Report **CIs**, **p‑values**, and practical impact (e.g., $$ ROI).
- Call out **assumptions** (independence, normal approx) & alternatives (bootstrap).

## Interview talking points
- When to **stop** an experiment; **sequential** peeking pitfalls.
- Dealing with **novelty effects** and **heterogeneous treatment effects**.
- Tradeoffs: **CUPED** vs. **stratification** vs. **reweighting**.

---

© You. Use freely for interviews/portfolio.
