marvel_movies = ['Captain Marvel', 'Avengers Game', 'The Averngers','Iron Man 3', 'DeadPool', 'Ant-man', 'Thor-The Dark World', 'Black Panther','SpiderMan-Homecoming','Guardians of The Galaxy']

special_marvel_movies = []

for movie_title in marvel_movies:
    if 'the' in movie_title.lower():
        special_marvel_movies.append(movie_title)

print(special_marvel_movies)

