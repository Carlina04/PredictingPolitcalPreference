import snscrape.modules.twitter as sntwitter
import pandas as pd
import nltk
import preprocessor as p
from googletrans import Translator
import time

#query = "#PHElections2022 until:2022-05-07 since:2022-02-08"

#tweets = []

#limit = 10000

#for tweet in sntwitter.TwitterSearchScraper(query).get_items():
#    # print(vars(tweet))
#    if len(tweets) == limit:
#        break
#    else:
#        tweets.append([tweet.date, tweet.user.username, tweet.content])

#df = pd.DataFrame(tweets, columns=['Date', 'User','Tweet'])

# ///raw gathered data file
#print(df)
#df.to_csv('VP/phelec.csv')

translator = Translator()
final=pd.read_csv('phelec.csv')
X=final['Tweet']

# stop words, stemming, taking out punctuation marks, converting to lowercase, removing links, emojis, & hashtags
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
    tw=translator.translate(X[i], src='tl', dest='en')
    tw=p.clean(X[i])
    tw=tw.lower().split()
    tw=[stemmer.stem(word) for word in tw if (word not in stop_words) and (word not in punct)]
    tw=' '.join(tw)
    tw=re.sub('[^a-zA-Z]',' ',tw)
    cleaned_data.append(tw)
    time.sleep(1)

df2 = pd.DataFrame(cleaned_data)

# pre-processed data file
print(df2)
df2.to_csv('test2.csv')
