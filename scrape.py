import requests
from bs4 import BeautifulSoup
import csv
import re

# URL of the transcript page
url = "https://transcripts.foreverdreaming.org/viewtopic.php?t=132883"

# Send a GET request to fetch the page content
response = requests.get(url)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting all text from the main transcript section
transcript_section = soup.find('div', class_='postbody')
transcript_lines = transcript_section.text.splitlines()

# Clean up the transcript lines (removing empty lines and stripping extra spaces)
transcript_lines = [line.strip() for line in transcript_lines if line.strip()]

# Function to clean each line by removing unwanted characters
def clean_line(line):
    # Remove hyphens and any other unwanted symbols, such as double quotes or excessive spaces
    line = re.sub(r'[-–—]', '', line)  # Remove hyphens, en-dashes, em-dashes
    line = re.sub(r'[^\w\s.,!?\'"]+', '', line)  # Remove non-word characters except punctuation
    return line.strip()

# Clean each line before processing
cleaned_lines = [clean_line(line) for line in transcript_lines]

# Group lines together that belong to the same sentence (ending with a period, exclamation mark, or question mark)
grouped_lines = []
current_block = ""

for line in cleaned_lines:
    if current_block:
        current_block += " " + line  # Append the current line to the ongoing block
    else:
        current_block = line

    # If the line ends with a sentence-ending punctuation, add it as a block
    if re.search(r'[.!?]$', line):
        grouped_lines.append(current_block)
        current_block = ""  # Reset for the next block

# Handle any remaining block that hasn't been added
if current_block:
    grouped_lines.append(current_block)

# Write the cleaned and grouped transcript into a CSV file
with open('forrest_gump_transcript_grouped.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Line Number', 'Transcript Line'])

    for i, line in enumerate(grouped_lines, 1):
        writer.writerow([i, line])

print("Grouped transcript has been saved to 'forrest_gump_transcript_grouped.csv'")
