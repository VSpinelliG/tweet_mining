'''
Inspired by https://pythondata.com/collecting-storing-tweets-with-python-and-mongodb/
developed by Eric D. Brown, D.Sc.
'''

import tweepy
import json
from pymongo import MongoClient
 
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
 
    def on_data(self, data):
        #Mongodb Cloud Atlas connection
        try:
            client = MongoClient('mongodb+srv://vinicius:vsg.983004@cluster-u6dxe.mongodb.net/test?retryWrites=true&w=majority')
            
            db = client.twitterdb

            datajson = json.loads(data)
            
            db.twitter_bolsonaro.insert_one(datajson)
        except Exception as e:
            print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True, retry_count=10, timeout=300))
streamer = tweepy.Stream(auth=auth, listener=listener)

WORDS = ['Bolsonaro', 'Jair Bolsonaro', 'Bolsominion', 'Bolsomito']

print("Tracking: " + str(WORDS))
streamer.filter(languages=["pt"], track=WORDS)