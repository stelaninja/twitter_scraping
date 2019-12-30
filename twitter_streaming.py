import json
from tweepy import OAuthHandler, Stream, StreamListener
from twitter_auth import *

# This is a basic listener that just prints received tweets to stdout.


class StdOutListener(StreamListener):

    # on_data gives the raw data

    def on_data(self, data):
        print(json.dumps(data, indent=4, sort_keys=True))
        return True

    # on_status gives the status
    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
