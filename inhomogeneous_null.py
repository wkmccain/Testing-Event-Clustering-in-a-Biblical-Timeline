import pandas as pd
import numpy as np

# Load for n_events
df = pd.read_csv('BIBLICAL_EVENTS_UNIFORM_v1.csv')
n_events = len(df)
n_inhom = 1000000

# Fixed bins
bin_edges = np.arange(-2000, 125, 25)

# Inhomogeneous null: linear rate from 1 to 3 over -2000 to +100 (T=2100 years)
maxes_inhom = []
for _ in range(n_inhom):
    u = np.sort(np.random.uniform(0, 1, n_events))
    # Cumulative intensity Λ(t) = t + t^2 (normalized)
    # Inverse: t = -1 + sqrt(1 + 2u) for a=1, b=2, normalized
    t = -1 + np.sqrt(1 + 2 * u)  # for [0,1] normalized
    times = -2000 + 2100 * t
    counts, _ = np.histogram(times, bins=bin_edges)
    maxes_inhom.append(counts.max())

# Results
inhom_max = max(maxes_inhom)
inhom_exceed_30 = sum(m >= 30 for m in maxes_inhom)
p_upper = 3 / n_inhom if inhom_exceed_30 == 0 else inhom_exceed_30 / n_inhom
print(f"Highest max bin: {inhom_max}")
print(f"Sims >= 30: {inhom_exceed_30} (p < {p_upper:.2e})")