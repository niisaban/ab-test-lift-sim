---
name: "🧹 Chore / maintenance"
about: Non-user-facing upkeep (deps, build, CI)
labels: chore
---

### Task
<!-- e.g., bump numpy; pin actions/setup-python; tweak pre-commit; etc. -->

### Why
<!-- Reliability, security, reproducibility, etc. -->

### Scope / risk
- User-visible change? ☐Yes ☐No
- Affects runtime code? ☐Yes ☐No
- Rollback plan: revert PR

### Checklist
- [ ] CI green
- [ ] Changelog/README (if appropriate)
- [ ] Local `pytest -q --maxfail=1 -ra`
