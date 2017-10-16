from flask import Flask, request, render_template
from modules.getRandItem import *
from modules.getYTstatus import *
from modules.getID import *
from modules.reddit import *
import logging
import random
import os

app = Flask(__name__)

#ids = ['_8-RMP3UyT8', 'dh-xVv5vTZc','euEDMWjes0E','TKXFBUn6lQA','_lnAtIS4wVg','fHWHJRx4D44','Iq06K70bneE','K2algR1qzPA', 'Ax5Hqg5FmSs', 'dHl6IK27FpE', 'xzYEccyx4ks', 'VaEbPrZfFqE', 'IuJVoy4Yo0w', 'T6JsFLmAKKQ', 'xn0-RBOSsGQ', 'W_wXNpHIwYs', 'p4PBShvrf4k','-6s_eRHYqVM','BKqZD1usygI','OdixqnfcqeA','V5RVP3u6BaY','fciUDhYrty8','ZALAB5lgG0I', 'cuMJH5pNAME', 'dYPPSU9ULFY', '_VEFR7BXXZw', 'm60FqY6Jags', 'j0xTkipsKM8', 'VSSFG_pNPg0', 'Y3jpQkBb36w', 'DC0LV8Uf_-Y', '3r3dwA0a-lY', 'LElTCvDN7Dg','id7_tSVDEG0','rFjcYwU69r8','XZHlhr_JEv4','bcPNOtK0JpA','R0UaiMHI4M4', 'vzxZzIiO84Yh', 'hQI-hko4eDI', 'Tz_iUQQ2hI4', '1T4OIw8fj7c', 'UmH782k3jKU', 'PPdU7_rqbqA', 'lc7wmkDgbaI', '_hedfvz-Rfw', 'G6k8D1Tzv3U', 'yN8TUgkPnbU','yb8nXwDMLb0','jJN1A_DHtsM','YWnE2eBB2mA','LhiaB9VYOYA','l4XCygw5_1o', 'n_3iZzYrLJA', 'eZaJL0g6R0k', 'dOMH9OHWXHE', 'E5SYKfA8K40', '-fWRJc_mzN8', 'I3ZQHVvxXTs', 'BaGikAngvWY', 'EDggq272KJ0', 'LfDrezpidBo', '4j-dv3Aege0', 'TKVS7vr3SqU', '4o2GGY2ybzU', 'hW5ZVy_pWZU', '4RNJ6hX2lEk','tnw1Kd2vhhw', 'bhVgQW3UhFM', 'e3ZBjOgThts', '81UsVPsAqxw', '8eSQrqHXYYM', 't4HaTd3NUNI', 'uJv06cj8nlg', 'EGJ7z7khKyA', 'drWHAvI9yp4', '1j25A_rN3u0', 'yijXnW9o5HM', 'fnKwkDCNjrU', 'gW-ucfCxM28', 'WLKr4RygOUU', 'tVS7b1bh4ts', 'AS2zBIgwui0', 'MAvH0bKWwew']

@app.route('/')
def homepage():
 
    musicUrlFinder('listentothis', 'new')
    rand = getRandItem(FindYoutubeID())
    yt_url = 'https://www.youtube.com/watch?v={video_id}'.format(video_id=rand)
    print len(rand)
    print rand
    if len(rand) == 0: 
        return render_template('VideoNotFound.html'), 404

    elif (len(rand) != 0) and (getYTstatus(yt_url)):
        print "[+] i Found id's {0}".format(len(FindYoutubeID()))
        return render_template('index.html', yt_id=rand, yt_name=getTitle(rand)), 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':

    app.run(host="0.0.0.0",port=8069 ,debug=True, threaded=True)
    #reddit.musicUrlFinder('listentothis')
    #reddit.gatherYTIds()
    #print onlyID

