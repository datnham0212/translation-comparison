import pandas as pd
from nltk.stem import WordNetLemmatizer
from underthesea import lemmatize
from difflib import SequenceMatcher

# Initialize English lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a function for English lemmatization
def lemmatize_english(text):
    return " ".join([lemmatizer.lemmatize(word, pos='v') for word in text.split()])

# Define a function for Vietnamese lemmatization
def lemmatize_vietnamese(text):
    return " ".join(lemmatize(text))

# Load the data
machine_translations = pd.read_csv('translated_captions.csv')
human_translations = pd.read_csv('vietnamese_captions.csv')

# Lemmatize both machine-translated and human-translated captions
machine_translations['lemmatized_vietnamese'] = machine_translations['translated_vietnamese'].apply(lemmatize_vietnamese)
human_translations['lemmatized_caption'] = human_translations['caption'].apply(lemmatize_vietnamese)

# Calculate similarity based on lemmatized texts
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Apply similarity comparison
machine_translations['similarity'] = machine_translations.apply(
    lambda row: similarity(row['lemmatized_vietnamese'], human_translations.loc[row.name, 'lemmatized_caption']),
    axis=1
)

# Save results for review
machine_translations.to_csv('lemmatized_comparison_results.csv', index=False)
