import pandas as pd
from googletrans import Translator

# Load your English captions CSV file
english_captions = pd.read_csv('english_captions.csv')

# Initialize the translator
translator = Translator()

# Translate the 'caption' column from English to Vietnamese
english_captions['translated_vietnamese'] = english_captions['caption'].apply(lambda x: translator.translate(x, src='en', dest='vi').text)

# Save the translated captions to a new CSV file
english_captions.to_csv('translated_captions.csv', index=False)
