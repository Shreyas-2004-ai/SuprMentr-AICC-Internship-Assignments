import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load dataset
df = pd.read_csv("dataset.csv")

# Drop 'User' column (not needed for calculation)
data = df.drop("User", axis=1)

# New user input
new_user = [[5,1,1]]

# KNN model
model = NearestNeighbors(n_neighbors=2, metric='euclidean')
model.fit(data)

distances, indices = model.kneighbors(new_user)

print("Nearest Users:")
print(df.iloc[indices[0]])