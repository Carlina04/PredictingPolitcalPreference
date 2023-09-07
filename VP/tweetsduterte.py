import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "Sara Duterte until:2022-05-07 since:2022-04-01"
query2 = "Sara Duterte until:2022-03-31 since:2022-02-08"

tweets = []
limit = 10000

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()): 
    if i>5000: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content]) 

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query2).get_items()): 
    if i>5000: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content]) 

df = pd.DataFrame(tweets, columns=['Date', 'User','Tweet'])

print(df)
df.to_csv('vpduterte.csv')