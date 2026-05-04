import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load Dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# -------------------------------
# Elbow Method
# -------------------------------
wcss = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(6,4))
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# -------------------------------
# Final KMeans with Optimal K=3
# -------------------------------
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(df)

df['Cluster'] = clusters

# -------------------------------
# Silhouette Score
# -------------------------------
score = silhouette_score(df.iloc[:, :-1], clusters)
print("Silhouette Score:", score)

# -------------------------------
# Cluster Visualization
# -------------------------------
plt.figure(figsize=(8,6))

plt.scatter(
    df['sepal length (cm)'],
    df['petal length (cm)'],
    c=df['Cluster'],
    cmap='viridis'
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 2],
    color='red',
    marker='X',
    s=200,
    label='Centroids'
)

plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("K-Means Clustering")
plt.legend()
plt.show()