import datetime


now = datetime.datetime.now()
future = datetime.timedelta(hours=5, minutes=15)

print((now + future).strftime("%d/%m/%y %I:%M:%S"))
print('Какое-то изменение')
