#coding=utf8

from flask import render_template
from learnflask import app

@app.route('/')
def index():
    return render_template('index.html')
