from movies import movies
from A3 import category
from A4 import mean_score

def average_score_of_category(movies, cats):
    new_list = category(movies, cats)
    return mean_score(new_list)

a = input()     
print(average_score_of_category(movies, a))
    