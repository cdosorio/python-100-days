from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0,10)

@app.route('/')
def index():

    return """<h1>Guess a number between 0 and 9</h1>
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">        
        """

#http://127.0.0.1:5000/3
@app.route("/<int:choice>")
def guess(choice):
    if choice < number:
        return '<h1 style="color:red;">Too low</h1>'
    elif choice > number:
        return '<h1 style="color:red;">Too high</h1>'
    else:
        return '<h1 style="color:green;">You Win!</h1>'

if __name__ == "__main__":
    app.run(debug=True)