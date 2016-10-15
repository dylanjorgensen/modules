from bs4 import BeautifulSoup

# Pass HTML into the constructor
soup = BeautifulSoup(open("alice.html"))


# Extracting all the URLs
for link in soup.find_all('a'):
    print(link.get('href'))

# Extracting all the text from a page
#print(soup.get_text())