def spy_game(nums):
    sub = [0, 0, 7]
    count = 0
    for i in nums:
        if(i == sub[count]):
            count += 1
        if count == 3:
            break
    return count == 3

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))