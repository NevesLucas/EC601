import userSentiment
import json


with open('keys.json', 'r') as f:
    credentials = json.load(f)

sentiment = userSentiment.UserSentiment(credentials)

user, userData, score = sentiment.recentSentimentOfUser("MarkHamill", 100)

print(user)

print('score: ' + str(score.score))
print('magnitude: ' + str(score.magnitude))

userTopics = sentiment.topics(userData)

print(userTopics)
