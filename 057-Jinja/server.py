from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    rand_number = random.randint(1,10)
    curr_year = datetime.today().year
    return render_template('index.html', num=rand_number, curr_year=curr_year, creator_name = "cosorio")

@app.route('/guess/<name>')
def guess(name):
    _name = name.title()
    _genre = get_genre(name)
    _age = get_age(name)

    return render_template('guess.html', name=_name, genre = _genre, age = _age)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    response.raise_for_status()
    print(num)    
    all_posts = response.json()
    return render_template('blog.html', posts = all_posts)



def get_genre(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data = response.json()
    return data["gender"]

def get_age(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    response.raise_for_status()
    data = response.json()
    return data["age"]

if __name__ == "__main__":
    app.run(debug=True)


