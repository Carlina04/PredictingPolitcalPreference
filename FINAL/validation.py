import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score

# Function to perform 10-fold cross-validation and return results
def perform_cross_validation(data_file, output_folder):
    # Load your data
    data = pd.read_csv(data_file)
    
    data.fillna('', inplace=True)

    # Assuming your data has 'text' as the column containing the tweet text and 'label' as the sentiment label
    X = data['Cleaned']
    y = data['Sentiment']

    # Initialize TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer(max_df=0.90, min_df=2, max_features=1000, stop_words='english')
    
    # Initialize models
    models = {
        'Naive Bayes': MultinomialNB(),
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'SVM': SVC(kernel='linear', C=1.0)
    }

    # Create dictionaries to store results for each model
    precision_results = {model_name: [] for model_name in models}
    recall_results = {model_name: [] for model_name in models}
    f1_results = {model_name: [] for model_name in models}

    # Perform 10-fold cross-validation
    kf = StratifiedKFold(n_splits=10, shuffle=True, random_state=69)

    for train_index, test_index in kf.split(X, y):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
        X_test_tfidf = tfidf_vectorizer.transform(X_test)

        for model_name, model in models.items():
            model.fit(X_train_tfidf, y_train)
            y_pred = model.predict(X_test_tfidf)

            # Get the unique class labels in your dataset
            unique_labels = set(y_test)

            # Initialize lists to store metrics for each class
            precision_per_class = []
            recall_per_class = []
            f1_per_class = []

            for label in unique_labels:
                # Compute metrics for the current class
                precision = precision_score(y_test, y_pred, labels=[label], average='micro')
                recall = recall_score(y_test, y_pred, labels=[label], average='micro')
                f1 = f1_score(y_test, y_pred, labels=[label], average='micro')

                # Store metrics for the current class
                precision_per_class.append(precision)
                recall_per_class.append(recall)
                f1_per_class.append(f1)

            # Store the results for the current fold
            precision_results[model_name].append(precision_per_class)
            recall_results[model_name].append(recall_per_class)
            f1_results[model_name].append(f1_per_class)

    # Calculate and print the average performance for each model
    for model_name in models:
        avg_precision = [sum(metrics) / len(metrics) for metrics in zip(*precision_results[model_name])]
        avg_recall = [sum(metrics) / len(metrics) for metrics in zip(*recall_results[model_name])]
        avg_f1 = [sum(metrics) / len(metrics) for metrics in zip(*f1_results[model_name])]

        print(f'{model_name} Results:')
        for label, precision, recall, f1 in zip(unique_labels, avg_precision, avg_recall, avg_f1):
            print(f'Class: {label}')
            print(f'  Average Precision: {precision:.2f}')
            print(f'  Average Recall: {recall:.2f}')
            print(f'  Average F1-Score: {f1:.2f}')
        print()

# Specify the dataset file and output folder
data_file = 'FINAL/ph_elections.csv'
output_folder = 'output'

# Create the output folder if it doesn't exist
import os
os.makedirs(output_folder, exist_ok=True)

# Perform cross-validation and save the results
perform_cross_validation(data_file, output_folder)
