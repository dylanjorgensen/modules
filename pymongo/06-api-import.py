# http://www.pythoncentral.io/introduction-to-tweepy-twitter-for-python/
# http://altons.github.io/python/2013/01/21/gentle-introduction-to-mongodb-using-pymongo/

from pymongo import MongoClient
client = MongoClient()
db = client.pymongo


doc = {"name":"Alberto","surname":"Negron","twitter":"@Altons"}
db.twitter.insert(doc)


import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = '2W9s0yWWHPGQrDCrq6CtJJzIv'
consumer_secret = 'PppKZd4iQrPX1DXNFPvxNtp9u2ZrjOtJcJkfXr2q7Hh9VqQpgQ'
access_token = '30415923-BYkqxqk61QozQYvKWzZY20xBnPI5WirFWuOEv4HjX'
access_token_secret = '71PNS9jGH3HZFDgUcoXTiOZ9tJoDHK9zu086kAC4egAMP'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

lookup ='podcast'
search = []
page = 1
maxPage = 3
while(page<=maxPage):
    tweets = api.search(lookup)
    for tweet in tweets:
        search.append(tweet)
    page = page + 1

# for x in search:
#     print x

# Let's how many tweets we got from the above search:
# print len(search)

# Not bad, let inspect the structure of the first object:
# print dir(search[0])

# loop through search and insert dictionary into mongoDB
for tweet in search:
    # Empty dictionary for storing tweet related data
    data ={}
    data['created_at'] = tweet.created_at
    data['geo'] = tweet.geo
    data['id'] = tweet.id
    data['source'] = tweet.source
    data['text'] = tweet.text
    data['retweet_count'] = tweet.retweet_count
    data['lang'] = tweet.lang

db.twitter.insert(data)



# # Creates the user object. The me() method returns the user whose authentication keys were used.
# user = api.me()
#
# print('Name: ' + user.name)
# print('Location: ' + user.location)
# print('Friends: ' + str(user.friends_count))




posts = db.twitter
print posts.count()
print posts.find().count()
print posts.find({"lang":"en"}).count()