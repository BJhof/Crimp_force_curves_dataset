#%% Imports and Data Loading
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset containing raw crimp force curves
df = pd.read_pickle("crimp_force_curves_dataset.pkl")

#%% Data Splitting by Quality Class and Conductor Cross-Section

# Define subsets for 0.50 mm² conductor
ok_05    = df[(df["Wire_cross-section_conductor"] == 0.5)  & (df["Sub_label_string"] == "OK")].reset_index()
oms_05   = df[(df["Wire_cross-section_conductor"] == 0.5)  & (df["Sub_label_string"] == "one missing strand")].reset_index()
tms_05   = df[(df["Wire_cross-section_conductor"] == 0.5)  & (df["Sub_label_string"] == "two missing strands")].reset_index()
thms_05  = df[(df["Wire_cross-section_conductor"] == 0.5)  & (df["Sub_label_string"] == "three missing strands")].reset_index()
ci_05    = df[(df["Wire_cross-section_conductor"] == 0.5)  & (df["Sub_label_string"] == "crimped insulation")].reset_index()

# Define subsets for 0.35 mm² conductor
ok_035   = df[(df["Wire_cross-section_conductor"] == 0.35) & (df["Sub_label_string"] == "OK")].reset_index()
oms_035  = df[(df["Wire_cross-section_conductor"] == 0.35) & (df["Sub_label_string"] == "one missing strand")].reset_index()
tms_035  = df[(df["Wire_cross-section_conductor"] == 0.35) & (df["Sub_label_string"] == "two missing strands")].reset_index()
thms_035 = df[(df["Wire_cross-section_conductor"] == 0.35) & (df["Sub_label_string"] == "three missing strands")].reset_index()
ci_035   = df[(df["Wire_cross-section_conductor"] == 0.35) & (df["Sub_label_string"] == "crimped insulation")].reset_index()

#%% Figure 5 – Sample Force Curves from Different Quality Classes

# Select sample index
sample = 0

# Extract example curves
sample1 = ok_05["Force_curve_RoI"][sample]
sample2 = ok_035["Force_curve_RoI"][sample]
sample3 = oms_05["Force_curve_RoI"][sample]
sample4 = oms_035["Force_curve_RoI"][sample]
sample5 = ci_05["Force_curve_RoI"][sample]
sample6 = ci_035["Force_curve_RoI"][sample]

# Plot
plt.figure(figsize=(6.3, 4.7))  # approx. 16 cm width

plt.plot(sample1, color="black", label="0.5 mm² / OK")
plt.plot(sample2, color="black", linestyle="--", label="0.35 mm² / OK")
plt.plot(sample3, color="red", label="0.5 mm² / Missing Strands")
plt.plot(sample4, color="red", linestyle="--", label="0.35 mm² / Missing Strands")
plt.plot(sample5, color="blue", label="0.5 mm² / Crimped Insulation")
plt.plot(sample6, color="blue", linestyle="--", label="0.35 mm² / Crimped Insulation")

plt.title("Force Curve RoI")
plt.xlabel("Displacement [Encoder signal]")
plt.ylabel("Force [Sensor value]")
plt.grid(True)
plt.tight_layout()
plt.legend()
# plt.savefig("force_curve_comparison.png", dpi=300)
plt.show()

#%% Figure 6a – Raw Force Curve (Unprocessed)

sample = ok_05["Force_curve_raw"][1]

plt.figure(figsize=(6.3, 4.7))
plt.plot(sample)
plt.title("Force Curve Raw")
plt.xlabel("Displacement [Encoder signal]")
plt.ylabel("Force [Sensor value]")
plt.grid(True)
plt.tight_layout()
# plt.savefig("force_curve_raw.png", dpi=300)
plt.show()

#%% Figure 6b – Baseline-Adjusted Force Curve

sample = ok_05["Force_curve_baseline"][1]

plt.figure(figsize=(6.3, 4.7))
plt.plot(sample)
plt.title("Force Curve Baseline")
plt.xlabel("Displacement [Encoder signal]")
plt.ylabel("Force [Sensor value]")
plt.grid(True)
plt.tight_layout()
# plt.savefig("force_curve_baseline.png", dpi=300)
plt.show()

#%% Figure 6c – Region of Interest (RoI)

sample = ok_05["Force_curve_RoI"][1]

