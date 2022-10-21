from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
from config import settings

app = Flask(__name__)
db = MySQL(app)


@app.route('/')
def index():
    return redirect( url_for('login') )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        return render_template('auth/login.html')
        
    return render_template('auth/login.html')
