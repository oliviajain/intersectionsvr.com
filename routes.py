from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/goals')
def goals():
    return render_template("goals.html")

@app.route('/team')
def team():
    return render_template("team.html")