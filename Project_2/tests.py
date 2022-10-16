import userSentiment
import json


with open('keys.json', 'r') as f:
    credentials = json.load(f)

sentiment = userSentiment.UserSentiment(credentials)

user, userData = sentiment.recentSentimentOfUser("MarkHamill", 100)

print(user)
print('magnitude: ' + str(userData.magnitude))

print('score: ' + str(userData.score))
