import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from textblob import TextBlob
from wordcloud import WordCloud
import plotly.graph_objects as go
import plotly.express as px

from nltk.tokenize import TweetTokenizer
import cleantext
Robredo_reviews = pd.read_csv('probredo.csv', encoding = 'utf-8')
Marcos_reviews = pd.read_csv('pmarcos.csv', encoding = 'utf-8')


robredo_clean=Robredo_reviews.drop_duplicates(subset=['text'],keep='last').copy()

# df_nd.to_csv('df_noduplicates.csv',header=False)