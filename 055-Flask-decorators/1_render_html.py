from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """<h1 style="text-align: center">Hello, World!</h1>
        <p>paragraph 1</p>        
        """

# route params
#http://127.0.0.1:5000/username/carlos/42
@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"Hello {name} you are {age} years old!"

if __name__ == "__main__":
    app.run(debug=True)
