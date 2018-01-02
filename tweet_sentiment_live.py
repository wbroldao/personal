#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 12:51:47 2018

@author: nito
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="bbOt9qUUt5qCsczbeg7dczMzA"
csecret="iSPzAIgW5rGHEwHo2JHMlkxHWVbpYD3hmv7E82rF80cV7O6evM"
atoken="156026116-T7D1kt8OCjzhVD0ankYcaIZeUinfJxoLmBU6g3aC"
asecret="9yu0HxRfaxDLsRtm7L7cVr0DmK2mmRxNAxI0NOVQnOBs"

class listener(StreamListener):
    
    def on_data(self, data):
        
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)
        
        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
            
            return True

    def on_error(self, status):
        
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])