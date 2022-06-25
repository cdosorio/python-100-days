from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello"

def make_bold(function):
    def wrapper_fn():
        return f"""
                <strong>
                {function()}
                </strong>
                """
    return wrapper_fn

def make_underlined(function):
    def wrapper_fn():
        return f"""
                <u>
                {function()}
                </u>
                """
    return wrapper_fn

@app.route("/bye")
@make_bold
@make_underlined
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
