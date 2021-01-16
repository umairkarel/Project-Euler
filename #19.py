import datetime
from dateutil.relativedelta import *
start = datetime.datetime(1901, 1, 1)
end = datetime.datetime(2000, 12, 1)
# print(start)

# print(start.weekday())
count = 0
while start < end:
	if start.weekday() == 6:
		count += 1
	start += relativedelta(months=+1)
print(count)






