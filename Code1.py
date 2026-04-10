# ==========================================
# Q1: Exercise Data Visualization 
# ==========================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 140  # high resolution output

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("Exercise_Data.csv")

# Clean column names (VERY IMPORTANT for hidden spaces)
df.columns = df.columns.str.strip()

df_long = df.melt(
    id_vars=["id", "diet", "kind"],
    value_vars=["1 min", "15 min", "30 min"],
    var_name="Time",
    value_name="Pulse"
)

# ======================================================
# HEATMAP 
# ======================================================

# Create pivot table for heatmap
heatmap_data = df_long.pivot_table(
    values="Pulse",
    index="diet",
    columns="kind",
    aggfunc="mean"
)

plt.figure(figsize=(10, 6))

sns.heatmap(
    heatmap_data,
    annot=True,                # show values inside cells
    fmt=".1f",
    cmap="crest",              # soft professional gradient (no harsh colors)
    linewidths=0.8,            # clean separation between cells
    linecolor="white",
    cbar_kws={
        "label": "Average Pulse Rate"
    }
)

plt.title(
    "Average Pulse Rate by Diet and Exercise Type",
    fontsize=16,
    fontweight="bold"
)
plt.xlabel("Exercise Type", fontsize=12)
plt.ylabel("Diet Type", fontsize=12)

plt.tight_layout()
plt.show()


# ======================================================
# CATEGORICAL PLOT (BOXPLOT)
# ======================================================

cat = sns.catplot(
    data=df_long,
    x="diet",
    y="Pulse",
    hue="kind",
    kind="box",
    palette="Set2",     # soft pastel palette (professional, not loud)
    height=6,
    aspect=1.6,
    showfliers=False    # removes extreme outliers for cleaner visuals
)

cat.fig.suptitle(
    "Pulse Distribution by Diet and Exercise Type",
    fontsize=16,
    fontweight="bold"
)

cat.set_axis_labels("Diet Type", "Pulse Rate")

# Improve legend styling
plt.legend(title="Exercise Type")

plt.tight_layout()
plt.show()


"""
CONCLUSION:

The heatmap shows that pulse rate varies depending on both diet and type of exercise.
Some combinations of diet and exercise consistently show higher average pulse rates.

The boxplot shows the distribution of pulse values across different groups,
indicating variation and spread within each category.

Overall, both diet and exercise type significantly influence heart rate patterns.
Exercise intensity appears to have a stronger effect than diet alone.
"""