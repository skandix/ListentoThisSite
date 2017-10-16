import config
import praw
import json
import re

# lists for collected songs.
youtube = []
onlyID = []

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
