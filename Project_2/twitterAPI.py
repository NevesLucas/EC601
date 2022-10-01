import tweepy
import json


class twitterClient:
    def __init__(self):
        with open('twitterkeys.json', 'r') as f:
            credentials = json.load(f)
        self.client = tweepy.Client(bearer_token=credentials["TOKEN"])
