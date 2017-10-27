# listentothis.datapor.no

## About
listentothis, is a simple flask site where it's grabbing top 100 newest youtube posts (that are youtube links..ofc) at the /r/listentothis subreddit.
Then when you visit the site it will pick a random id.

## Install
```bash
pip install -r requirements.txt

./runserver.py
```

## Todo
- [] Refresh/update the set of id's every n-hours.
- [] Update the session rather than forcing a reload of the site.
