a = int(input())
b = (i for i in range(1, a+1) if i%2==0)
print (list(b))
print (type(b))