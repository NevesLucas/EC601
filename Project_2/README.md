# Project 2

## Part 1: API exploration.

For this task I set up tweepy and botometer to query data from the twitter api 
and check if user accounts were bots.

Unfortunately, botometer requries evenated twitter api permissions, and so I was unable to set
up botometer at this time, though I did request access

Tweepy works well though, basic test was to query for tweets matching a certain keyword, 
and return the body if the tweet and its author ID.
`twitterTest.py` does a simple query for keywords and returns the located tweets and author IDs

Google NLP was simple to set up.
`NLPTest.py` exercises querying sentiment analysis using googleNLP for a simple hello world setup.

