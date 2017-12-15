print ("¿Que Termino desea buscar?")
datouno = input()
datouno = str(datouno)

import tweepy
from textblob import TextBlob

consumer_key = "3mlgum1YcG0AUckDaEUfPu1ru"
consumer_secret = "1r7FssSYPwBDBi3sKmI2IKMuCBZQjKSx0irvdfQNcVRA4KBjGF"

access_token = "712533602102284288-APB4heLQMkM9BSGy4L6FrDedgpTX1YV"
access_token_secret = "EPatAxW5bccl3jCkAursJLHIOZ2R3OiLhIUvvmHQrFxfa"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api= tweepy.API(auth)

public_tweets = api.search(datouno)

for tweet in (public_tweets):
	print (tweet.text)
	analysis = TextBlob(tweet.text)
	print (analysis.sentiment)
	print ("\n")
	print ("\n")


