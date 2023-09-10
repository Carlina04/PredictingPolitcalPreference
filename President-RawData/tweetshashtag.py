import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "#Halalan2022 until:2022-05-07 since:2022-05-04"
query2 = "#Halalan2022 until:2022-05-01 since:2022-04-28"
query3 = "#Halalan2022 until:2022-04-20 since:2022-04-16"
query4 = "#Halalan2022 until:2022-04-13 since:2022-04-07"
query5 = "#Halalan2022 until:2022-04-04 since:2022-03-29"
query6 = "#Halalan2022 until:2022-03-25 since:2022-03-15"
query7 = "#Halalan2022 until:2022-03-08 since:2022-03-01"
query8 = "#Halalan2022 until:2022-02-27 since:2022-02-20"
query9 = "#Halalan2022 until:2022-02-15 since:2022-02-12"
query10 = "#Halalan2022 until:2022-02-10 since:2022-02-08"

query11 = "#phvote until:2022-02-10 since:2022-02-08"
query12 = "#phvote until:2022-05-01 since:2022-04-28"
query13 = "#phvote until:2022-04-20 since:2022-04-16"
query14 = "#phvote until:2022-04-13 since:2022-04-07"
query15 = "#phvote until:2022-04-04 since:2022-03-29"
query16 = "#phvote until:2022-03-25 since:2022-03-15"
query17 = "#phvote until:2022-03-08 since:2022-03-01"
query18 = "#phvote until:2022-02-27 since:2022-02-20"
query19 = "#phvote until:2022-02-15 since:2022-02-12"
query20 = "#phvote until:2022-02-10 since:2022-02-08"

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


for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query11).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query12).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query13).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])
    
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query14).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query15).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])
    
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query16).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query17).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])
    
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query18).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])
    
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query19).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])
    
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query20).get_items()): 
    if i>999: 
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])
    
df = pd.DataFrame(tweets, columns=['Date', 'User','Tweet'])

print(df)
df.to_csv('hashtags.csv')