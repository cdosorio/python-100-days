from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests

TMDB_API_KEY = "1234"
TMDB_API_BASE_URL = "https://api.themoviedb.org/3/"
TMDB_IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/'

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    url_movies = f"{TMDB_API_BASE_URL}discover/movie?sort_by=popularity.desc&api_key={TMDB_API_KEY}"
    print(url_movies)
    response = requests.get(url=url_movies)
    data = response.json()
    movies = data["results"]

    for movie in movies:
        # full image url
        movie['poster_path'] = f"{TMDB_IMAGE_BASE_URL}w500{movie['poster_path']}"
    return render_template("index.html", movies=movies)



if __name__ == '__main__':
    app.run(debug=True)
