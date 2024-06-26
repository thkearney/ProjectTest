from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
users = {'test@test.com': 'test', 'frownyface': 'nosmile'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect(url_for('success'))
    else:
        return render_template('login.html', message='Invalid username or password')

@app.route('/success')
def success():
    return 'Login successful!'
