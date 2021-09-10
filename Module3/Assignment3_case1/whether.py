#problem 3
import time
day = time.localtime()
if day.tm_hour < 17:
    print("Its Day outside")
else:
    print("Its dark outside")
