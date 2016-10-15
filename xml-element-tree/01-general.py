
import xml.etree.ElementTree as ET
import pprint

tree = ET.parse('research.xml')
root = tree.getroot()


# Basic children of root printing
for child in root:
    child.tag  # This will print out the tag of each child element



# Xpath expressions
title = root.find('./fm/bibl/title')
title_text = ""
for p in title:
    title_text += p.text
print "\nTitle :", title_text


for a in root.findall('./fm/bibl/aug/au'):
    email = a.find('email')
    if email is not None:
        print email.text


