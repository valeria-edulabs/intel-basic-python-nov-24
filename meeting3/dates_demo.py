# bday = "11-02-1987"
# result = bday.split("-")
# print(result)
# d, m, y = bday.split("-")
# print(d)
# today = "19-11-2024"
import time
from datetime import datetime,date, timedelta

# datetime.datetime
# datetime.date
# datetime.time
# datetime.timedelta

print(datetime.now(), type(datetime.now()))
print(date.today(), type(date.today()))

ts1 = datetime.now()
time.sleep(3)
ts2 = datetime.now()

print("ts1", ts1, "ts2", ts2)
print(ts2 - ts1)

yogev = datetime(1985, 8, 5, 15, 6, 4)
valeria = datetime(1987, 2, 11, 20, 59, 7)



print(valeria - yogev)
print(yogev - valeria)


now = datetime.now()
print(now + timedelta(minutes=15))


print(now.weekday())
# Sun, 18-11-2024
print(now.strftime("%a, %d-%m-%Y"))

my_date = "01/06/1999 13:04:09"
my_date_as_datetime = datetime.strptime(my_date, "%d/%m/%Y %H:%M:%S")
print(datetime.now() - my_date_as_datetime)

print(my_date_as_datetime < now)