from itertools import permutations

def findPerm(string):
    words = [''.join(perm) for perm in permutations(string)]
    print(set(words))

a = input()
findPerm(a)
