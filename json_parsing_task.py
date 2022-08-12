import requests
import json

url = 'https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json'

response = requests.get(url=url)
data = response.json()
movies = []
movie_data = []

for every_object in data:
    movie_data = {"Movie name": every_object['title'], "Movie year": every_object['year'],
                  "Movie cast": every_object["cast"]}
    movies.append(movie_data)
print(movies)
