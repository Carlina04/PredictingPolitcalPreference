import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("FINAL/ph_elections.csv")

# Filter out Neutral sentiment
no_neu = data[data["Sentiment"] != 'Neutral']

# Vectorization (using TF-IDF)
tfidf_vectorizer = TfidfVectorizer(max_df=0.90, min_df=2, max_features=1000, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(no_neu['Cleaned'].values.astype('U'))

# Data Splitting
X_train, X_test, y_train, y_test = train_test_split(tfidf, no_neu['Sentiment'], test_size=0.2, random_state=69)
print("X_train_shape : ",X_train.shape)
print("X_test_shape : ",X_test.shape)
print("y_train_shape : ",y_train.shape)
print("y_test_shape : ",y_test.shape)

# Model Training (using Support Vector Machine)
model_svm = SVC(kernel='linear', C=1.0, random_state=69)
model_svm.fit(X_train, y_train)

# Model Prediction
predicted_svm = model_svm.predict(X_test)

# Evaluation
mat = confusion_matrix(y_test, predicted_svm)
sns.heatmap(mat.T, annot=True, fmt='d', cbar=False)
plt.title('PH Election Matrix for SVM')
plt.xlabel('True label')
plt.ylabel('Predicted label')
plt.show()
plt.savefig("FINAL/SVM_PH_ELEC.png")

score_svm = accuracy_score(predicted_svm, y_test)
print("Accuracy with Support Vector Machine: ", score_svm)
