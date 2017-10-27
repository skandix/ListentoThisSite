#!/bin/python
from modules.reddit import musicUrlFinder, getRandomID
from flask import Flask, request, render_template
from modules.youtube import checkVideoById
import random
import os

app = Flask(__name__)

@app.route('/')
def homepage(rand = "", title= ""):

    musicUrlFinder('listentothis', 'new')

    # Fetch a random ID until we get a valid one
    while(len(title) == 0):
        rand = getRandomID()
        title = checkVideoById(rand)

    print "[+] Found ID: {0}".format(rand)
    print "[+] Title: {0}".format(title.encode('utf-8'))

    # passing arguments as a list, then you can recall them by index
    return render_template('index.html', args=[rand, title])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4020 ,debug=False, threaded=True)
