from movies import movies

def category(movies, cats):
    new_list = list()
    for i in movies:
        if cats == i["category"]:
            new_list.append(i)
    return new_list

# kittens = input()
# print(category(movies, kittens))
