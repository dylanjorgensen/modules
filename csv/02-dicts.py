import csv


with open('weather.csv', 'rb') as sd:
    r = csv.DictReader(sd)
    for line in r:
        print






# This class will turn the table into a dictionary and use the header as the key value.
# csv.DictReader
