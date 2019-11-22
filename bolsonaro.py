'''
Inspired by https://pythondata.com/collecting-storing-tweets-with-python-and-mongodb/
developed by Eric D. Brown, D.Sc.
'''

import tweepy
import json
from pymongo import MongoClient
from urllib3.exceptions import ProtocolError
 
CONSUMER_KEY = "wCG28mEeJD9oszKHAN2QoaBUb"
CONSUMER_SECRET = "DEr3pBDCQzZx3j2WebgprqI1AhIwKz9pBK2YEJd3OURSutcc4Y"
ACCESS_TOKEN = "342516024-DCBkJqpakJBvVbhIRA9i0ZUAjvpDfxXIfF6UsKh4"
ACCESS_TOKEN_SECRET = "XauVvi599ZW8c0IBxEV7b2jPgCcZAfkHydCsDde9YBvao"
 
 
class StreamListener(tweepy.StreamListener):    
 
    def on_connect(self):
        print("Successful API connection!")
 
    def on_error(self, status_code):
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def getText(self, data):       
        # Try for extended text of original tweet, if RT'd (streamer)
        try: text = data['retweeted_status']['extended_tweet']['full_text']
        except: 
            # Try for extended text of an original tweet, if RT'd (REST API)
            try: text = data['retweeted_status']['full_text']
            except:
                # Try for extended text of an original tweet (streamer)
                try: text = data['extended_tweet']['full_text']
                except:
                    # Try for extended text of an original tweet (REST API)
                    try: text = data['full_text']
                    except:
                        # Try for basic text of original tweet if RT'd 
                        try: text = data['retweeted_status']['text']
                        except:
                            # Try for basic text of an original tweet
                            try: text = data['text']
                            except: 
                                # Nothing left to check for
                                text = ''
        return text
    
    def on_data(self, data):
        #Mongodb Cloud Atlas connection
        client = MongoClient('mongodb+srv://vinicius:vsg.983004@cluster-u6dxe.mongodb.net/test?retryWrites=true&w=majority')
        
        db = client.twitterdb

        datajson = json.loads(data)

        tweet_text = self.getText(datajson)

        jsonbd = { "id" : datajson["id"], "text" : tweet_text }
        
        db.tweet_bolsonaro.insert_one(jsonbd)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True, retry_count=10, timeout=300))
streamer = tweepy.Stream(auth=auth, listener=listener)

WORDS = ['Bolsonaro', 'Jair Bolsonaro', 'Bolsominion', 'Bolsomito', 'Presidente Bolsonaro',
'Presidente Jair Bolsonaro']

print("Tracking: " + str(WORDS))

while True:
    try:
        streamer.filter(languages=["pt"], track=WORDS)
    except (ProtocolError, AttributeError):
        continue