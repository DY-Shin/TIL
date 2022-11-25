import requests
import json

TMDB_API_KEY = '5409f4c3910231c41d381e6b518db90a'

def get_movie_datas():
    total_data = []

    for i in range(1, 10):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        # request_url2 = https://api.themoviedb.org/3/movie/{movie_id}/credits?language=ko-KR
        movies = requests.get(request_url).json()
        for movie in movies['results']:
            actors_data = []
            url = ""
            if movie.get('release_date', '') and movie.get('backdrop_path', ''):
                movie_id = movie["id"]
                request_url2 = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                movies2 = requests.get(request_url2).json()
                casts = movies2["cast"]
                for cast in casts:
                    actor = cast["name"]
                    actor_path = cast["profile_path"]
                    if len(actors_data) < 10:
                        actors_data.append({"actor": actor, "actor_path": actor_path})


                request_url1 = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}&language=en-US"
                trailers = requests.get(request_url1).json()
                for result in trailers["results"]:
                    if result["type"] == 'Trailer':
                        url = result["key"]
                    elif result["type"] == "Teaser":
                        url = result["key"]

                request_url1 = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}&language=ko-KR"
                trailers = requests.get(request_url1).json()
                for result in trailers["results"]:
                    if result["type"] == 'Trailer':
                        url = result["key"]
                    elif result["type"] == "Teaser":
                        url = result["key"]

        # print(actors_data)
                # print(actors_data)
                fields = {
                    # 'movie_id': movie['id'],
                    'title': movie['title'],
                    'original_title': movie['original_title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'vote_count': movie['vote_count'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'backdrop_path': movie['backdrop_path'],
                    'adult': movie['adult'],
                    'genres': movie['genre_ids'],
                    'youtube_url': url,
                    'actors_data': actors_data,
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

def get_genre_data():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            # 'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)

    with open("movies/fixtures/genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

get_movie_datas()
get_genre_data()