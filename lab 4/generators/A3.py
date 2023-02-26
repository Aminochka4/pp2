def generator(x):
    cnt = 0
    while cnt != x:
        if cnt % 12 == 0:
            yield cnt
        cnt += 1
a = int(input())
b = generator(a)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
for i in b:
    print(i)
