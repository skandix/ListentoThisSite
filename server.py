from flask import Flask, request, render_template
from modules.getYTstatus import *
from modules.reddit import *
from modules.youtube import *
import logging
import random
import os

app = Flask(__name__)

@app.route('/')
def homepage():
 
    musicUrlFinder('listentothis', 'new')
    rand = ""
    title = ""
    # Fetch a random ID until we get a valid one
    while(len(title) == 0):
        rand = getRandomID()
        title = checkVideoById(rand)
    print "[+] i Found id {0}".format(rand)
    print "[+] Title {}".format(title.encode('utf-8'))
    if getYTstatus(rand):
        return render_template('index.html', yt_id=rand,title=title)
    else:
        return render_template('VideoNotFound.html'), 404
       

@app.errorhandler(404)
def page_not_found(e):
    return render_template('VideoNotFound.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8069 ,debug=False, threaded=True)
