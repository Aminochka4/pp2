def not_set(a):
    new_list=[]
    for i in a:
        if i not in new_list:
            new_list.append(i)
    return new_list

a = list(map(int, input().split()))
print(not_set(a))
