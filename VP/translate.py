import snscrape.modules.twitter as sntwitter
import pandas as pd
import nltk
import preprocessor as p
from googletrans import Translator
import time

translator = Translator()

df=pd.read_csv('vppangilinan.csv')

translated=[]

for elem in df['Tweet']:
    translated.append(translator.translate(elem).text)
    time.sleep(1)
df['translated'] = translated
df.to_csv('pangilinanTrans.csv')
