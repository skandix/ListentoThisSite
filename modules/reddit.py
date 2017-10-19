import config
import praw
import re

# lists for collected songs.
youtube = []
onlyID = set()
SAVEDLOOT = 'pickles/loot.p'

def musicUrlFinder(thread, cat):
    r = praw.Reddit(client_id=config.r_cli_id
                    ,client_secret=config.r_cli_secret
                    ,user_agent=config.r_user_agent) 
    sub = r.subreddit(thread)

    if cat is "new":
        for subz in sub.new():
            if "youtube" in subz.url or "youtu.be" in subz.url:
                if subz.url not in youtube:
                   youtube.append(subz.url)
                else:
                    pass

    elif cat is "hot":
        for subz in sub.hot():
            if "youtube" in subz.url or "youtu.be" in subz.url:
                if subz.url not in youtube:
                   youtube.append(subz.url)
                else:
                    pass

    elif cat is "top":
        for subz in sub.top():
            if "youtube" in subz.url or "youtu.be" in subz.url:
                if subz.url not in youtube:
                   youtube.append(subz.url)
                else:
                    pass
    parseURLs()

def parseURLs():
    """
    Parses all the urls in the youtube list, fetching IDs from "nicely formated" youtube URLs and puts them into a
    set of IDs for later usage. E.g.
    https://www.youtube.com/watch?v=spu32SLIdlU
    youtu.be/spu32SLIdlU
    """
    for url in youtube:
        loot = re.search(r'(v=|\.be\/)([\w\d\-]{11})',url)
        if loot is not None:
            onlyID.add(loot.group(2))
    #saveIDs()

def getRandomID():
    """
    :return: A random ID from the set onlyID
    """
    import random
    return random.sample(onlyID,1)[0]

def saveIDs():
    """
    Saves the IDs in onlyID to disk
    """
    import pickle
    pickle.dump(onlyID, open(SAVEDLOOT,'wb'))

def loadIds():
    """
    Loads the IDs into onlyID from disk if it exists
    """
    import pickle, os.path
    if os.path.isfile(SAVEDLOOT):
        global onlyID
        onlyID = pickle.load(open(SAVEDLOOT,'rb'))

def FindYoutubeID():

    output = []

    for k in youtube:
        loot = re.search(re.compile(r'(?:\/watch.([v=]+[^+]{11})|youtu.be/([^+]{11}))'), k)
        if loot:
            if "/watch?v=" in loot.group():
                watchId = str(loot.group()).replace('/watch?v=', '')
                if watchId not in output:
                    output.append(watchId)
                else:
                    pass

            else:
                if loot.group() not in output:                
                    output.append(loot.group())
                else:
                    pass

    return output
#musicUrlFinder('listentothis', 'new')
#FindYoutubeID(youtube)
