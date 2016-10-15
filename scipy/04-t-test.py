import scipy.stats





# equal_var is to say if we think the variance of our two sample is equal.
from sklearn.datasets import make_classification
features_train, labels_train = make_classification(n_samples=100000, n_features=20,
                                    n_informative=2, n_redundant=10,
                                    random_state=42)

features_test, labels_test = make_classification(n_samples=100000, n_features=20,
                                    n_informative=2, n_redundant=10,
                                    random_state=42)



# General t-test
scipy.stats.ttest_ind(list_1, list_2)


# Weltch's t-test: By adding the equal_var=False we are saying
# we don't know if our samples have equal degrees of freedom.
scipy.stats.ttest_ind(list_1, list_2, equal_var=False) # Result: array(t-statistic, p-value)
