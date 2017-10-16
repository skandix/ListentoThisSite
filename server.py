from flask import Flask, request, render_template
from modules.getRandItem import *
from modules.getYTstatus import *
from modules.getID import *
from modules.reddit import onlyID

import modules.reddit

import logging
import random
import os

app = Flask(__name__)

@app.route('/',)
def homepage():
    
    rand = getRandItem(reddit.onlyID)
    yt_url = 'https://www.youtube.com/watch?v={video_id}'.format(video_id=rand)
    print len(rand)
    if len(rand) == 0: 
        return render_template('VideoNotFound.html'), 404

    elif (len(rand) != 0) and (getYTstatus(yt_url)):
        print "[+] i Found id's {0}".format(len(getID(baseURL)))
        return render_template('index.html', yt_id=rand, yt_name=getTitle(rand)), 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8069 ,debug=True, threaded=True)
    reddit.musicUrlFinder('listentothis')
    reddit.gatherYTIds()
    print onlyID

