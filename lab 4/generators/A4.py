a = int(input())
b = int(input())
c = (i*i for i in range(a, b))
for x in c:
    print (x)