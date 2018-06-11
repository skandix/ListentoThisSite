import praw
import re

# lists for collected songs.
youtube = []
onlyID = set()
SAVEDLOOT = 'pickles/loot.p'

def musicUrlFinder(thread, categy):

    r = praw.Reddit(client_id='clientID'
                    ,client_secret='clientSecret'
                    ,user_agent='listen.datapor.no'
    sub = r.subreddit(thread)

    if category is "new":
        for subreddit in sub.new():
            if "youtube" in subreddit.url or "youtu.be" in subreddit.url:
                if subreddit.url not in youtube:
                   youtube.append(subreddit.url)
                else:
                    pass

    elif category is "hot":
        for subreddit in sub.hot():
            if "youtube" in subreddit.url or "youtu.be" in subreddit.url:
                if subreddit.url not in youtube:
                   youtube.append(subreddit.url)
                else:
                    pass

    elif category is "top":
        for subreddit in sub.top():
            if "youtube" in subreddit.url or "youtu.be" in subreddit.url:
                if subreddit.url not in youtube:
                   youtube.append(subreddit.url)
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


