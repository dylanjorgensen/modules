import pandas as pd




# URL to file
if False:
    clean = lambda s: s.replace('$', '')[:-1] if '.' in s else s.replace('$', '') # a lot going on here
    url = 'https://raw.github.com/gjreda/best-sandwiches/master/data/best-sandwiches-geocode.tsv'
    sandwiches = pd.read_table(url, sep='\t', converters={'price': lambda s: float(clean(s))})

    print sandwiches.info()
    # print sandwiches.head(3)



# JSON
if True:
    gh = pd.read_json('https://api.github.com/repos/pydata/pandas/issues?per_page=3')

    print gh.info()
    # print gh
    # print gh[['body', 'created_at', 'title', 'url']].head(3)
