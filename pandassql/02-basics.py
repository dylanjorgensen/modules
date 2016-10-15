# Resources
# - http://blog.yhathq.com/posts/pandasql-sql-for-pandas-dataframes.html
# - https://www.youtube.com/watch?v=QjICgmk31js

import pandas
import pandasql

# Import pandas dataframe
df = pandas.read_csv('weather_mini.csv')

# Sanity check data
# print df.dtypes
'''
    date          object
    pressure       int64
    dew            int64
    snow         float64
    accidents      int64
'''

# Tables
if True:
    # q = """ SELECT * FROM df """  # Standard syntax
    # q = """ select * from df """  # Wower or uppercase work
    # q = """ SELECT * FROM df: """  # Works with semicolon

    # q = """ SELECT * FROM df LIMIT 10;"""  # Limits  results to 10
    # q = """ SELECT dew AS super_dew FROM df """  # Alias for selection
    pass


# Columns
if True:
    # q = """ SELECT dew,snow,fog FROM df"""

    # q = """ SELECT * FROM df WHERE dew=10"""
    # q = """ SELECT dew,snow FROM df WHERE dew>=10"""
    # q = """ SELECT dew,snow FROM df WHERE dew=( SELECT MAX(dew) FROM df)"""  # Subqueries: 2nd query embedded inside 1st query

    # q = """ SELECT SUM(dew) FROM df """
    # q = """ SELECT dew, MAX(fog) FROM df """  # Also seems to return max dew even though not requested
    # q = """ SELECT MIN(dew), MAX(fog) FROM df """
    pass


# Rows
if True:
    # q = """ SELECT * FROM df WHERE dew=10"""
    # q = """ SELECT * FROM df WHERE dew>10"""
    # q = """ SELECT * FROM df WHERE dew>10"""
    # q = """ SELECT * FROM df WHERE snow IS NULL """
    # q = """ SELECT snow FROM df WHERE snow IS NULL """
    # q = """ SELECT snow FROM df WHERE snow IS NOT NULL """
    pass

# Date & Time
if True:
    # https://www.sqlite.org/lang_datefunc.html
    # q = """ SELECT date FROM df """
    # q = """ SELECT strftime("%", date) FROM df """  # day of week 0-6 with Sunday==0
    # q = """ SELECT date FROM df WHERE date>CURRENT_TIME """
    pass

# Aggregation
if True:
    # placeholder
    pass


# Group By
if True:
    # q = """ SELECT color, COUNT(*) FROM df GROUP BY  color """  # Turns rows into category vars
    # q = """ SELECT * FROM df; SELECT MAX(dew) FROM df; """
    pass





    # q = """ SELECT * FROM df """
    query_result = pandasql.sqldf(q.lower(), locals())
    print query_result
