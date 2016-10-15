

#########################
# Supervised Learning
# Regression
#########################

# Create some simple data
import numpy as np
np.random.seed(0)
X = np.random.random(size=(20, 1))
y = 7 * X.squeeze() + 2 + np.random.normal(size=20)
print X.shape

# Fit a linear regression to it
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
model.fit(X, y)

# Report Results
print 'intercept_ :', model.intercept_
print 'coef_ :', model.coef_
print 'r-squared :', model.score(X, y)

# Model the prediction
X_test = np.linspace(0, 1, 100)[:, np.newaxis]  # Make sample data to test
y_test = model.predict(X_test)

# Plot the data
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(X.squeeze(), y, 'o')
ax.plot(X_test.squeeze(), y_test)
plt.show()