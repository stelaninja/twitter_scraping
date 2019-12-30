# Import modules
from twython import TwythonStreamer
import sys
from requests.exceptions import ChunkedEncodingError

# Import authentication
from twitter_auth import *

# Get keywords

keywords = input("Vad vill du lyssna efter? ")

# Create the class


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            print("@{}: {}".format(username.encode(
                'utf-8'), tweet.encode('utf-8')))

    def on_error(self, status_code, data):
        print("ERROR: %s" % status_code)
        print(str(data))
        print
        self.disconnect()


# Get the stream
stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_secret
)

# Find and print the stream


def streamed():
    while True:
        try:
            stream = MyStreamer(
                consumer_key,
                consumer_secret,
                access_token,
                access_secret
            )
            stream.statuses.filter(track=keywords, stall_warnings=True)
        except ChunkedEncodingError:
            continue


streamed()

# stream.statuses.filter(track='raspberry')
