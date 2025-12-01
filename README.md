# Testing-Event-Clustering-in-a-Biblical-Timeline
Testing Event Clustering in a Biblical Timeline
# README for "Testing Event Clustering in a Biblical Timeline"

## Overview
This Zenodo deposit archives the manuscript, dataset, and code for the preprint paper "Testing Event Clustering in a Biblical Timeline" (McCain, 2025). The paper performs a preregistered statistical analysis of 109 dated biblical events (2000 BCE to 100 CE) to test for temporal clustering, focusing on a potential anomaly in the early first century CE.

- **Manuscript**: Testing Event Clustering in a Biblical Timeline.pdf (anonymised version for blind review)  
- **Dataset**: BIBLICAL_EVENTS_UNIFORM_v1.csv (109 events with dates, weights, categories, and sources)  
- **Code**: run_preregistered_analysis.py (main Monte Carlo script for uniform null)  
- **Exploratory Code**: bin_width_robustness.py, date_jitter_robustness.py, inhomogeneous_null.py (robustness checks)  
- **Results Files**: bin_width_robustness_results.txt, date_jitter_robustness_results.txt, inhomogeneous_null_results.txt (outputs from exploratory scripts)  

OSF [https://osf.io/g6t7x/].  

## Data Description
- **BIBLICAL_EVENTS_UNIFORM_v1.csv**:  
  - Columns: name, year_start, year_end, weight (all 1.0), category, source_hint  
  - Events: 109 total, curated from the Protestant canon using conservative dating (e.g., 1446 BCE Exodus, 30–33 CE crucifixion).  
  - SHA-256 hash: e3f8a9c1d2b7e4c8a9f1b6d8e7c3f2a1b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4 (verify integrity)  
  - Usage: Load with pandas.read_csv() for mid-year calculation and binning.  

## Code Description and Reproduction Instructions
All code is in Python (requires pandas, numpy). To reproduce:

1. Install dependencies: `pip install pandas numpy`  
2. Run the main script: `python run_preregistered_analysis.py`  
   - Outputs: Observed peak (39 events), dominance ratio (46.2), Monte Carlo p-value (< 3e-7 from 10M simulations)  
3. Run exploratory scripts:  
   - `python bin_width_robustness.py` → Checks 20/30/50-year bins  
   - `python date_jitter_robustness.py` → Jitters dates within uncertainty (10K sims)  
   - `python inhomogeneous_null.py` → Inhomogeneous null with trend (1M sims)  

Expected runtime: Main script ~2 minutes (on standard hardware); exploratory ~5 minutes total.  

## License
CC-BY 4.0 (requires attribution for reuse; commercial use allowed). Future models are separate and reserved for commercial development.

## Citation
McCain, W. (2025). Testing Event Clustering in a Biblical Timeline. Zenodo. DOI: [https://10.0.20.161/zenodo.17772609]  

Contact: wiley.mccain@gmail.com
