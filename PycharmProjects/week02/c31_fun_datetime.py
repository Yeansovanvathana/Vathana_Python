import time
def current_date():
    return time.strftime("%Y/%m/%d")
print(current_date())
print(type(current_date()))

# time
def current_time():
    return time.strftime("%H:%M:%S")
print(current_time())
print(type(current_time()))