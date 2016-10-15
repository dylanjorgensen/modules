
# https://docs.python.org/2/library/calendar.html
# https://pymotw.com/2/calendar/

import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
print c.prmonth(2007, 7)


print calendar.TextCalendar(calendar.SUNDAY).formatyear(2007, 2, 1, 1, 2)