# %%
import pandas as pd
import numpy as np

# --- Load Data ---

# Load the dataset containing raw crimp force curves
df = pd.read_pickle("crimp_force_curves_dataset.pkl")

# %%

# --- Define Helper Functions ---

def baseline_curve(curve):
    """
    Inverts the input curve and shifts it so that the first point starts at y = 0.
    """
    curve = np.multiply(curve, -1)
    return curve - curve[0]

def roi_curve(curve, start=1575, end=2075):
    """
    Extracts a region of interest (ROI) from the curve between given frame indices.
    """
    return curve[start:end]

# %%

# --- Generate Baseline-Shifted Curves ---

baseline_curves = []
for curve in df["Force_curve_raw"]:
    processed_curve = baseline_curve(curve)
    baseline_curves.append(processed_curve)

# %%

# --- Extract Region of Interest (ROI) from Baseline Curves ---

roi_curves = []
for curve in baseline_curves:
    roi = roi_curve(curve)
    roi_curves.append(roi)

# %%

# --- Store Processed Curves in DataFrame ---

df["Force_curve_baseline"] = baseline_curves
df["Force_curve_RoI"] = roi_curves

# Drop any unintended 'index' column if present
df = df.drop(columns="index", errors="ignore")

# %%

