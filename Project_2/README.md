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

## Part 2: Simple Twitter app

-- The purpose of this twitter library is to analyze a users tweets to determine their overall sentiment.
are they a negative poster? are they always positive? do they focus on a single topic or discuss many different ones?

-- NOTE: the original idea was to analyze users for Bot behavior and if they are likely to be a bot, determine what they
are attempting to promote/suppress, essentially determine the bots agenda. 
Due to inability to leverage botometer with the V2 api, instead this library will focus on simply getting
a users overall sentiment and topic of interest.

### User Stories:

1. As a User I want to give a username to analyze
2. As a User I want to select the number of tweets to analyze
3. As a user I want to receive aen aggregate sentiment score over the window provided

### Library usage

The main wrapper class for this tool is `userSentiment.py` which combines tweepy and NLP apis to get a user sentiment score for their past N tweets.

A simple test case exercising this is in `tests.py`

Currently no real error checking occurs, though the main failure case would be exceeding API usage limits.







`