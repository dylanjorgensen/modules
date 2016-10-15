# Resources
# - http://scikit-learn.org/stable/

# Notes
'''
- model.fit(X, y) : Large X means 2D array, lower y means 1D Matrix
- model.coef_ : trailing_ is a predicted var like y-hat in stats
'''

# ML Process
'''
- Step 1: Make a classifier
- Step 2: Fit the Classifier with (features, labels)
- Step 3: Run prediction
- Step 4: Plot results
- Step 5: Check Accuracy
'''

# Process Timer
'''
from sklearn.metrics import accuracy_score
print accuracy_score(pred, labels_test)
'''


# Accuracy Checker
'''
from sklearn.metrics import accuracy_score
print accuracy_score(pred, labels_test)
'''

# Data Generator
'''
from sklearn.datasets import make_classification
features_train, labels_train = make_classification(n_samples=100000, n_features=20,
                                    n_informative=2, n_redundant=10,
                                    random_state=42)

features_test, labels_test = make_classification(n_samples=100000, n_features=20,
                                    n_informative=2, n_redundant=10,
                                    random_state=42)
'''
