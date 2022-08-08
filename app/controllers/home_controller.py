from app import app
from flask import render_template, redirect, session


@app.route('/', methods=['GET'])
def index():
    session['user_id'] = 1
    return render_template('home/home.html')
