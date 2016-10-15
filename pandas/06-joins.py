# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html


import numpy as np
import pandas as pd

df = pd.read_csv('data/stocks.csv')
print df.head()


apple = df[["Date", "Apple"]]
apple = apple[0:18]
google = df[["Date", "Google"]]
google = google[17:20]


# print apple.head()
# print google.head()




# #Join the two dataframes along rows
# cat = pd.concat([apple, google])
#
# #Join the two dataframes along columns
# #cat = pd.concat([apple, google], axis=1)
# print cat

# # Returns just rows where they both have the same value
# merge = pd.merge(apple, google, on='Date', how='inner')
#
# # Returns all 20 rows from the left table with NaNs
# merge = pd.merge(apple, google, on='Date', how='left')
#

# Keeps output size of left and adds column.
# merge = pd.merge(google, apple, left_on="Date", right_on="Date", how="right")


merge = pd.merge(google, apple, on="Date", how="right")


def adder(df):
    df = "hello"
    return df

merge = merge.apply(adder)


print merge

