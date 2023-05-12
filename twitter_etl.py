import pandas as pd
import tweepy
import json
from datetime import datetime
import s3fs
import config_file


# twitter auth

auth = tweepy.QAuthHandler(config_file.access_key , config_file.access_secret)
auth.set_access_token(config_file.consumer_key , config_file.consumer_secret)

# creating an api object 

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = '@elonmusk',
                           count = 200,
                           include_rts = False,
                           tweet_mode = 'extended'
                           )

print(tweets)



