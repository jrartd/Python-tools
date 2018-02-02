from twitter import *

access_token = "712533602102284288-QGxqYcFiQlGZGTaoNIgHgq2KZxqZeeH"
access_token_secret = "rlH5ItRHtlguzChQbIvLDo1yYCu47liEtq8fdVgeOZpb9"
consumer_key = "VWe4b0p7vRcVS06gbJyS83dIS"
consumer_secret = "PjkoSJ4YxPXo4V9Uk7bazq4y507e6zBr96q7u2OlJeP1aVZd7w"
texto_tweet = input("Ingrese el texto a twittear")

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

t.statuses.update(status= texto_tweet)

