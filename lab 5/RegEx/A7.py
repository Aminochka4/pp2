import re
a = input()
ls =  a.split("_")
print(ls[0] + "".join(ls[i].capitalize() for i in range(1, len(ls))))

# camel = ""
# i = 0
# while (i!=len(a)):
#     if (a[i]=="_"):
#         camel += a[i] + a[i+1].upper()
#         i+=2
#     else:
#         camel += a[i]
#         i += 1

# print (re.sub("_", "", camel))
# print(a.split("_"))
