'''
If it turns out our data is non normal we have a couple choices
If there is lots, and lots of data then we can just run all normal distribution tests anyway.
If not we can use a nonparametric test


Mann-Whitney u-test
This is for nonparametric data
Tests the null hypothesis to populations are the same

'''

import scipy.stats




# Results: (u,p) u=U-statistic, p=P-value
result = scipy.stats.mannwhitneyu(x_sample,y_sample)
