# Importh the modules
from twython import Twython
import sys

# Import Twitter API keys
from twitter_auth import *

# Set authentication

twitter = Twython(
	consumer_key,
	consumer_secret,
	access_token,
	access_secret
)

# Get message

tweet = raw_input("What do you want to tweet? ")

# Send tweet

if tweet == "":
	print("Unable to tweet nothing!")
	sys.exit()

else:
	twitter.update_status(status=tweet)
	print("Tweeted: %s" % tweet)

