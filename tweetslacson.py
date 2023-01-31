import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "Panfilo Lacson until:2022-05-07 since:2022-02-08"

tweets = []

limit = 10000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

query2 = "Ping Lacson until:2022-05-07 since:2022-02-08"

for tweet in sntwitter.TwitterSearchScraper(query2).get_items():
    # print(vars(tweet))
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User','Tweet'])

print(df)
df.to_csv('placson.csv')