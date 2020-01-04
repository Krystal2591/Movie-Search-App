import collections
import requests




MovieResults=collections.namedtuple('MovieResults',
                                    "imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres")

def find_movies(search_prompt):

    if not search_prompt or not search_prompt.strip():
        raise ValueError


    url='http://movie_service.talkpython.fm/api/search/{}'.format(search_prompt)


    response=requests.get(url)
    response.raise_for_status()


    movie_data=response.json()
    movies_that_match=movie_data.get('hits')

    movies=[

    MovieResults(**m)
    for m in movies_that_match

    ]
    return movies



