import tweepy
import sys
from textblob import TextBlob

consumer_key='YOlFFPSJJKbKzgEbuMhuU2JRN'
consumer_secret='AYYgR0yg5poxO3n6eB0DfSObX90EVxOnbZ5BGPMORrQNdEITBf'

access_token='861214691938271233-UES8Neymh63zsvLWNmclJqgPVcssGRi'
access_token_secret='fsUdhNJq4M39uRShig6R8avauXq9ZRAyfZkPfXf9Nl10F'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('Trump')


non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

for tweet in public_tweets:
    print(tweet.text.translate(non_bmp_map))
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
