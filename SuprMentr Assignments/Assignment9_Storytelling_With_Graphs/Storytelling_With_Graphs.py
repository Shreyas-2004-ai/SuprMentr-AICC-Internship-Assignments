import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# --- Bar Chart ---
plt.figure()
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# --- Pie Chart ---
plt.figure()
plt.pie(df["Sales"], labels=df["Month"], autopct='%1.1f%%')
plt.title("Sales Distribution - Pie Chart")
plt.show()

# --- Histogram ---
plt.figure()
plt.hist(df["Sales"], bins=5)
plt.title("Sales Distribution - Histogram")
plt.xlabel("Sales Range")
plt.ylabel("Frequency")
plt.show()