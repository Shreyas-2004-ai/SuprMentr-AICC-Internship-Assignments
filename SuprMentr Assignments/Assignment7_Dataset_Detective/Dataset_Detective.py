import pandas as pd

# Load dataset (change filename if needed)
df = pd.read_csv("student_data_simple.csv")

# 1. Display top rows
print("\n--- Top 5 Rows ---")
print(df.head())

# 2. Find highest value column (numeric only)
numeric_cols = df.select_dtypes(include='number')
max_values = numeric_cols.max()

highest_column = max_values.idxmax()
highest_value = max_values.max()

print("\n--- Highest Value Column ---")
print(f"Column: {highest_column}")
print(f"Highest Value: {highest_value}")

# 3. Count missing values
print("\n--- Missing Values ---")
missing = df.isnull().sum()
print(missing)

# 4. Basic info
print("\n--- Dataset Info ---")
print(df.info())

# 5. Summary statistics
print("\n--- Summary Statistics ---")
print(df.describe())