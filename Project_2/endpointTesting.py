#import Botometer
import twitterAPI
import json

with open('keys.json', 'r') as f:
    credentials = json.load(f)

twitter = twitterAPI.twitterClient(credentials)
test = twitter.getTweetsByHashtag('covid', '2022-10--01', 1)
print(test)
#botDetect = Botometer.Botmeter(credentials)

