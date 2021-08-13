import datetime
import time


now = datetime.datetime.now()

print(now)
time.sleep(3)

end = datetime.datetime.now()
print(end)
print(end - now)
