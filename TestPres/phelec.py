import pandas as pd
from googletrans import Translator
import time

def translate_tweets(input_csv_file, output_csv_file, source_lang='tl', target_lang='en'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv_file)

    # Extract the column containing the tweets
    tweets = df['Tweet']

    # Initialize the translator
    translator = Translator()

    # Translate the tweets and store them in a list
    translated_tweets = []
    rows_to_drop = []  # Store the indices of rows to be dropped

    for idx, tweet in enumerate(tweets):
        try:
            translated_tweet = translator.translate(tweet, src=source_lang, dest=target_lang).text
            translated_tweets.append(translated_tweet)
        except Exception as e:
            print(f"Translation error at row {idx + 1}: {e}")
            rows_to_drop.append(idx)  # Add the index to the list of rows to be dropped
            # Retry the translation after a delay
            time.sleep(5)
            continue

        # Add a delay to avoid rate limiting
        time.sleep(1)

    # Create a new DataFrame with the translated tweets
    translated_df = pd.DataFrame({'Translated_Tweet': translated_tweets})

    # Drop rows with errors from the original DataFrame
    df_cleaned = df.drop(rows_to_drop)

    # Write the translated DataFrame to a new CSV file
    translated_df.to_csv(output_csv_file, index=False)

# Example usage:
input_csv_file = 'TestPres/hashtags.csv'  # Replace with the path to your input CSV file
output_csv_file = 'TestPres/hashtagsTrans.csv'  # Replace with the desired output CSV file path

translate_tweets(input_csv_file, output_csv_file)
