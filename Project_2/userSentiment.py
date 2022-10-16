import twitterAPI
import NLP

class UserSentiment:

    def __init__(self, keys):
        self.twitter = twitterAPI.TwitterClient(keys)
        self.nlp = NLP.NLPClient()

    def recentSentimentOfUser(self,username,tweetCount):

        user, tweets = self.twitter.getRecentTweetsOfUser(username, tweetCount)
        return user, self.nlp.submitTweets(tweets)