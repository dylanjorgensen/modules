


#########################
# Supervised Learning
# Regression
#########################

# Create some simple data
# import pandas as pd
# df = pd.read_csv('09-regression-test.csv')

import numpy as np
X = [[50,80],[80,65],[60,60],[95,80],[95,50],[40,90]]  # Features
y = [65,83,69,92,84,55]



# Fit a linear regression to it
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
model.fit(X, y)

# Report Results
print 'intercept_ :', model.intercept_
print 'coef_ :', model.coef_
print 'get_params :', model.get_params()

# Model the prediction
predict_data = [[52,81],[81,66],[60,62], [0,8]]
y_hat = model.predict(predict_data)


# # Plot the data
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(X, y, 'o')
ax.plot(predict_data, y_hat)
plt.show()