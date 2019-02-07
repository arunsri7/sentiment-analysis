from textblob import TextBlob
a = input()
b = TextBlob(a)
print(b.sentiment.polarity)