from flask import Blueprint

from .libs.getYTstatus import getYTstatus

#from libs.reddit import musicUrlFinder, getRandomID
#from libs import getYTstatus


root = Blueprint('root', __name__, template_folder='templates')

@root.route('/')
def homepage(rand = "", title= ""):
    #musicUrlFinder('listentothis', 'new')

    # Fetch a random ID until we get a valid one
    #while(len(title) == 0):
    #    rand = getRandomID()
    #    title = checkVideoById(rand)

    #print("[+] Found ID: {0}".format(rand))
    #print("[+] Title: {0}".format(title.encode('utf-8')))

    # passing arguments as a list, then you can recall them by index
    #return render_template('index.html', args=[YspnoiJFSus, klauz])
    return getYTstatus("asdjasdjasd")


