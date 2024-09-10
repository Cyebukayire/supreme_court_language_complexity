import pandas as pd
import nltk
import nltk.data

# Download tokenizer
try:
    # Check if 'punkt' is already downloaded
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('tokenizers/punkt_tab')

except LookupError:
    # If not found, download it
    nltk.download('punkt')
    nltk.download('punkt_tab')

def count_sentences(text):
    # Tokenize text into sentences
    sentences = nltk.sent_tokenize(text)
    return len(sentences)