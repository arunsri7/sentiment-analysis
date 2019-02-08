import sys,tweepy,csv,re
from textblob import TextBlob   

class HashtagAnalyzer():
    def __init__(self, hashtag, noOfTweets):
        self.hashtag = hashtag
        self.noOfTweets = noOfTweets

        # initialize tweepy
        consumerKey = 'qrsbHJP4D0YiUlcvyJICE0mON'
        consumerSecret = '54ImsKFqQf83Cvdjcvr0qVbx6Xn9zFM8c5cIH879vcp3BmnU9b'
        accessToken = '224946576-OxRFcJylUuP2O38q5v1cL1FtQ89AzdTaHxlpXkse'
        accessTokenSecret = 'WrwvygvSRePFHTBJEsUTIzDn9bigG3G1TthIWxV9pYZKd'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        self.api = tweepy.API(auth)

    def analyse(self):
        tweets = tweepy.Cursor(self.api.search, q=self.hashtag).items(self.noOfTweets)
        for tweet in tweets:
            print(tweet.text)
        # continue


if __name__ == "__main__":
    # input for term to be searched and how many tweets to search
    searchTerm = input("Enter HashTag : ")
    noOfTerms = int(input("Enter the number of tweets to search: "))

    polarity = 0
    positive = 0
    negative = 0
    neutral = 0

    ha = HashtagAnalyzer(searchTerm, noOfTerms)
    ha.analyse()