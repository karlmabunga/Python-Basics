import datetime

x = datetime.datetime.now()
month = x.strftime('%B')
weekday = x.strftime('%A')


print(month)
print(weekday)

print(x.strftime('%b %d %Y %H: %M: %S:'))

print(dir(x))
print(x.date())

