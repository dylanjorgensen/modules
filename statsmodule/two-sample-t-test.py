from scipy import stats


counties = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [8, 7, 6, 9, 10, 5, 7, 11, 8, 7]
b = [5, 6, 4, 6, 5, 3, 2, 9, 4, 4]

# Unpaired t-test
# t, p = stats.ttest_ind(a, b, equal_var=False) # Independedn
t, p = stats.ttest_rel(a, b) # Independedn
print t
print p