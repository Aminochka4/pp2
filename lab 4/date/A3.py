import datetime
x = datetime.datetime.now()
# print(x.strftime("%c"))
print (x.replace(microsecond = 0))