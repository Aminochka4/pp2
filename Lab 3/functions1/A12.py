def histogram(s):
    for i in s:
        print ('*'*i)

a = list(map(int, input().split()))
histogram(a)