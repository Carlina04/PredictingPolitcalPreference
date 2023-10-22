import snscrape.modules.twitter as sntwitter
import pandas as pd
import nltk
import preprocessor as p

final=pd.read_csv('VP/phelecTranslated.csv')
X=final['Translated_Tweet']

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

df2 = pd.DataFrame(cleaned_data)

# pre-processed data file
print(df2)
df2.to_csv('VP/phelecPP.csv')
