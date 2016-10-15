# Tutorial Review
# https://github.com/gjreda/pydata2014nyc/blob/master/demo.ipynb


# Resources
# SQL to Pandas, and pandas overview
# - https://www.youtube.com/watch?v=1uVWjdAbgBg
# - http://pandas.pydata.org/
# - http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/#indexing
# - https://www.youtube.com/watch?v=04zBNE2ZHSI
# - http://nbviewer.ipython.org/github/twistedhardware/mltutorial/blob/master/notebooks/IPython-Tutorial/7%20-%20Pandas.ipynb

'''
Overview
- Pandas is the package that makes Python work like MatLab
- Data analysis and modeling
- DataFrame object for data manipulation
- Reading and writing data from formats like CSV
- Intelligent data alignment and integrated handling of missing data
- Reshaping and pivoting of data sets
- label-based slicing, fancy indexing, and subsetting
- Aggregating or transforming data with a powerful group by engine
- Time series-functionality: date range generation and frequency conversion,
moving window statistics, moving window linear regressions, date shifting and
lagging. Even create domain-specific time offsets and join time series
without losing data;
'''


'''
Series Reviewer
- Use brackets inside of parenthesis
- Can simply add a scaler or operation to var
- Cause use inequalities to return a boolen
- A var with a series can have .any() or .all() to test the boolens
- .apply(f) is a faster way to call of function on every item
- Avoid looping over your data use things like the .apply() method
- x.astype(np.float64) is an easy way to change the type of all elements
- Avoid copying one series to another because if change the first the second will also change
- One way around this problem is using x.copy() that will make a unique instance
- Use x.describe to get a bunch of stats measurements
- You can adjust the percenti;es of x.describe x.describe(percentile_width=50)
'''

'''
DataFrame reviewer
- pd.DataFrame is a class that is case sensitive so use capitols
- pd.DataFrame(data, columns=["x"]) is how you add a header
- df["x"][0] this finds the element zero in coulumn x
- df["x_plus_2"] = df["x"] + 2 add an extra column from the first
- You can use the .map() method to change 'false' to display 'true'
- Drop needs the axis filled in to know row or column df = df.drop("is_even", 1)
- Multi-column select needs two brackets df[["x", "odd_even"]]