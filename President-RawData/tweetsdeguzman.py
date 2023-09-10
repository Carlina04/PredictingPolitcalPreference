import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "Ka Leody until:2022-05-08 since:2022-05-01"
query2 = "Ka Leody until:2022-04-30 since:2022-04-20"
query3 = "Ka Leody until:2022-04-19 since:2022-04-10"
query4 = "Ka Leody until:2022-04-03 since:2022-03-27"
query5 = "Ka Leody until:2022-03-26 since:2022-03-19"
query6 = "Ka Leody until:2022-03-18 since:2022-03-10"
query7 = "Ka Leody until:2022-03-08 since:2022-03-02"
query8 = "Ka Leody until:2022-03-01 since:2022-02-24"
query9 = "Ka Leody until:2022-02-23 since:2022-02-16"
query10 = "Ka Leody until:2022-02-15 since:2022-02-08"

tweets = []
limit = 10000

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content]) 

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query2).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content]) 

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query3).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query4).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query5).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query6).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query7).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query8).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query9).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query10).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User','Tweet'])

print(df)
df.to_csv('pdeguzman.csv')