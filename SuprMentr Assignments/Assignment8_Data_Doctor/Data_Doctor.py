import pandas as pd

# Load dataset
df = pd.read_csv("student_dirty_data.csv")

print("\n--- Original Data ---")
print(df)

# 1. Handle Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Department"] = df["Department"].fillna("Unknown")

# 2. Remove Duplicates
df = df.drop_duplicates()

# 3. Standardize Text
df["Name"] = df["Name"].str.strip().str.title()
df["Department"] = df["Department"].str.strip().str.upper()

print("\n--- Cleaned Data ---")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_student_data_v2.csv", index=False)

print("\n✅ Cleaned file saved as 'cleaned_student_data_v2.csv'")