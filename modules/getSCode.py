#don't even know why i have this... wtf...
import requests

def is_url_ok(url):
	return 200 == requests.head(url).status_code

#print ("https://www.youtube.com/watch?v=hopYXDBQIso")
#print requests.head("https://www.youtube.com/watch?v=hopYXDBQIso").status_code
