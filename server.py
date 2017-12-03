#!/bin/python
from modules.reddit import musicUrlFinder, getRandomID
from flask import Flask, request, render_template
from modules.youtube import checkVideoById
import logging
from logging.handlers import RotatingFileHandler
import json

app = Flask(__name__)

@app.route('/')
def homepage(rand = "", title= ""):

    musicUrlFinder('listentothis', 'new')

    # Fetch a random ID until we get a valid one
    while(len(title) == 0):
        rand = getRandomID()
        title = checkVideoById(rand)

    app.logger.info("[+] Found ID: {0}".format(rand))
    app.logger.info("[+] Title: {0}".format(title.encode('utf-8')))

    # passing arguments as a list, then you can recall them by index
    return render_template('index.html', args=[rand, title])

@app.route('/status')
def status():
    status={
        'totalID':len(rand)
    }
    return json.dumps()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    formatter = logging.Formatter( "%(asctime)s | %(pathname)s:%(lineno)d | %(funcName)s | %(levelname)s | %(message)s ")
    handler = RotatingFileHandler('logs/app.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)
    app.run(host="0.0.0.0",port=4020 ,debug=False, threaded=True)


