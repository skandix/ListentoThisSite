import config
import praw
import json
import re

# lists for collected songs.
youtube = []
onlyID = []

def musicUrlFinder(thread):
    r = praw.Reddit(client_id=config.r_cli_id
                    ,client_secret=config.r_cli_secret
                    ,user_agent=config.r_user_agent) 
    sub = r.subreddit(thread)
    
    for subz in sub.new():
        if "youtube" in subz.url or "youtu.be" in subz.url:
            if subz.url not in youtube:
               youtube.append(subz.url)
            else:
                pass

def gatherYTIds():
    ids = []

    youtubeString = ''.join(youtube)
    loot = re.findall(re.compile(r'(?:\/watch.([v=]+[^+]{11})|youtu.be/([^+]{11}))'), youtubeString)

    for strippedID in loot:
        Youtube = strippedID[0].replace('v=','').strip()
        Youtu_be = strippedID[1].strip()
        ids.append(Youtube)
        ids.append(Youtu_be)

    encodeList = [x.encode('UTF8') for x in ids]
    for Id in encodeList:
        Id = Id.rstrip()
        if Id is "":
            pass
        else:
            onlyID.append(Id)
    
    print onlyID

    jsonDump(onlyID)

def jsonDump(listing):
    with open('youtube.json', 'w') as fp:
        json.dump(listing, fp)

def startup():
    global Loaded
    with open('youtube.json') as data:
        Loaded = json.load(data) 
    return "Found {:} ID's from Previous run\nLooking for new ones".format(len(Loaded))

# print startup()
# while True:
#    print "RRRRRRunning"
#    musicUrlFinder('listentothis')
#    gatherYTIds()
