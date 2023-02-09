def pal(n):
    if(n == n[::-1]):
        return True
    return False

a = input()
print(pal(a))