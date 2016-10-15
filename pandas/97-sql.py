import pandas as pd
import pandasql as ps

# Resources
# - http://www.r-bloggers.com/turning-data-into-awesome-with-sqldf-and-pandasql/
# - http://www.sql.su/
# - https://www.youtube.com/watch?v=1uVWjdAbgBg
# - https://github.com/gjreda/pydata2014nyc/blob/master/demo.ipynb

"""
SQL Light Guide
 - Selecting
 - Joining
 - Grouping
 - Filtering

*** Indexes are not columns!
Pandasql lets you make SQL queries in Python but you can also use pandas itself without this
module for much of it's functionality.
"""


# SQL Query
if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)

    q1 = """SELECT COUNT(*) FROM football WHERE wins = 10""" # Count duplicates in a column
    print ps.sqldf(q1, locals())



# Panda's Queries
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
