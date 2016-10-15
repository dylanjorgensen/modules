# Resources
# - http://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup


# Pass HTML into the constructor
soup = BeautifulSoup(open("alice.html"))
# print(soup.prettify())


# soup.title # <title>The Dormouse's story</title>
# soup.title.name  # u'title'
# soup.title.string  # u'The Dormouse's story'
# soup.title.parent.name  # u'head'
# soup.p  # <p class="title"><b>The Dormouse's story</b></p>
# soup.p['class']  # u'title'
# soup.a  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>


# soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>