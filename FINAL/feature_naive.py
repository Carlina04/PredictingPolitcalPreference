import nltk
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer 
import pandas as pd
import gensim 
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("VP-PreProcessed/dutertePP.csv")
no_neu = data[data["Sentiment"] != 'Neutral'] #only picking out tweets with either POSITIVE or NEGATIVE sentament

bow_vectorizer = CountVectorizer(max_df=0.90 ,min_df=2 , max_features=1000,stop_words='english')
bow = bow_vectorizer.fit_transform(no_neu['Cleaned'].values.astype('U')) # tokenize and build vocabulary
bow.shape

data=data.fillna(0) #replace all null values by 0

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(bow, no_neu['Sentiment'],test_size=0.2, random_state=69)
print("X_train_shape : ",X_train.shape)
print("X_test_shape : ",X_test.shape)
print("y_train_shape : ",y_train.shape)
print("y_test_shape : ",y_test.shape)

from sklearn.naive_bayes import MultinomialNB  # Naive Bayes Classifier

model_naive = MultinomialNB().fit(X_train, y_train) 
predicted_naive = model_naive.predict(X_test)

from sklearn.metrics import confusion_matrix

plt.figure(dpi=600)
mat = confusion_matrix(y_test, predicted_naive)
sns.heatmap(mat.T, annot=True, fmt='d', cbar=False)

plt.title('Confusion Matrix for Naive Bayes')
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.savefig("VP-Models/Naive_Bayes/Duterte_Matrix.png")
plt.show()

from sklearn.metrics import accuracy_score

score_naive = accuracy_score(predicted_naive, y_test)
print("Accuracy with Naive-bayes: ",score_naive)
