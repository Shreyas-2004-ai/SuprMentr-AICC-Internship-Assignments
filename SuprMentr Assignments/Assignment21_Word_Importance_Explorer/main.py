from sklearn.feature_extraction.text import TfidfVectorizer

# 5 sample documents
documents = [
    "Machine learning is amazing and powerful",
    "Deep learning is a subset of machine learning",
    "Python is widely used in machine learning",
    "Artificial intelligence and machine learning are related fields",
    "Data science uses machine learning techniques"
]

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# Feature names
features = vectorizer.get_feature_names_out()

# Convert to array
tfidf_matrix = X.toarray()

# Print top words for each document
for i, doc in enumerate(tfidf_matrix):
    print(f"\nDocument {i+1}:")
    top_indices = doc.argsort()[-3:][::-1]
    for idx in top_indices:
        print(f"{features[idx]} -> {doc[idx]:.3f}")