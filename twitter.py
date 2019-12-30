# Importing the modules
import urllib2
import json

# User chooses tweet
screen_name = raw_input("Which tweet do you want to search? ")

# Twitter API
url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + screen_name

# Get the tweets
data = json.load(urllib2.urlopen(url))

# Print the result
print len(data), "tweets"

for tweet in data:
	print tweet['text']
