import tweepy

class twitterClient:
    def __init__(self, keys):

        self.client = tweepy.Client(bearer_token=keys["TOKEN"])

    def searchRecentTweets(self, query, numberOfTweets, fields):
        tweets = self.client.search_recent_tweets(query=query,
                                                  tweet_fields=fields,
                                                  max_results=numberOfTweets)
        return tweets