#coding=utf8

from flask import render_template, url_for
from learnflask.blue import bpp

@bpp.route('/')
def index():
    #print bpp.root_path
    #print url_for('bpp.index')
    #print url_for('bpp.static', filename='google.png')
    #/home/rxs/workspace/projects/flask-exp/learnflask/blue
    #/bpp/
    #/bpp/static/google.png
    return render_template('index.html')
