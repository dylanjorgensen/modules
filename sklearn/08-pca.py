
#########################
# Unsupervised Learning
#########################

# Load dataset
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target

# Run the algorithm
from sklearn.decomposition import PCA
pca = PCA(n_components=2)  # Because we want to display it in 2D
pca.fit(X)  # Because PCA is unsupervised you only need the features
X_reduced = pca.transform(X)  # This gives you a reduced data set so you can plot it
print "Reduced dataset shape:", X_reduced.shape

# Plot the results
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1])
plt.show()