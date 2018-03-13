import os
import time
import tweepy
consumer_key ="wM26QpzQJtrDBP5xvnIbTzT2W"
consumer_secret ="5TOwSmPGDo9TXbmExGLDRh3fx8XsD5KLoxAQyqeGM91OylmfsA"
access_token ="967252154720423936-lnUYpmeWyXhWtXZ2fKlJrmtTfO1YvKn"
access_token_secret ="LBMn727ycFTUV4rbo7iiNn9gdevyzetto5gsRUfWk3lEu"

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

a=0
while a<=2 :
    
    cmd="fswebcam -F 3 --fps 20 -r 800*600 /home/cs2017a123/Desktop/img.jpg"
    os.system(cmd)
    img="/home/cs2017a123/Desktop/img.jpg"
    print("pic taken")
    api.update_with_media(img,status="nice one")
    print("wait for 5 seconds")
    time.sleep(5)
    a+=1
    
    print("succes")
    
