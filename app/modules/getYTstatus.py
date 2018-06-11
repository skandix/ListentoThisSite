import requests
import re

def getYTstatus(id, yt="https://www.youtube.com/watch?v="):
	regexp = re.compile(ur'"submessage">[\n]\S+[\w .]+')
	loot = re.findall(regexp, requests.get(yt+id).text)
	if loot:
		return False
	else:
		return True
