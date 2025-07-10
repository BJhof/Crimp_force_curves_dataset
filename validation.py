#%% Load Dataset
import pandas as pd
import numpy as np

# Load the dataset containing crimp force curves and metadata
df = pd.read_pickle("crimp_force_curves_dataset.pkl")
#%% Completeness – Check curve lengths and missing values

print("Completeness Check:")
print(f"- Unique lengths of raw curves: {df['Force_curve_raw'].apply(len).unique()}")
print(f"- Unique lengths of baseline curves: {df['Force_curve_baseline'].apply(len).unique()}")
print(f"- Unique lengths of RoI curves: {df['Force_curve_RoI'].apply(len).unique()}")
print(f"- Any missing values in DataFrame: {df.isnull().any().any()}")
#%% Accuracy – Identify label mismatches between CFM system and expert annotations

# Create mask where system and expert labels disagree
mismatch_mask = df["Binary_label_encoded"] != df["CFM_label_encoded"]
mismatches_df = df[mismatch_mask]

# Separate mismatches by conductor cross-section
mismatches_05 = mismatches_df[mismatches_df["Wire_cross-section_conductor"] == 0.5].reset_index()
mismatches_035 = mismatches_df[mismatches_df["Wire_cross-section_conductor"] == 0.35].reset_index()

print("\nAccuracy Check (CFM vs Expert Labels):")
print(f"- Mismatches for 0.50 mm²:\n{mismatches_05['Sub_label_string'].value_counts()}")
print(f"- Mismatches for 0.35 mm²:\n{mismatches_035['Sub_label_string'].value_counts()}")
#%% Consistency – Define standard deviation function (used in images.py)

def std(curves):
    """
    Compute the pointwise standard deviation across a list of force curves.

    Parameters:
        curves (pd.Series): Series of NumPy arrays (each of length 500).
    
    Returns:
        np.ndarray: Array of standard deviations at each point (length 500).
    """
    data = np.vstack(curves.values)  # shape: (n_samples, 500)
    return np.std(data, axis=0)

#%% Uniqueness – Ensure all CrimpID values are unique

print("\nUniqueness Check:")
print(f"- Any duplicated CrimpID values: {df['CrimpID'].duplicated().any()}")

