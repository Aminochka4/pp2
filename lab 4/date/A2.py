import datetime
x = datetime.datetime.now()
print ("yesterday: ", x - datetime.timedelta(days = 1))
print ("today: ", x)
print ("tomorrow: ", x + datetime.timedelta(days = 1))