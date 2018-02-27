# importing the module
import tweepy
 
# personal details
consumer_key ="wM26QpzQJtrDBP5xvnIbTzT2W"
consumer_secret ="5TOwSmPGDo9TXbmExGLDRh3fx8XsD5KLoxAQyqeGM91OylmfsA"
access_token ="967252154720423936-lnUYpmeWyXhWtXZ2fKlJrmtTfO1YvKn"
access_token_secret ="LBMn727ycFTUV4rbo7iiNn9gdevyzetto5gsRUfWk3lEu"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
