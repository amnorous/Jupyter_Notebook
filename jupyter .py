# ------------------------------------------------------
# Ubuntu-Inspired Data Analysis Assignment
# Objective:
# 1. Load and analyze a dataset using pandas.
# 2. Create simple plots with matplotlib (and seaborn) for visualization.
# ------------------------------------------------------

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------
# Task 1: Load and Explore the Dataset
# ------------------------------------------------------

try:
    # Option 1: Load from CSV file (replace 'data.csv' with your dataset filename)
    # df = pd.read_csv("data.csv")

    # Option 2: Use built-in Iris dataset (via seaborn)
    df = sns.load_dataset("iris")

    print("✅ Dataset successfully loaded!\n")
except FileNotFoundError:
    print("⚠️ File not found. Please check the filename or path.")
except Exception as e:
    print(f"⚠️ An error occurred while loading the dataset: {e}")

# Display first few rows
print("🔎 First five rows of the dataset:")
print(df.head(), "\n")

# Check structure of dataset
print("📊 Dataset Info:")
print(df.info(), "\n")

# Check missing values
print("❓ Missing values in dataset:")
print(df.isnull().sum(), "\n")

# Clean dataset (fill or drop missing values if any)
df = df.dropna()  # or df.fillna(method='ffill', inplace=True)

# ------------------------------------------------------
# Task 2: Basic Data Analysis
# ------------------------------------------------------

# Basic statistics
print("📈 Basic statistics of numerical columns:")
print(df.describe(), "\n")

# Grouping: mean petal length by species
grouped = df.groupby("species")["petal_length"].mean()
print("🌸 Average petal length per species:")
print(grouped, "\n")

# Observations:
# - Virginica tends to have the largest petal length on average
# - Setosa tends to have the smallest

# ------------------------------------------------------
# Task 3: Data Visualization
# ------------------------------------------------------

# Set plot style
sns.set(style="whitegrid")

# 1. Line chart (trend over sample index for sepal length)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length", color="teal")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal_length", data=df, palette="viridis", ci=None)
plt.title("Bar Chart: Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8,5))
plt.hist(df["sepal_width"], bins=15, color="orange", edgecolor="black")
plt.title("Histogram: Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, palette="deep")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# ------------------------------------------------------
# Findings / Observations
# ------------------------------------------------------
# 1. Virginica species has the largest petal dimensions on average.
# 2. Setosa species is clearly separated in scatter plot (smallest petals, widest sepals).
# 3. Sepal width distribution is fairly normal but with a slight left skew.
# 4. Trends over samples show variations, but clear group differences by species.

print("✅ Analysis and visualization complete.")
