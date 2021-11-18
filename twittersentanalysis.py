import tweepy
import sys
from textblob import TextBlob

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('Trump')


non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

for tweet in public_tweets:
    print(tweet.text.translate(non_bmp_map))
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
