import twitterAPI
import NLP

class UserSentiment:

    def __init__(self, keys):
        self.twitter = twitterAPI.TwitterClient(keys)
        self.nlp = NLP.NLPClient()

    def recentSentimentOfUser(self, username, tweetCount):
        user, tweets = self.twitter.getRecentTweetsOfUser(username, tweetCount)
        return user, tweets, self.nlp.tweetSentiment(tweets)

    def gatherTweets(self, username,count):
        return self.twitter.getRecentTweetsOfUser(username, count)

    def sentiment(self, data):
        return self.nlp.tweetSentiment(data)

    def topics(self, data):
        return self.nlp.tweetTopics(data)

    def entities(self, data):
        return self.nlp.tweetEntities(data)
