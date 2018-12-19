from requests import get
from re import compile, findall

def getYTstatus(id):
    url = ("https://www.youtube.com/watch?v={:}".format(id))

    regexp = compile(r'"submessage">[\n]\S+[\w .]+')
    loot = findall(regexp, get(url).text)

    if loot:
            return False
    else:
            return True
def getTitle(id):
    url = ("https://www.youtube.com/watch?v={:}".format(id))

    regex = compile(r'<meta name="twitter:title" content="[^.]+">')
    loot = findall(regex, get(url).text)

    for titles in loot:
        return titles.replace('<meta name="twitter:title" content="','').replace('">','')


if __name__ == '__main__':
	print (getTitle("zNcxJxBnyXQ"))
