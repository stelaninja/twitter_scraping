# -*- coding: utf-8 -*-

# Import the modules
import tweepy
import sys
import time

from twitter_auth import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Get username

username = input("Vilket användarnamn? ")


# tweets = tweepy.Cursor(api.user_timeline, id=username, tweet_mode='extended').items(10)
tweets = api.user_timeline(username, tweet_mode='extended')

print("Recieving tweets for @" + username + "...\n")
for tweet in tweets:
    print(str(tweet.id) + ' - ' + tweet.full_text)
    print(" ")
