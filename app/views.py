from flask import render_template, request
from app import app


@app.route('/')
def index():
    return render_template('index.html')


#@app.route('/about')
#def about():
#    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')

