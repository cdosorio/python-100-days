from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import DateTime, func
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

## CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## CONFIGURE TABLE
class TodoItem(db.Model):
    __tablename__ = "TodoItem"
    id = db.Column(db.Integer, primary_key=True) 
    description = db.Column(db.String(250), unique=False, nullable=False)    
    time_created = db.Column(DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(DateTime(timezone=True), onupdate=func.now())
    done = db.Column(db.Boolean, nullable=False)    
#db.create_all()


## WTForm
class CreateTodoForm(FlaskForm):
    description = StringField("Task:", validators=[DataRequired()])    
    submit = SubmitField("Submit Post")


## Routes 
@app.route('/')
def get_all_todos():
    todos = TodoItem.query.all()
    return render_template("index.html", all_todos=todos)

@app.route("/new-post", methods=["GET", "POST"])
def add_todo():
    form = CreateTodoForm()
    if form.validate_on_submit():
        new_todo = TodoItem(
            description = form.description.data,
            done = False
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("get_all_todos"))
    return render_template("add-todo.html", form=form)

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = TodoItem.query.filter_by(id=todo_id).first()
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("get_all_todos"))

@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    todo_to_delete = TodoItem.query.get(todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_todos'))
    

if __name__ == "__main__":
    app.run(debug=True, port=5002)