import snscrape.modules.twitter as sntwitter
import pandas as pd
import nltk
import preprocessor as p
import time

data = pd.read_csv('Testing/VPs/duterteLabel.csv')
data = data.dropna()
X=data['translated']

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
    tw=p.clean(X[i])
    tw=tw.lower().split()
    tw=[stemmer.stem(word) for word in tw if (word not in stop_words) and (word not in punct)]
    tw=' '.join(tw)
    tw=re.sub('[^a-zA-Z]',' ',tw)
    cleaned_data.append(tw)
    time.sleep(1)

data["Cleaned"] = cleaned_data

# pre-processed data file
print(data)
data.to_csv('VP-PreProcessed/dutertePP.csv')
