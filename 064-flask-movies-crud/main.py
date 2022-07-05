from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

TMDB_API_KEY = "1234"
TMDB_API_BASE_URL = "https://api.themoviedb.org/3/"
TMDB_IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()

# CREATION FORM
class CreateMovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField('Submit')

# EDIT FORM
class RateMovieForm(FlaskForm):
    rating = StringField("Rating", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    # READ ALL RECORDS
    #all_movies = db.session.query(Movie).all()

    # ordered_movies = Movie.query.order_by(Movie.rating.desc()).all()
    # i = 1
    # for movie in ordered_movies:
    #     movie.ranking = i
    #     i += 1
    # db.session.commit()

    ordered_movies = Movie.query.order_by(Movie.rating).all()
    for index, movie in enumerate(ordered_movies):
        movie.ranking = len(ordered_movies) - index
    db.session.commit()

    return render_template("index.html", movies=ordered_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    create_form = CreateMovieForm()
    
    if request.method == "POST" and 'title' in request.form:
        # GET EXTRA INFO
        print('GET movies by title ', request.method)
        title = request.form["title"]
        url_movies = f"{TMDB_API_BASE_URL}search/movie?api_key={TMDB_API_KEY}&language=en-US&query={title}&page=1&include_adult=false"
        response = requests.get(url=url_movies)
        data = response.json()
        movies = data["results"]
        return render_template("select.html", movies = movies)
    elif 'id' in request.args:   # querystring
        print('Get detail of selected movie ', request.method)
        movie_id = request.args.get('id')
        url_movie_details = f"{TMDB_API_BASE_URL}movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US" 
        response = requests.get(url=url_movie_details)
        data = response.json()       
        # CREATE RECORD
        new_movie = Movie(
            id = movie_id,
            title = data["title"],
            img_url = f"{TMDB_IMAGE_BASE_URL}w500{data['poster_path']}",
            year = data["release_date"],
            description= data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()    
        return redirect(url_for('edit', id = movie_id) )
    return render_template("add.html", form=create_form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_form = RateMovieForm()
    movie_id = request.args.get('id')  # querystring

    if request.method == "POST":
        # UPDATE RECORD
        print('UPDATING RECORD ID ' , movie_id)
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = request.form["rating"]
        movie_to_update.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))

    movie_selected = Movie.query.get(movie_id)
    return render_template("edit.html", movie=movie_selected, form=edit_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')

    # DELETE A RECORD BY ID
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
