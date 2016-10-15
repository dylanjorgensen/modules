
# http://iaingallagher.tumblr.com/post/50980987285/t-tests-in-python

import scipy.stats as ss

g1 = [16.65, 13.20, 17.20, 11.50, 54.08, 16.09, 75.50, 26.00, 2.79, 10.11]
g2 = [15.08, 13.71, 13.63, 16.92, 59.33, 17.60, 73.50, 25.88, 3.03, 7.99]

print ss.ttest_ind(g1, g2)



# The first argument is the T value, and the second is the degrees of freedom.
print ss.t.sf(-0.03470643049959005, 9)






# 1-sample t-test
from scipy import stats
one_sample_data = [356, 536, 1032, 209, 285]

one_sample = ss.ttest_1samp(one_sample_data, 175.3)

print "The t-statistic is %.3f and the p-value is %.3f." % one_sample



female = [16.65, 13.20, 17.20, 11.50, 54.08, 16.09, 75.50, 26.00, 2.79, 10.11]
male = [15.08, 13.71, 13.63, 16.92, 59.33, 17.60, 73.50, 25.88, 3.03, 7.99]


two_sample = ss.ttest_ind(male, female)

print "The t-statistic is %.3f and the p-value is %.3f." % two_sample

# assuming unequal population variances
two_sample_diff_var = ss.ttest_ind(male, female, equal_var=False)

print two_sample_diff_var


