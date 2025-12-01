import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('BIBLICAL_EVENTS_UNIFORM_v1.csv')
n_events = len(df)
n_jitter = 10000

# Fixed bins
bin_edges = np.arange(-2000, 125, 25)

# Simulate jitter
peaks_jitter = []
for _ in range(n_jitter):
    jittered = df['year_start'] + np.random.uniform(0, df['year_end'] - df['year_start'] + 1e-6, size=n_events)
    counts, _ = np.histogram(jittered, bins=bin_edges)
    peaks_jitter.append(counts.max())

# Results
median = np.median(peaks_jitter)
min_peak = np.min(peaks_jitter)
max_peak = np.max(peaks_jitter)
print(f"Median peak: {median}, Range: {min_peak}–{max_peak}")