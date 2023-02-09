heads = int(input())
legs = int(input())
def solve(numheads, numlegs):
    rabbits = (numlegs - numheads * 2)/2
    chickens = numheads - rabbits
    return rabbits, chickens

print (solve(heads, legs))