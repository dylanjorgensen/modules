import webbrowser
import time

total_breaks = 3
breaks = 0

while breaks <= total_breaks:
    time.sleep(2)
    webbrowser.open("http://nintendo.com")
    breaks += 1
    print time.ctime()