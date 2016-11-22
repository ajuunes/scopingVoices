import os
import sys
import urllib2
import requests

import json
import pandas as pd

from tweepy import Stream
from twython import Twython
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# credential area 

access_token = "replace"
access_token_secret = "replace"
consumer_key = "replace"
consumer_secret = "replace"

# you make the call
twit = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

# search paramters - https://dev.twitter.com/rest/reference/get/search/tweets
fucker = twit.search(q='#periscope', result_type='recent', count=1)
#print json.dumps(fucker, indent=4, sort_keys=True)

# grab that first one and break it apart to get at the meat

def check():
    checker = fucker['statuses'][0]['entities']['urls']
    if checker == None:
        return false
    else:
        return true

try:
    tweet = fucker['statuses'][0]['entities']['urls'][0]['expanded_url']
except KeyError, e:
    print e

parts = tweet.split('/')
broadcast_id = parts[4]

dammit  = fucker['statuses'][0]['entities']['hashtags']

# using the public peri api to access the HLS, or HTTP Live Streaming url
periAccessURL = 'https://api.periscope.tv/api/v2/accessVideoPublic?broadcast_id='+ broadcast_id
r = requests.get(periAccessURL)
fullPeriData = r.json()

#print json.dumps(data, indent=4, sort_keys=True)

print "STREAMLINK"

streamLink = fullPeriData['hls_url']
print streamLink

'''
file = open("chatID.txt", "w")
file.write(chatBroadID)
file.write(" - ")
file.write(streamLink)
file.close()
'''
os.system("vlc -vvv %s" % str(streamLink))

