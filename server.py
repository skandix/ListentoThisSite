from flask import Flask, request, render_template
import json

from modules.reddit import musicUrlFinder, getRandomID
from modules.youtube import getTitle, getYTstatus

app = Flask(__name__)

@app.route('/')
def homepage(rand = "", title= ""):

    musicUrlFinder('listentothis', 'new')
    rand = getRandomID()
    title = getTitle(rand)

    print("[+] Found ID: {0}".format(rand))
    print("[+] Title: {0}".format(title.encode('utf-8')))

    if getYTstatus(rand):
        return render_template('index.html', args=[rand, title])
    else:
        return

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4020 ,debug=False, threaded=True)


