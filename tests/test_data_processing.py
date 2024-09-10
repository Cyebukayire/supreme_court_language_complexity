# tests/test_data_processing.py
import pytest
from process_data import counter

def test_count_sentences():
    text = "This is a sentence. This is another sentence."
    assert counter(text) == 2
