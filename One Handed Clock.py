import time

current_time = time.localtime()

hour = current_time.tm_hour

minute = current_time.tm_min

second = current_time.tm_sec

year = current_time.tm_year

month = current_time.tm_mon

day = current_time.tm_mday

print('The date is', month, day, year)

print('The time is', hour, minute, second)


