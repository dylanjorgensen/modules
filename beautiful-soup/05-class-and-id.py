
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("data-elements.html"))

# Finds and returns table and select button with the id=CarrierList
id = soup.find(id='CarrierList')
# print(id)

# Filters id to just the options
for option in id.find_all('option'):
    # print option
    # print option.text  # Prints just the text between the tags
    print(option['value'])  # goes even deeper into value tag
