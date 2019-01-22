from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/msadetails/')
@app.route('/msadetails/<name>')
def hello(name=None):
    return render_template('msadetails.html', name=name)