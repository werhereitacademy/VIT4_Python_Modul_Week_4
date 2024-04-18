import time

from datetime import datetime, timedelta

def current_time():
    return datetime.now()

def two_weeks_later():
    return current_time() + timedelta(days=14)


print(current_time().strftime("%Y-%m-%d %H:%M:%S"))
print(two_weeks_later().strftime("%Y-%m-%d %H:%M:%S"))