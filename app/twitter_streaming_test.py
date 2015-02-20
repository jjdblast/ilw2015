#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from HTMLParser import HTMLParser
import tweet_manager as T

#Variables that contains the user credentials to access Twitter API 
access_token = "3042171819-pvrOOV7zTQyHyWRBnX9ELRMgg3tCciZwGtbSBed"
access_token_secret = "Ify6y6VZTzbMcNLKs5kVdrQ8vSnabXXQMtuFMVYTIsqiq"
consumer_key = "qrCdXHj0hVE1SXsaVbJzyayYM"
consumer_secret = "t7CEC7b0Zk8glNdmN4u0lRST8Bh6ju45GfGwlAEdJEjXxGUt6n"
geobox_edinburgh= [-3.3247789539,55.8827314464,-3.0859881461,55.9836318931]


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def __init__(self, tweet_manager,*args, **kwargs):
        self.counter=0
        self.tweet_manager = tweet_manager
        super(StdOutListener, self).__init__(*args, **kwargs)


    def on_data(self, data):
        data = json.loads(HTMLParser().unescape(data))
        write_data = {}
        write_data["place"]=data["place"]
        write_data["time_created"]=data["created_at"]
        write_data["coordinates"]=data["coordinates"]
        
        if write_data["coordinates"] is None:
            return True
        self.counter+=1

        write_data["text"]=data["text"]
        output=str(write_data)
        self.tweet_manager.process_tweet(output)    
        return True

    def on_status(self, status):
        print status.text
        if status.coordinates:
            print 'coords:', status.coordinates
        if status.place:
            print 'place:', status.place.full_name
        return True

    on_event = on_status

    def on_error(self, status):
        print status


if __name__ == '__main__':
    M=T.TweetManager()
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener(tweet_manager=M)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(locations=geobox_edinburgh)

