import pandas as pd
import seaborn as sns

# Load the built-in Iris dataset
df = sns.load_dataset('iris')

# 1. Show the first few rows to understand the structure
print("--- Dataset Preview ---")
print(df.head())

# 2. Statistical summary (Mean, Max, Min, etc.)
print("\n--- Summary Statistics ---")
print(df.describe())

# 3. Check for missing values (Crucial step in Data Science)
print("\n--- Missing Values Check ---")
print(df.isnull().sum())