plt.figure(figsize=(6.3, 4.7))
plt.plot(sample)
plt.title("Force Curve RoI")
plt.xlabel("Displacement [Encoder signal]")
plt.ylabel("Force [Sensor value]")
plt.grid(True)
plt.tight_layout()
# plt.savefig("force_curve_ROI.png", dpi=300)
plt.show()

#%% Figure 7 – Preprocessing Pipeline Visualization

# Extract sample force curves from each stage
sample_raw = ok_05["Force_curve_raw"][1]
sample_baseline = ok_05["Force_curve_baseline"][1]
sample_roi = ok_05["Force_curve_RoI"][1]

# Set up subplots
fig, axes = plt.subplots(1, 3, figsize=(18 / 2.54, 5))  # 18 cm width

# Raw curve
axes[0].plot(sample_raw)
axes[0].set_title("Force Curve Raw", fontsize=10)
axes[0].set_xlabel("Displacement [Encoder signal]", fontsize=9)
axes[0].set_ylabel("Force [Sensor value]", fontsize=9)
axes[0].grid(True)

# Baseline-adjusted curve with RoI highlighted
axes[1].plot(sample_baseline)
axes[1].set_title("Force Curve Baseline", fontsize=10)
axes[1].axvspan(1575, 2075, color='yellow', alpha=0.3)
axes[1].grid(True)

# RoI only
axes[2].plot(sample_roi)
axes[2].set_title("Force Curve RoI", fontsize=10)
axes[2].grid(True)

# Subfigure labels
for i, label in enumerate(["(a)", "(b)", "(c)"]):
    axes[i].text(0.5, -0.18, label, transform=axes[i].transAxes,
                 ha="center", va="center", fontsize=11)

plt.tight_layout()
plt.subplots_adjust(bottom=0.22, wspace=0.4)
# plt.savefig("force_curve_preprocessing.png", dpi=300)
plt.show()

#%% Figure 8 – Standard Deviation across the Region of Interest (RoI)
from validation import std

std_ok_05 = std(ok_05["Force_curve_RoI"])
std_oms_05 = std(oms_05["Force_curve_RoI"])
std_tms_05 = std(tms_05["Force_curve_RoI"])
std_thms_05 = std(thms_05["Force_curve_RoI"])
std_ci_05 = std(ci_05["Force_curve_RoI"])
std_ok_035 = std(ok_035["Force_curve_RoI"])
std_oms_035 = std(oms_035["Force_curve_RoI"])
std_tms_035 = std(tms_035["Force_curve_RoI"])
std_ci_035 = std(ci_035["Force_curve_RoI"])

# Create side-by-side subplots for 0.5 mm² and 0.35 mm²
fig, axes = plt.subplots(1, 2, figsize=(18 / 2.54, 5))  # ~18 cm width, 5 cm height

# --- Left Plot: 0.50 mm² ---
axes[0].plot(std_ok_05, color="black", label="OK")
axes[0].plot(std_oms_05, color="orange", label="One Missing Strand")
axes[0].plot(std_tms_05, color="red", label="Two Missing Strands")
axes[0].plot(std_thms_05, color="darkred", label="Three Missing Strands")
axes[0].plot(std_ci_05, color="blue", label="Crimped Insulation")

axes[0].set_title("Wire Cross-Section: 0.50 mm²", fontsize=10)
axes[0].set_xlabel("Displacement [Encoder Signal]", fontsize=9)
axes[0].set_ylabel("Standard Deviation", fontsize=9)
axes[0].grid(True)
axes[0].legend(loc="upper left", fontsize=8)

# --- Right Plot: 0.35 mm² ---
axes[1].plot(std_ok_035, color="black", label="OK")
axes[1].plot(std_oms_035, color="orange", label="One Missing Strand")
axes[1].plot(std_tms_035, color="red", label="Two Missing Strands")
axes[1].plot(std_ci_035, color="blue", label="Crimped Insulation")

axes[1].set_title("Wire Cross-Section: 0.35 mm²", fontsize=10)
axes[1].set_xlabel("Displacement [Encoder Signal]", fontsize=9)
axes[1].set_ylabel("")  # Avoid duplicate y-axis label
axes[1].grid(True)
axes[1].legend(loc="upper left", fontsize=8)

# Layout adjustments
plt.tight_layout()
plt.subplots_adjust(wspace=0.3)

# Save figure as high-resolution PNG
#plt.savefig("Figure8_Standard_Deviation.png", dpi=300)

# Show the plot
plt.show()