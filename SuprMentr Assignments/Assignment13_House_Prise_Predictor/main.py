import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("dataset.csv")

# Features and Labels
X = df[['Area']]
y = df['Price']

# Model
model = LinearRegression()
model.fit(X, y)

# User input
area = float(input("Enter house area: "))

# Prediction
predicted_price = model.predict([[area]])

print(f"Predicted House Price: ₹{predicted_price[0]:,.2f}")