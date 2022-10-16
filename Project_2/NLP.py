import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.getcwd(), "GCloud.json")
from google.cloud import language_v1

class NLPClient:
    def __init__(self):
        self.client = language_v1.LanguageServiceClient()

    def submitGenericQuery(self, text):
        document = language_v1.Document(
            content=text, type_=language_v1.Document.Type.PLAIN_TEXT
        )
        sentiment = self.client.analyze_sentiment(request={"document": document}).document_sentiment
        return sentiment

    def tweetSentiment(self, tweets):
        data = tweets[0]
        agreggateTweets = '\n'.join(tweet.text for tweet in data.data)
        document = language_v1.Document(
            content=agreggateTweets, type_=language_v1.Document.Type.PLAIN_TEXT
        )
        OverallSentiment = self.client.analyze_sentiment(request={"document": document}).document_sentiment
        return OverallSentiment

    def tweetTopics(self, tweets):
        data = tweets[0]
        agreggateTweets = '\n'.join(tweet.text for tweet in data.data)
        document = language_v1.Document(
            content=agreggateTweets, type_=language_v1.Document.Type.PLAIN_TEXT
        )
        topics = self.client.classify_text(request={"document": document}).categories
        return topics

    def tweetEntities(self, tweets):
        data = tweets[0]
        agreggateTweets = '\n'.join(tweet.text for tweet in data.data)
        document = language_v1.Document(
            content=agreggateTweets, type_=language_v1.Document.Type.PLAIN_TEXT
        )
        entitySentiment = self.client.analyze_entity_sentiment(request={"document": document}).categories
        return entitySentiment
