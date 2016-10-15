import statsmodels.api as sm

features = [1,4,5,6,3]
values = [4,5,6,2,3]


features = sm.add_constant(features)
model = sm.OLS(values, features)
results = model.fit()
intercept = results.params[0]
params = results.params[1:]

print intercept
print params


'''
OUTPUT:

Your intercept: 199.07125028
Your parameters: [-4.44124847  0.91818241]

This means homeruns will be predicted using the equation
homeruns = -4.44 * height + 0.92 * weight + 199.07
'''
