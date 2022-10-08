#import Botometer
import twitterAPI
import json

with open('keys.json', 'r') as f:
    credentials = json.load(f)

twitter = twitterAPI.twitterClient(credentials)
test = twitter.searchRecentTweets('covid', 10, "text,author_id")
print(test)
#botDetect = Botometer.Botmeter(credentials) # needs v1 credentials

