import pandas as pd
import nltk
from src.llm_processing import process_text_with_llm

nltk.download('punkt')  # Required for sentence tokenization

def count_sentences(text):
    # Tokenize text into sentences
    sentences = nltk.sent_tokenize(text)
    return len(sentences)