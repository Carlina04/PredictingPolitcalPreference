import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "Kiko Pangilinan until:2022-05-07 since:2022-05-04"
query2 = "Kiko Pangilinan until:2022-05-01 since:2022-04-28"
query3 = "Kiko Pangilinan until:2022-04-20 since:2022-04-16"
query4 = "Kiko Pangilinan until:2022-04-13 since:2022-04-07"
query5 = "Kiko Pangilinan until:2022-04-04 since:2022-03-29"
query6 = "Kiko Pangilinan until:2022-03-25 since:2022-03-15"
query7 = "Kiko Pangilinan until:2022-03-08 since:2022-03-01"
query8 = "Kiko Pangilinan until:2022-02-27 since:2022-02-20"
query9 = "Kiko Pangilinan until:2022-02-15 since:2022-02-12"
query10 = "Kiko Pangilinan until:2022-02-10 since:2022-02-08"

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
df.to_csv('vppangilinan.csv')