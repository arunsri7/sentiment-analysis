
import sys,tweepy,csv,re
from textblob import TextBlob   




consumerKey = 'qrsbHJP4D0YiUlcvyJICE0mON'
consumerSecret = '54ImsKFqQf83Cvdjcvr0qVbx6Xn9zFM8c5cIH879vcp3BmnU9b'
accessToken = '224946576-OxRFcJylUuP2O38q5v1cL1FtQ89AzdTaHxlpXkse'
accessTokenSecret = 'WrwvygvSRePFHTBJEsUTIzDn9bigG3G1TthIWxV9pYZKd'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# input for term to be searched and how many tweets to search
searchTerm = input("Enter HashTag : ")
NoOfTerms = int(input("Enter the number of tweets to search: "))
# searching for tweets
tweets = tweepy.Cursor(api.search, q=searchTerm).items(NoOfTerms)

polarity = 0
positive = 0
negative = 0
neutral = 0
for tweet in tweets:
    print(tweet.text)
