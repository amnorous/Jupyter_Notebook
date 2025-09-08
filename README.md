# ------------------------------------------------------
# Ubuntu-Inspired Data Analysis Assignment
# ------------------------------------------------------

## 🎯 Objective
1. Load and analyze a dataset using **pandas**.  
2. Create simple plots with **matplotlib** (and **seaborn**) for visualization.  

---

## 📦 Step 1: Import Libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
📊 Step 2: Load and Explore the Dataset
python
Copy code
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

# Dataset structure
print("📊 Dataset Info:")
print(df.info(), "\n")

# Missing values
print("❓ Missing values in dataset:")
print(df.isnull().sum(), "\n")

# Clean dataset
df = df.dropna()
📝 Observations:

Dataset contains measurements of iris flowers (sepal length, sepal width, petal length, petal width) across three species.

No missing values in the built-in dataset.

📈 Step 3: Basic Data Analysis
python
Copy code
# Basic statistics
print("📈 Basic statistics of numerical columns:")
print(df.describe(), "\n")

# Grouping: mean petal length by species
grouped = df.groupby("species")["petal_length"].mean()
print("🌸 Average petal length per species:")
print(grouped, "\n")
📝 Observations:

Virginica has the largest average petal length.

Setosa has the smallest petal length.

📉 Step 4: Data Visualization
1. Line Chart: Sepal Length Trend
python
Copy code
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length", color="teal")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()
2. Bar Chart: Average Petal Length by Species
python
Copy code
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal_length", data=df, palette="viridis", ci=None)
plt.title("Bar Chart: Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()
3. Histogram: Sepal Width Distribution
python
Copy code
plt.figure(figsize=(8,5))
plt.hist(df["sepal_width"], bins=15, color="orange", edgecolor="black")
plt.title("Histogram: Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()
4. Scatter Plot: Sepal Length vs Petal Length
python
Copy code
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, palette="deep")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
