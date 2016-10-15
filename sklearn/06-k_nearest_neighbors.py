# Resources
# - http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

#########################
# Supervised Learning
# Classification
#########################


from sklearn import neighbors, datasets


iris = datasets.load_iris()
X, y = iris.data, iris.target
print X.shape

knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)

# What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
print iris.target_names[knn.predict([[2, 5, 4, 2]])]
