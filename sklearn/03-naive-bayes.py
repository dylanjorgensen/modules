# Resources
# - http://scikit-learn.org/stable/modules/naive_bayes.html
# - http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB

from time import time
import numpy as np
from sklearn.naive_bayes import GaussianNB


# make a matrix and an array
features_train = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
labels_train = np.array([1, 1, 1, 2, 2, 2])

features_test = np.array([[3, -3], [-2, -1], [-3, 2], [1, 1], [2, 1], [3, 2]])
labels_test = np.array([1, 2, 3, 2, 2, 3])

# Set a classifier
clf = GaussianNB()

# Fit the classifier with training data
t0 = time()
clf.fit(features_train, labels_train)  # (x = features) (y = labels)
print "training time:", round(time()-t0, 3), "s"

# Call the predictor function on training data
t1 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

# Check the accuracy
from sklearn.metrics import accuracy_score
print accuracy_score(pred, labels_test)

