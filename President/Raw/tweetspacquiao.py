import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "Manny Pacquiao until:2022-05-07 since:2022-02-08"
query2 = "Manny Pacquiao until:2022-05-04 since:2022-04-26"
query3 = "Manny Pacquiao until:2022-04-25 since:2022-04-16"
query4 = "Manny Pacquiao until:2022-04-13 since:2022-04-02"
query5 = "Manny Pacquiao until:2022-04-01 since:2022-03-20"
query6 = "Manny Pacquiao until:2022-03-18 since:2022-03-10"
query7 = "Manny Pacquiao until:2022-03-08 since:2022-03-01"
query8 = "Manny Pacquiao until:2022-02-27 since:2022-02-21"
query9 = "Manny Pacquiao until:2022-02-22 since:2022-02-16"
query10 = "Manny Pacquiao until:2022-02-15 since:2022-02-08"

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
df.to_csv('ppacquiao.csv')