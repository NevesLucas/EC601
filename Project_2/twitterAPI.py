import tweepy

class twitterClient:
    def __init__(self, keys):

        self.client = tweepy.Client(bearer_token=keys["TOKEN"])

    def getTweetsByHashtag(self, tagList, daterange, numberOfTweets):
        tweets = tweepy.Cursor(self.client.search_recent_tweets,
                               tagList, lang="en",
                               since_id=daterange,
                               tweet_mode='extended').items(numberOfTweets)
        return tweets
