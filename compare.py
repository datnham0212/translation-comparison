from difflib import SequenceMatcher
import pandas as pd
from nltk.translate.bleu_score import sentence_bleu

# Load both machine-translated and human-translated Vietnamese subtitles
machine_translations = pd.read_csv('translated_captions.csv')
human_translations = pd.read_csv('vietnamese_captions.csv')

# Define a function to calculate similarity ratio (Levenshtein-based)
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Define a function to calculate BLEU score
def bleu_score(reference, candidate):
    return sentence_bleu([reference.split()], candidate.split())

# Apply similarity comparison for each row
machine_translations['similarity'] = machine_translations.apply(
    lambda row: similarity(row['translated_vietnamese'], human_translations.loc[row.name, 'caption']),
    axis=1
)

# Apply BLEU score comparison
machine_translations['bleu_score'] = machine_translations.apply(
    lambda row: bleu_score(human_translations.loc[row.name, 'caption'], row['translated_vietnamese']),
    axis=1
)

# Save the result for review
machine_translations.to_csv('comparison_results.csv', index=False)
