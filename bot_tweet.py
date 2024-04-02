import tweepy

consumer_key = "CmSWkBALEM21u6ngCbRIF0Wnp"
consumer_secret = "FCzKAsDjRxuimlEex9g6VOma2woORt0oCRR50xuOo68IuFXT4Z"
access_token = "887732196211142659-EY0SgnQeYZrFpbP68c7aRDzi1Oq6OOa"
access_token_secret = "CMJ0PT3upBzpWj6UIxVHLkT8pggHBQful3H421b8PXhWO"

# Autenticar na API do Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Publicar um tweet
tweet_text = "Oi, mundo!"
api.update_status(tweet_text)
