# link to markdown
http://daringfireball.net/projects/markdown/syntax#header



# Resources
# - http://pymotw.com/2/json/

'''
Do not use simplejson, it was with python 2.5, but now 2.7 has taken it over.

The json module provides an API for converting in-memory Python objects to a serialized representation known as JavaScript Object Notation (JSON)
'''

import json

# Generate sample data
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]

# Encoding
if False:

    data_string = json.dumps(data)  # Unsorted
    data_string = json.dumps(data, sort_keys=True)  # Sorted by keys
    data_string = json.dumps(data, sort_keys=True, indent=2)  # Sort and indent

    print data_string, type(data_string)


# Decoding
if False:
    # Decode back into list
    decoded = json.loads(data_string)
    print 'DECODED:', decoded, type(decoded)

