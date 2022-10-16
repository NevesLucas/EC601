import tweepy

class TwitterClient:
    def __init__(self, keys):

        self.client = tweepy.Client(bearer_token=keys["TOKEN"])

    def searchRecentTweets(self, query, numberOfTweets, fields):
        tweets = self.client.search_recent_tweets(query=query,
                                                  tweet_fields=fields,
                                                  max_results=numberOfTweets)
        return tweets

    def getRecentTweetsOfUser(self, username, numberOfTweets, fields=['text']):
        user = self.client.get_user(username=username)
        tweets = []
        if numberOfTweets <= 100:
            tweets.append(self.client.get_users_tweets(id=user.data.id, tweet_fields=fields, max_results=numberOfTweets))
        else:
            for tweet in tweepy.Paginator(self.client.get_users_tweets, id=user.data.id,
                                          tweet_fields=fields, max_results=100).flatten(limit=numberOfTweets):
                tweets.append(tweet)

        return user, tweets
