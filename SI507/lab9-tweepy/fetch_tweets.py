import tweepy
from tweepy import OAuthHandler
import json

from lab9_config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authorization setup to access the Twitter API
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)



# Fetch Taylor Swift's 300 most recent tweets and save them to tweets.json
with open('tweets.json', 'w') as json_file:
	page = 1
	while True:
		tweets = api.user_timeline(id='taylorswift13' ,count=20) # insert code here to fetch tweets
		if tweets:
			for tweet in tweets:
				# Make sure you limit the number of tweets to 300.
				json_tweet = tweet._json # convert to JSON format
				# Write the tweet to tweets.json
				json_file.write(str(json_tweet)+'\n')
		else:
			break
		page += 1

		# Make sure you limit the number of tweets to 300.
		if page > 15:
			break

