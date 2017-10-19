from flask import Flask, request, render_template
from modules.getRandItem import *
from modules.getYTstatus import *
from modules.getID import *
from modules.reddit import *
import logging
import random
import os

app = Flask(__name__)

@app.route('/')
def homepage():
 
    musicUrlFinder('listentothis', 'new')
    rand = getRandomID()
    print "[+] i Found id's {0}".format(len(rand))
    print "\n{0}\n{1}\n".format(rand,getRandomID())

    # Checks if video is avaliable here...
    if getYTstatus(rand):
        return render_template('index.html', yt_id=rand)
    else:
        return render_template('VideoNotFound.html'), 404
       

@app.errorhandler(404)
def page_not_found(e):
    return render_template('VideoNotFound.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8069 ,debug=False, threaded=True)
