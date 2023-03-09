import snscrape.modules.twitter as sntwitter
import pandas as pd
import nltk

query = "#PHElections2022 until:2022-05-07 since:2022-02-08"

tweets = []

limit = 10000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User','Tweet'])

# raw gathered data file
print(df)
df.to_csv('VP/phelec.csv')

final=pd.read_csv('VP/phelec.csv')
X=final['Tweet']

# stop words, stemming, taking out punctuation mark, converting to lowercase
from nltk.corpus import stopwords
nltk.download('stopwords')
import string
from nltk.stem import PorterStemmer

stop_words=stopwords.words('english')
punct=string.punctuation
stemmer=PorterStemmer()

import re
cleaned_data=[]
for i in range(len(X)):
    tw=re.sub('[^a-zA-Z]',' ',X.iloc[i])
    tw=tw.lower().split()
    tw=[stemmer.stem(word) for word in tw if (word not in stop_words) and (word not in punct)]
    tw=' '.join(tw)
    cleaned_data.append(tw)

df2 = pd.DataFrame(cleaned_data)

# pre-processed data file
print(df2)
df2.to_csv('VP/test.csv')
