import datetime

dt =datetime.datetime.now(datetime.timezone.utc)
print(dt)
print(dt.date())
print(dt.time())
print(dt.timetz())
print(dt.timestamp())
print(dt.toordinal())
print(dt.weekday())
print(dt.isoweekday())
print(dt.isoweekday())

dt=datetime
dt=datetime.datetime(2019,12,4,15,35,58,469)
dt_p =dt+datetime.timedelta(days=15,hours=5)
dt_m =dt-datetime.timedelta(weeks=3)
print(dt_p)
print(dt_m)

dt1=datetime.datetime(2019,11,30,4,46,14,123)
dt2=datetime.datetime(2020,12,4,15,35,58,469)
x= dt2-dt2
print(x)
print(x.days)
print(x.seconds)
