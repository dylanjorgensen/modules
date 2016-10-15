

import pandas as pd

# define date range
start_date='2010-01-05'
end_date='2010-01-15'
dates = pd.date_range(start_date,end_date)


# Create an empty dataframe
df1 = pd.DataFrame(index=dates)
# print(df1)
# print(df1.info())


# Read SPY data into temporary dataframe
# If you use parse_dates=True then read_csv tries to parse the index as a date.
# Therefore, you would also need to declare the first column as the index with index_col=[0]:
df_stocks = pd.read_csv("data/stocks.csv", parse_dates=True, index_col="Date", na_values=['NaN'])
# print(df_stocks)
# print(df_stocks.info())



# Join
df1 = df1.join(df_stocks, how='inner')
# print(df_stocks)


'''
how : {‘left’, ‘right’, ‘outer’, ‘inner’}
How to handle indexes of the two objects. Default: ‘left’ for joining on index, None otherwise
left: use calling frame’s index
right: use input frame’s index
outer: form union of indexes
inner: use intersection of indexes
'''





# # Drop NaNs
df1 =df1.dropna()

print(df1)

