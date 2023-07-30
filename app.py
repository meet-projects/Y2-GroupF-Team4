from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route("/courses", methods=['GET','POST'])
def courses():
    return render_template('courses.html')

@app.route('/trainers', methods=['GET', 'POST'])
def trainers():
    return render_template('trainers.html')

@app.route("/events", methods=['GET','POST'])
def events():
    return render_template('events.html')

@app.route("/pricing", methods=['GET','POST'])
def pricing():
    return render_template('pricing.html')
#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)