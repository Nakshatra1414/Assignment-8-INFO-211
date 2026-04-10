# ==========================================
# Q2: Planets Dataset Visualization 
# ==========================================

import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# STYLE SETTINGS 
# -------------------------------
sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 140

# Load dataset
planets = sns.load_dataset("planets")

# Clean missing values (important for robustness)
planets = planets.dropna()

# ======================================================
# RELATIONAL PLOTS (2)
# ======================================================

# 1. Scatter Plot (Distance vs Orbital Period)
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=planets,
    x="distance",
    y="orbital_period",
    hue="method",
    palette="viridis",   # professional gradient (no harsh colors)
    alpha=0.7,
    edgecolor=None
)

plt.title("Planet Distance vs Orbital Period", fontsize=14, fontweight="bold")
plt.xlabel("Distance from Star")
plt.ylabel("Orbital Period")
plt.legend(title="Discovery Method")
plt.tight_layout()
plt.show()


# 2. Line Plot (Year vs Average Mass)
plt.figure(figsize=(8, 5))

sns.lineplot(
    data=planets,
    x="year",
    y="mass",
    estimator="mean",
    errorbar=None,
    color="#2a6f97"   # soft professional blue
)

plt.title("Trend of Planet Mass Over Time", fontsize=14, fontweight="bold")
plt.xlabel("Year of Discovery")
plt.ylabel("Average Mass")
plt.tight_layout()
plt.show()


# ======================================================
# DISTRIBUTION PLOTS (2)
# ======================================================

# 3. Histogram (Orbital Period Distribution)
plt.figure(figsize=(8, 5))

sns.histplot(
    data=planets,
    x="orbital_period",
    bins=30,
    color="#6c757d"   # neutral professional gray
)

plt.title("Distribution of Orbital Periods", fontsize=14, fontweight="bold")
plt.xlabel("Orbital Period")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


# 4. KDE Plot (Mass Distribution)
plt.figure(figsize=(8, 5))

sns.kdeplot(
    data=planets,
    x="mass",
    fill=True,
    color="#3a86ff",
    alpha=0.5
)

plt.title("Density Distribution of Planet Mass", fontsize=14, fontweight="bold")
plt.xlabel("Mass")
plt.ylabel("Density")
plt.tight_layout()
plt.show()


# ======================================================
# CATEGORICAL PLOTS (2)
# ======================================================

# 5. Box Plot (Orbital Period by Method)
plt.figure(figsize=(10, 5))

sns.boxplot(
    data=planets,
    x="method",
    y="orbital_period",
    palette="Set3",
    showfliers=False
)

plt.xticks(rotation=45)
plt.title("Orbital Period by Discovery Method", fontsize=14, fontweight="bold")
plt.xlabel("Discovery Method")
plt.ylabel("Orbital Period")
plt.tight_layout()
plt.show()


# 6. Bar Plot (Average Mass by Method)
plt.figure(figsize=(10, 5))

sns.barplot(
    data=planets,
    x="method",
    y="mass",
    estimator="mean",
    palette="crest"
)

plt.xticks(rotation=45)
plt.title("Average Planet Mass by Discovery Method", fontsize=14, fontweight="bold")
plt.xlabel("Discovery Method")
plt.ylabel("Average Mass")
plt.tight_layout()
plt.show()



"""
INSIGHTS:

1. The scatter plot shows that planets with greater distance tend to have longer orbital periods,
   indicating a strong positive relationship.

2. The line plot suggests variation in planet mass discovery trends over time.

3. The histogram shows most planets have relatively lower orbital periods.

4. The KDE plot reveals a right-skewed distribution in planet mass.

5. The boxplot highlights differences in orbital period across discovery methods,
   with some methods detecting wider ranges of planets.

6. The bar plot shows that certain discovery methods tend to detect heavier planets on average.

Overall, the dataset reveals strong relationships between discovery method, mass, and orbital behavior.
"""