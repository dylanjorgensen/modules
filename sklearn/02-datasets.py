# Resources
# - http://scikit-learn.org/0.11/datasets/index.html

'''
shape = features * samples
samples = how many things you are testing

features = attributes you are measured
- flowers: petal with, colors
- handwriting: 8x8 pixel grid - 64 features

Labels/target classes
- flowers: different types of flowers
- handwriting: 0-9 digits

'''


# --- Iris ---#

from sklearn.datasets import load_iris

# Embeds the iris CSV file along with a helper function to load it into numpy arrays:
iris = load_iris()

# The features of each sample flower are stored in the `data` attribute
iris.keys()

# Shape (2D array): number of samples (150), number of features (4)
print iris.data.shape
print iris.data[0]  # Show example flower measurements

# Target (1D array): Classes
print iris.target.shape
