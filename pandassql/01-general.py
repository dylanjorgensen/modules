# Resources
# - https://www.youtube.com/watch?v=QjICgmk31js
# - https://pypi.python.org/pypi/pandasql
# - https://www.youtube.com/watch?v=-thOn1NKJew&list=PL_RGaFnxSHWr_6xTfF2FrIw-NAOo3iWMy

'''
- pandasql creates a DB, schema and all, loads your data, and runs your SQL.
- pandasql.sqldf accepts 2 parameters, a sql query string, and set of session/environment variables (locals() or globals())

'''

# Import Statement
import pandas
import pandasql


# Basic example in a function
def playground(filename):

    df = pandas.read_csv(filename)

    # Defines pandasql query
    q = """ SELECT dew,fog FROM df"""

    #Execute your SQL command against the pandas frame
    query_result = pandasql.sqldf(q.lower(), locals())
    return query_result

filename = 'weather_mini.csv'
print playground(filename)


