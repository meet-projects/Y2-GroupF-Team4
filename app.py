from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


Config = {
    'apiKey': "AIzaSyCfnx6cn3LTdQT2dnM-p4sujkJpnNbSd8Q",
    'authDomain': "ghis-school.firebaseapp.com",
    'databaseURL': "https://ghis-school-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "ghis-school",
    'storageBucket': "ghis-school.appspot.com",
    'messagingSenderId': "784019588579",
    'appId': "1:784019588579:web:8123304ed3443173338cd6",
    'measurementId': "G-B28L6BZZC0"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()



#Code goes below here
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route("/scholarships", methods=['GET','POST'])
def scholarships():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            text = request.form['schoolarTalk']
            application = {"name": name,"email": email, "text": text}
            db.child("Applications").push(application)
            return redirect(url_for('scholarships'))
        except:
            error = "error"
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

@app.route('/comments', methods=['GET','POST'])
def comments():
    if request.method == 'POST':
        try:
            name = request.form['username']
            email = request.form['email']
            text = request.form['comment']
            comment = {"username": name,"email": email, "comment": text}
            db.child("Comments").push(comment)
            comments = db.child("Comments").get().val()
            return render_template('comments.html', comments = comments)
        except:
            error = "error"
    comments = db.child("Comments").get().val()
    return render_template('comments.html', comments=comments)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)