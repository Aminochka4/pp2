from A1 import score
from movies import movies
def sublist(movies):
    new_list = list()
    for i in movies:
        if (score(i)):
            new_list.append(i)
    return new_list