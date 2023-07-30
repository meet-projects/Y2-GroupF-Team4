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

@app.route("/scholarships", methods=['GET','POST'])
def scholarships():
    return render_template('scholarships.html')

@app.route('/alumani', methods=['GET', 'POST'])
def alumani():
    return render_template('alumani.html')

@app.route("/events", methods=['GET','POST'])
def events():
    return render_template('events.html')

@app.route("/studentlife", methods=['GET','POST'])
def studentlife():
    return render_template('studentlife.html')
#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)