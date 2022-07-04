import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import colorgram

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["UPLOAD_FOLDER"] = "static/uploads/"
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
Bootstrap(app)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

## Routes 
@app.route('/')
def home():   
    return render_template("index.html")

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path =  os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)        
        flash('Image successfully uploaded and displayed below')
        # extract color info
        main_color_num = 10
        colors = colorgram.extract(save_path, main_color_num)
        color_list = [(color.rgb, round(color.proportion, 2), f"rgb({color.rgb.r},{color.rgb.g},{color.rgb.b})") for color in colors]
        #print(color_list)

        return render_template('index.html', filename=filename, colors=color_list)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True, port=5000)