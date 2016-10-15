
import pandas as pd

df = pd.read_csv('data/titanic_after.csv')


# print(df['Survived'][:5]) # return column


# cols = ['Survived', 'Sex', 'Age'] # just passing a list
# print(df[cols][:5])


# # SELECT *
# # FROM df
# # WHERE sex = 'male'
# print(df[df['Sex'] == 'male'][:10])


# SELECT *
# FROM df
# WHERE sex = 'male'
# LIMIT 10
# ORDER BY Fare DESC
print(df[df['Sex'] == 'male'][:10].sort_values(by='Fare', ascending=False))






# View Info
# print(df.head()) # top 5 rows
# print(df.tail()) # last 5 rows
# print(df.tail(n)) # # last n rows



# print(df[10:21]) # Rows 10-20


# print(df['Fare'].max()) # max value in column
# print(df['Fare'].mean()) # mean value in column



"""

Read in multiple stocks:
Create an empty pandas.DataFrame with dates as index: pandas.date_range
Drop missing date rows: pandas.DataFrame.dropna
Incrementally join data for each stock: pandas.DataFrame.join
Manipulate stock data:
Index and select data by row (dates) and column (symbols)
Plot multiple stocks at once (still using pandas.DataFrame.plot)
Carry out arithmetic operations across stocks
Hit Next to continue.

"""



