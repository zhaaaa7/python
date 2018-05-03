import tweepy
from tweepy import OAuthHandler
import json

from lab9_config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authorization setup to access the Twitter API
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

tweets = api.user_timeline(id='taylorswift13' ,count=1) # insert code here to fetch tweets
for i in tweets:
	i=i._json
	print(i['id'],i['text'],i['favorite_count'],i['entities']['hashtags'])