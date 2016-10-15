# Resources
# - https://docs.google.com/document/d/1S4Gk42ZPBKAUZh7IPbqyzq_vk18oCvcniVcA4byBXCE/pub

import csv

# Create objects
f_in = open('weather.csv', 'r')  # the r stands for reading an existing file
f_out = open('weather_out.csv', 'w')  # the w option stands for writing on a file

# Create readers
reader_in = csv.reader(f_in, delimiter=',')
writer_out = csv.writer(f_out, delimiter=',')

# Skip the first line because it has headers
reader_in.next()


# line is now a python list with 9 elements
for line in reader_in:
    # print line[0]  # This prints the first column
    # print line # This prints the whole sheets as row arrays
    date = line[0]

    line_1 = [date, line[1], line[2]]
    line_2 = [date, line[3], line[4]]
    writer_out.writerow(line_1)
    writer_out.writerow(line_2)

f_in.close()
f_out.close()