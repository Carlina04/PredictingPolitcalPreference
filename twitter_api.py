import tweepy
import configparser
import pandas as pd

# read tokens from config file
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# get tweets from home and place inside csv
# public_tweets = api.home_timeline()

# columns = ['Time', 'User', 'Tweet']
# data = []
# for tweet in public_tweets:
#     data.append([tweet.created_at, tweet.user.screen_name, tweet.text])


# df = pd.DataFrame(data, columns=columns)
# print(df)

# df.to_csv('testtweets.csv')

# get tweets from specific user
# user = 'veritasium'
# limit = 300
# #only returns 200 so use tweep.Cursor() eg below

# #tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# for tweet in tweets :
#     print(tweet.full_text)

#get tweets with specific hashtags and keywords
#keywords can be any word, #hashtags, @username
# keywords = '#2022'
# limit = 300

# tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)

# for tweet in tweets :
#     print(tweet.full_text)

def generate_dates(start, end, n, seed=1, replace=False):
    dates = pd.date_range(start, end).to_series()
    return dates.sample(n, replace=replace, random_state=seed)
print(generate_dates('20220208', '20220531', 5, seed=1))

#Halalan2022, #phvote for training