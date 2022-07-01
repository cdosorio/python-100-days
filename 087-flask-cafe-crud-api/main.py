from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import requests
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

# API is from class 62 (This client website will run in port 5001)
CAFE_API_BASE_URL = "http://localhost:5000/"
CAFE_API_KEY = "TopSecretAPIKey"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CreateCafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    location = StringField('Location (Address)', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CreateCafeForm()
    if form.validate_on_submit():
        url_add_cafe = f"{CAFE_API_BASE_URL}add"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        cafe_params = {
            'name': form.name.data,
            'map_url': form.map_url.data,
            'img_url': form.img_url.data,
            'location': form.location.data
        }

        print(cafe_params)
        response = requests.post(url=url_add_cafe, data=cafe_params, headers=headers) 
        response.raise_for_status()
        #exercise_response = response.json()
        print(f"response: {response.text}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    # class 62 used a csv     
    url_cafes = f"{CAFE_API_BASE_URL}all"
    response = requests.get(url=url_cafes)
    data = response.json()
    cafes = data["cafes"]
    return render_template('cafes.html', cafes=cafes)

@app.route("/delete")
def delete():
    cafe_id = request.args.get('id')
    url_delete = f"{CAFE_API_BASE_URL}report-closed/{cafe_id}?api-key={CAFE_API_KEY}"
    requests.delete(url_delete)
    return redirect(url_for('cafes'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
