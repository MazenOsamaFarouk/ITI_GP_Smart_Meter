from datetime import datetime
import time as t
currentTime = None
while True:
    # time_stamp = t.time() # number of seconds since 1-1-1970 UTC time
    # current_time = datetime.fromtimestamp(time_stamp).strftime("%d-%B,%H:%M:%S")
    # print(current_time)
    current_date = datetime.now().strftime("%d-%B,%H:%M:%S")
    print(current_date)
    t.sleep(5)