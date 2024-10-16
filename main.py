import pandas as pd
from googletrans import Translator
from pyvi import ViTokenizer
from difflib import SequenceMatcher
from nltk.translate.bleu_score import sentence_bleu

# Initialize the translator
translator = Translator()

# Load your English captions CSV file
english_captions = pd.read_csv('forrest_gump_transcript_en.csv')
human_translations = pd.read_csv('forrest_gump_transcript_vn.csv')

# Check the columns for verification
print("English Captions Columns:", english_captions.columns)
print("Vietnamese Captions Columns:", human_translations.columns)

# Step 1: Translate English captions to Vietnamese
english_captions['translated_vietnamese'] = english_captions['Transcript Line'].apply(
    lambda x: translator.translate(x, src='en', dest='vi').text
)

# Step 2: Tokenize the machine-translated Vietnamese text
english_captions['tokenized_vietnamese'] = english_captions['translated_vietnamese'].apply(ViTokenizer.tokenize)

# Step 3: Tokenize the human-translated Vietnamese captions
human_translations['tokenized_caption'] = human_translations['Transcript Line'].apply(ViTokenizer.tokenize)

# Step 4: Define a function to calculate similarity ratio (Levenshtein-based)
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Step 5: Define a function to calculate BLEU score
def bleu_score(reference, candidate):
    return sentence_bleu([reference.split()], candidate.split())

# Step 6: Apply similarity and BLEU score comparisons between machine and human translations
english_captions['similarity'] = english_captions.apply(
    lambda row: similarity(row['tokenized_vietnamese'], human_translations.loc[row.name, 'tokenized_caption']),
    axis=1
)

english_captions['bleu_score'] = english_captions.apply(
    lambda row: bleu_score(human_translations.loc[row.name, 'tokenized_caption'], row['tokenized_vietnamese']),
    axis=1
)

# Step 7: Save the comparison results to a CSV file
english_captions.to_csv('pyvi_comparison_results.csv', index=False)

# Print some of the results for quick inspection
print(english_captions[['Line Number', 'Transcript Line', 'translated_vietnamese', 'tokenized_vietnamese', 'similarity', 'bleu_score']].head())
