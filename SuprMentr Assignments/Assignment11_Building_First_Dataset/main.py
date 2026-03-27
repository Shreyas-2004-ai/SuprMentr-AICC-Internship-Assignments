import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
y = np.array([35,40,50,55,65,70,80,90])

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
hours = float(input("Enter study hours: "))
prediction = model.predict([[hours]])

print(f"Predicted Marks: {prediction[0]:.2f}")