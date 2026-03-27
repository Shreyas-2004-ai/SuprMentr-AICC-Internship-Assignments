import pandas as pd
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("dataset.csv")

# Select features
X = df[['Annual Income', 'Spending Score']]

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Show result
print(df)

# Group description
for i in range(3):
    print(f"\nCluster {i} Customers:")
    print(df[df['Cluster'] == i])