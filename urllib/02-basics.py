# https://docs.python.org/2/howto/urllib2.html

import urllib2
response = urllib2.urlopen('http://python.org/')
html = response.read()

print html