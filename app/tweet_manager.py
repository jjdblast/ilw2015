from datetime import datetime
import ast
import re
import os


class TweetManager(object):
    
    def __init__(self):
        self.geobox_edinburgh= [-3.3247789539,55.8827314464,-3.0859881461,55.9836318931]


    def test_loc(self, tweet):
        latitude = tweet["latitude"]
        longitude = tweet["longitude"]
        if (latitude > self.geobox_edinburgh[-1]) or (latitude < self.geobox_edinburgh[1]):
            return False
        if (longitude < self.geobox_edinburgh[0]) or (longitude > self.geobox_edinburgh[2]):
            return False
        return True
    
    def process_tweet(self, tweet, rafael_style=False):
        tweet=self.make_dict(tweet, rafael_style)
        if tweet is None:
            return
        if tweet["text"] is None:
            return

        tweet["text"]=self.clean_tweet(tweet["text"])
        if tweet["text"] is None:
            return
        if self.test_loc(tweet):
            tweet=self.get_sentiment(tweet)
            if tweet["sentiment"] is None:
                return
            self.write_tweet_dict(tweet)
        
        
    def write_tweet_dict(self,tweet):
        time=tweet["time"]
        date=self.get_date(time)
        sentiment = tweet["sentiment"]
        filename="%s.txt" % date
        if sentiment==0:
            return

        for key in tweet.keys():
            try:
                tweet[key]=tweet[key].replace("\n", "")
            except AttributeError:
                pass
        path=os.path.join("data", filename)
        f=open(path, "a")
        output="%s\t%s\t%s\t%s\t%s\n" % (tweet["sentiment"], tweet["longitude"],
                        tweet["latitude"], tweet["time"],
                        tweet["text"])
        print output
        f.write(output)
        f.close()

    def get_sentiment(self, tweet):
        #Speaks to Rafael's code, returns sentiment.
        f=os.popen("java Client " + "\""+tweet["text"]+"\"")
        sentiment=f.read()
        sentiment=sentiment.replace("\n", "")
        if len(sentiment)==0:
            tweet["sentiment"]=None
        else:
            tweet["sentiment"]=int(sentiment)
        return tweet
        
    def clean_tweet(self, tweet):
        #Removes weird characters new line characters and so on.
        tweet=tweet.strip()
        if len(tweet)==0:
            return None
        tweet= tweet.decode('unicode_escape').encode('ascii','ignore')
        tweet=tweet.strip()
        if len(tweet)==0:
            return None
        tweet=tweet.replace("\r\n", "").replace("\n", "")
        if len(tweet)==0:
            return None
        return tweet
    
    def make_dict(self,tweet, rafael_style=False):
        if tweet is None:
            return None
        if rafael_style:
            '''
            Tweets look like:
                What kind of fool do you take me for? But I heard all that before!	GeoLocation{latitude=55.98595606, longitude=-3.19085809}	Sat Feb 14 20:41:14 GMT 2015
            '''
            tweet=tweet.split("\t")
            text=tweet[0]
            loc=tweet[1]
            time=tweet[2]
            locs=re.findall(pattern=".*latitude=(.*),.*longitude=(.*)}",string=loc,
                flags=re.DOTALL)[0]
            longitude = float(locs[1])
            latitude  = float(locs[0])
            tweet_dict={"time":time, "text":text, "longitude":longitude,
                        "latitude":latitude}
            return tweet_dict
        else:
            '''
            Tweets look like:
                {'text': u'Thieves steal \xa370,000 in raid on security firm at industrial estate \n\nhttp://t.co/D3anAMRlbT http://t.co/RxwDnlZY1d STV', 'place': {u'full_name': u'Edinburgh, Scotland', u'url': u'https://api.twitter.com/1.1/geo/id/7ae9e2f2ff7a87cd.json', u'country': u'United Kingdom', u'place_type': u'city', u'bounding_box': {u'type': u'Polygon', u'coordinates': [[[-3.3285119, 55.894729], [-3.3285119, 55.991662], [-3.077505, 55.991662], [-3.077505, 55.894729]]]}, u'country_code': u'GB', u'attributes': {}, u'id': u'7ae9e2f2ff7a87cd', u'name': u'Edinburgh'}, 'coordinates': {u'type': u'Point', u'coordinates': [-3.206273, 55.951663]}, 'time_created': u'Tue Feb 17 11:05:35 +0000 2015'}
            '''
            tweet=ast.literal_eval(tweet)
            loc= tweet["coordinates"]

            if loc is None:
                return None
            else:
                loc = loc["coordinates"]
                
                latitude = float(loc[1])
                longitude = float(loc[0])
            tweet_dict={"text":tweet["text"],"time":tweet["time_created"].replace("\n",""),
                        "longitude":longitude, "latitude":latitude}
            return tweet_dict
                                         
            
    def format_tweet(self, tweet):
        text=tweet["text"]
        longitude = tweet["longitude"]
        latitude = tweet["latitude"]
        time = tweet["time"]
        output = "%s\t[%s, %s]\t%s\n" % (text, latitude, longitude, time)
        return output
    
    
        
    def get_datetime(self, time):
        time=time.replace("GMT ", "")
        time=time.replace("+0000 ", "")
        time=time.strip()
        date_format="%a %b %d %H:%M:%S %Y"
        dt=datetime.strptime(time, date_format)
        return dt
    
    def get_date(self, time):
        dt = self.get_datetime(time)
        return dt.date().strftime("%d-%m-%y")
        
