import nltk
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("FINAL/ph_elections.csv")

# Filter out Neutral sentiment
no_neu = data[data["Sentiment"] != 'Neutral']

# Vectorization
bow_vectorizer = CountVectorizer(max_df=0.90, min_df=2, max_features=1000, stop_words='english')
bow = bow_vectorizer.fit_transform(no_neu['Cleaned'].values.astype('U'))

# Data Splitting
X_train, X_test, y_train, y_test = train_test_split(bow, no_neu['Sentiment'], test_size=0.2, random_state=69)
print("X_train_shape : ",X_train.shape)
print("X_test_shape : ",X_test.shape)
print("y_train_shape : ",y_train.shape)
print("y_test_shape : ",y_test.shape)

# Model Training (using Logistic Regression)
model_logistic = LogisticRegression()
model_logistic.fit(X_train, y_train)

# Model Prediction
predicted_logistic = model_logistic.predict(X_test)

# Evaluation
mat = confusion_matrix(y_test, predicted_logistic)
sns.heatmap(mat.T, annot=True, fmt='d', cbar=False)
plt.title('PH Elections Confusion Matrix for Logistic Regression')
plt.xlabel('True label')
plt.ylabel('Predicted label')
plt.savefig("FINAL/PH_Elections_Matrix.png")
plt.show()

score_logistic = accuracy_score(predicted_logistic, y_test)
print("Accuracy with Logistic Regression: ", score_logistic)
