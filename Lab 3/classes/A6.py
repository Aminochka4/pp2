def isPrime(numb):
    a = list(filter(lambda x: all(x%i != 0 for i in range(2, int(x**0.5)+1)) and x > 1, numb))
    return a 

n = list(map(int, input().split()))
print(isPrime(n))  