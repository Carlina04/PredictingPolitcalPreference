import pandas as pd
from googletrans import Translator

def translate_tweets(input_csv_file, output_csv_file, source_lang='tl', target_lang='en'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv_file)

    # Extract the column containing the tweets
    tweets = df['Tweet']

    # Initialize the translator
    translator = Translator()

    # Translate the tweets and store them in a list
    translated_tweets = []

    for tweet in tweets:
        translated_tweet = translator.translate(tweet, src=source_lang, dest=target_lang).text
        translated_tweets.append(translated_tweet)

    # Create a new DataFrame with the translated tweets
    translated_df = pd.DataFrame({'Translated_Tweet': translated_tweets})

    # Write the translated DataFrame to a new CSV file
    translated_df.to_csv(output_csv_file, index=False)

# Example usage:
input_csv_file = 'vpduterte.csv'  # Replace with the path to your input CSV file
output_csv_file = 'duterteTranslated.csv'  # Replace with the desired output CSV file path

translate_tweets(input_csv_file, output_csv_file)
try:
    translated_text = translator.translate(text_to_translate, src=source_lang, dest=target_lang).text
except Exception as e:
    print(f"An error occurred: {e}")
    translated_text = "Translation not available"