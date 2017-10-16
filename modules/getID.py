# -*- coding: utf-8 -*-
# this module is used to scrape ids from youtube playlists.... 
import re
import requests

ids = "https://www.youtube.com/playlist?list=PLRHOes-euCzw9551-2k_vGlsh_KkzoAD6"

baseYT = "https://www.youtube.com/watch?v="

onlyid = []
onetime = []

def getHTML(url):
        return requests.get(url).text

def getStatus(url):
        return requests.get(url).status_code

def getTitle(id):
    
        url = baseYT+id
        
        regex = re.compile(ur'<meta name="twitter:title" content="[^.]+">')
        loot = re.findall(regex, getHTML(url))
        for titles in loot:
            return titles.replace('<meta name="twitter:title" content="','').replace('">','')

def getID(url, s=""):
        
	regex = re.compile(r'\/watch.[v=].[^+]{11}')
	loot = re.findall(regex, getHTML(url))
	
        for i in loot:
		clean = i.replace('/watch?v=', '')
		onlyid.append(clean)
		s += str([x for x in onlyid if onlyid.count(x)==1]).replace("[]", '').replace('/watch_videoshelf":', '').replace("['']", '').replace("&", "")[2:-1]

	count = 0
	v = ""
        for j in s:
                count += 1
                v += str(j)
                if count == 13:
			onetime.append(v)
			count = 0
			v = ""
        dirtyChar = map(lambda x: x.replace("'", "").replace(' ',''), onetime)
        return dirtyChar

#for id in  getID("https://www.youtube.com/playlist?list=PLRHOes-euCzw9551-2k_vGlsh_KkzoAD6"):
    #    getTitle(id)
#print range(len(getID("https://www.youtube.com/playlist?list=PLRHOes-euCzw9551-2k_vGlsh_KkzoAD6")))

#for j in onetime:
#    print getTitle("https://www.youtube.com/watch?v="+j)

#def vidTitle(url, temp=""): 

