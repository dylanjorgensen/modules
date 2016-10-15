# Resources
# - https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
# http://strftime.org/
# Format table: https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
import datetime


today = datetime.date.today()
now = datetime.datetime.now().time()

# date, datetime, and time objects all support a strftime(format) method, to create a string
# representing the time under the control of an explicit format string.
print today.strftime('%x')
print today.strftime('We are the %d, %b %Y')


# Return the day of the week as an integer, where Monday is 0 and Sunday is 6
print today.weekday()


# Converting a string into an object then changing the format
str_date = '2015-02-03'
new_fmt = datetime.datetime.strptime(str_date, '%Y-%m-%d')  # Changes the string to an object
print new_fmt.strftime('%d, %b %Y') # Changes the object to custom format




# df['date'] = df['DATEn'].apply(lambda x: x.strftime('%d%m%Y'))
