#!/usr/bin/env python3
"""
build_perbin_from_uniform_events.py

Convert an event list with (year_start, year_end, weight) into a 25-year
per-bin file compatible with linear_vs_warp_core.py.

Inputs:
  --events : CSV with columns at least year_start, year_end, weight

Outputs:
  --out    : CSV with columns Start, End, Obs_avg, Exp_best_avg

Obs_avg       = total weight of events whose mid-year falls in the bin
Exp_best_avg  = uniform expected weight per bin (total_weight / N_bins)
"""

import argparse
import math
import numpy as np
import pandas as pd


def build_perbin_from_events(events_df: pd.DataFrame,
                             bin_width: float = 25.0,
                             bin_start: float | None = None,
                             bin_end: float | None = None) -> pd.DataFrame:
    # Basic checks
    required = {"year_start", "year_end", "weight"}
    if not required.issubset(events_df.columns):
        raise ValueError(f"Events file must contain columns {required}, "
                         f"got {list(events_df.columns)}")

    # Compute mid-year for each event
    mid_year = (events_df["year_start"].astype(float) +
                events_df["year_end"].astype(float)) / 2.0
    weights = events_df["weight"].astype(float).values

    # Determine bin range (defaults: auto from data)
    y_min = float(mid_year.min()) if bin_start is None else float(bin_start)
    y_max = float(mid_year.max()) if bin_end   is None else float(bin_end)

    # Snap to bin_width grid (handles negative years)
    start = bin_width * math.floor(y_min / bin_width)
    end   = bin_width * math.ceil(y_max / bin_width)

    edges = np.arange(start, end + bin_width, bin_width)
    n_bins = len(edges) - 1

    # Assign each event to a bin by mid-year
    idx = np.searchsorted(edges, mid_year.values, side="right") - 1
    obs = np.zeros(n_bins, dtype=float)
    for w, i in zip(weights, idx):
        if 0 <= i < n_bins:
            obs[i] += w

    total_weight = float(weights.sum())
    exp_uniform = np.full(n_bins, total_weight / n_bins, dtype=float)

    perbin = pd.DataFrame({
        "Start": edges[:-1],
        "End":   edges[1:],
        "Obs_avg": obs,
        "Exp_best_avg": exp_uniform,
    })

    return perbin


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", required=True,
                    help="CSV with columns year_start, year_end, weight")
    ap.add_argument("--out", required=True,
                    help="Output per-bin CSV (Start, End, Obs_avg, Exp_best_avg)")
    ap.add_argument("--bin_width", type=float, default=25.0)
    ap.add_argument("--bin_start", type=float, default=None,
                    help="Optional override for first bin edge (e.g., -2000)")
    ap.add_argument("--bin_end", type=float, default=None,
                    help="Optional override for last bin edge (e.g., 120)")
    args = ap.parse_args()

    events_df = pd.read_csv(args.events)
    perbin = build_perbin_from_events(
        events_df,
        bin_width=args.bin_width,
        bin_start=args.bin_start,
        bin_end=args.bin_end,
    )

    perbin = perbin.sort_values("Start").reset_index(drop=True)
    perbin.to_csv(args.out, index=False)
    print(f"Wrote per-bin file with {len(perbin)} bins to {args.out}")


if __name__ == "__main__":
    main()
