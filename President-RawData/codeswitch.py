import snscrape.modules.twitter as sntwitter
import pandas as pd
import nltk
import preprocessor as p
from googletrans import Translator
import time

translator = Translator()
timeout = 30

df=pd.read_csv('President-RawData/pmarcos.csv')

translated=[]

for elem in df['Tweet']:
    translated.append(translator.translate(elem).text)
    time.sleep(1)
df['translated'] = translated
df.to_csv('President-PreProcessed/pmarcosTrans.csv')