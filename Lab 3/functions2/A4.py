from movies import movies

def mean_score(movies):
    sum = 0
    for i in movies:
        sum += i["imdb"]
    return sum / len(movies)

# print (mean_score(movies))