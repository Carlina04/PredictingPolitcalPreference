import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")
import pandas as pd
data = pd.read_csv("President-Unlabelled/probredoTrans.csv")
data = data.dropna()
#print(data.head())

sentiments = SentimentIntensityAnalyzer()
data["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["Translated_Tweet"]]
data["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["Translated_Tweet"]]
data["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data["Translated_Tweet"]]
data['Compound'] = [sentiments.polarity_scores(i)["compound"] for i in data["Translated_Tweet"]]
data.head()
#print(data.head())

score = data["Compound"].values
sentiment = []
for i in score:
    if i >= 0.05 :
        sentiment.append('Positive')
    elif i <= -0.05 :
        sentiment.append('Negative')
    else:
        sentiment.append('Neutral')
data["Sentiment"] = sentiment
data.head()
print(data.head())

print(data["Sentiment"].value_counts())

data.to_csv("P-Labelled/robredoLabel.csv")