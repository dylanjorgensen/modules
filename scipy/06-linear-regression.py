from scipy import stats
import numpy as np
import pylab

# Fit the model
x = np.array([1, 2, 5, 7, 10, 15])
y = np.array([2, 6, 7, 9, 14, 19])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)

# Calculate some additional outputs
predict_y = intercept + slope * x
pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Check values
print 'slope:', slope
print 'intercept:', intercept
print 'r_value', r_value
print 'p_value', p_value
print 'slope_std_error', slope_std_error
print 'degrees_of_freedom', degrees_of_freedom


# Plotting
pylab.plot(x, y, 'o')
pylab.plot(x, predict_y, 'k-')
pylab.show()