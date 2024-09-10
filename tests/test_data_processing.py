# tests/test_data_processing.py
import pytest
from src.data_processing import count_sentences

def test_count_sentences():
    text = "This is a sentence. This is another sentence."
    assert count_sentences(text) == 2
