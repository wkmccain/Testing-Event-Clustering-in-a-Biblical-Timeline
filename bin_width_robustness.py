import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('BIBLICAL_EVENTS_UNIFORM_v1.csv')
df['mid_year'] = (df['year_start'] + df['year_end']) / 2
n_events = len(df)

# Function to compute for given bin_width
def compute_clustering(bin_width):
    bin_edges = np.arange(-2000, 125, bin_width)
    counts, _ = np.histogram(df['mid_year'], bins=bin_edges)
    peak_count = counts.max()
    peak_idx = counts.argmax()
    peak_start = bin_edges[peak_idx]
    peak_end = bin_edges[peak_idx + 1]
    peak_mid = (peak_start + peak_end) / 2
    other_counts = np.delete(counts, peak_idx)
    mean_others = other_counts.mean() if len(other_counts) > 0 else 0
    R = peak_count / mean_others if mean_others > 0 else float('inf')
    return {
        'bin_width': bin_width,
        'peak_bin': f"{peak_start}–{peak_end} CE (mid {peak_mid:.1f})",
        'peak_count': peak_count,
        'R': round(R, 2)
    }

# Run for 20, 30, 50 years
bin_widths = [20, 30, 50]
results = [compute_clustering(w) for w in bin_widths]

# Output
for r in results:
    print(r)