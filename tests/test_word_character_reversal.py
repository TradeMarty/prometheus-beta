import pytest
from src.word_character_reversal import reverse_words_and_characters

def test_basic_reversal():
    """Test basic word and character reversal"""
    assert reverse_words_and_characters("Hello World") == "dlroW olleH"
    assert reverse_words_and_characters("Python is awesome") == "emosewa si nohtyP"

def test_empty_string():
    """Test empty string input"""
    assert reverse_words_and_characters("") == ""

def test_single_word():
    """Test single word input"""
    assert reverse_words_and_characters("hello") == "olleh"

def test_multiple_spaces():
    """Test input with multiple spaces"""
    assert reverse_words_and_characters("  Hello   World  ") == "dlroW olleH"

def test_mixed_case():
    """Test mixed case input"""
    assert reverse_words_and_characters("Python Programming") == "gnimmargorP nohtyP"

def test_special_characters():
    """Test input with special characters"""
    assert reverse_words_and_characters("Hello, World!") == "!dlroW ,olleH"