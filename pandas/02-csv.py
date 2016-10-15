# Resources
# - https://youtu.be/1uVWjdAbgBg?t=28m00s
# - https://github.com/gjreda/pydata2014nyc
# - http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/

'''
CSV Importing

There are many options when importing data to help deal with a variety of problems. When importing
a CSV here are some of the read csv parameters.
- Change separator
- File compression
- Delimiters (ex. 1,000 becomes 1000)
'''



import pandas as pd


## Read a csv into a data frame
df = pd.read_csv('data/titanic_before.csv')


# choose index columns and rows.
# df = pd.read_csv('data/titanic_before.csv', index_col=1, usecols=[1,2,3], nrows=2)
# print(df.head())



# Loop over multiple files.
# https://classroom.udacity.com/courses/ud501/lessons/3975568860/concepts/41007385920923
# we also need to deal with renaming the columns in each file to stop overlap.
symbols = ['GOOG', 'IBM','GLD']
for symbol in symbols:
    df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col-'Date', parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])










# Add two columns
df['hello'] = 'hello' # Creates a new column
# df['new2'] = df['Cabin'] + ' ' + df['Sex']

# Drop several columns, and specifiy the 1 axis
df = df.drop(['Pclass', 'Name', 'SibSp', 'Parch', 'Ticket','Embarked'],1)

# Export to new csv
df.to_csv('data/titanic_after.csv')


