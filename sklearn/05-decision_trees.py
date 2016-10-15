# Resources
# - http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

from sklearn import tree
from sklearn.datasets import make_classification



# Build, fit and predict
if False:

    # Make some training and test data
    features_train, labels_train = make_classification(n_samples=100000, n_features=20,
                                        n_informative=2, n_redundant=10,
                                        random_state=42)

    features_test, labels_test = make_classification(n_samples=100000, n_features=20,
                                        n_informative=2, n_redundant=10,
                                        random_state=31)
    # Classifier
    clf = tree.DecisionTreeRegressor()
    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)

    # Check accuracy
    from sklearn.metrics import accuracy_score
    print accuracy_score(pred, labels_test)


# --- Entropy --- #

# Entropy Example
if True:
    import math
    print -0.5*math.log(0.5, 2) - 0.5*math.log(0.5, 2) # Low entropy: 1
    print -0.3*math.log(0.3, 2) - 0.7*math.log(0.7, 2) # Med entropy: .881
    print -0.01*math.log(0.01, 2) - 0.99*math.log(0.99, 2) # High entropy: .080

#
# import math
# print -(2.0/3.0)*math.log((2.0/3.0), 2) - (1.0/3.0)*math.log((1.0/3.0), 2)
# parent_entropy = 1.0
# weighted_avg = (1.0/2.0)*1.0 + (1.0/2.0)*1.0
# print parent_entropy - weighted_avg

