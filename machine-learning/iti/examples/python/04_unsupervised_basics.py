"""Curriculum addition: scaled K-means clustering and PCA."""
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

X, _ = load_iris(return_X_y=True)
X_scaled = StandardScaler().fit_transform(X)
clusters = KMeans(n_clusters=3, n_init=20, random_state=42).fit_predict(X_scaled)
projection = PCA(n_components=2).fit_transform(X_scaled)
print("silhouette:", round(silhouette_score(X_scaled, clusters), 3))
print("PCA shape:", projection.shape)
