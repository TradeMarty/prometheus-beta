import pytest
from src.palindrome_validator import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome cases"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True

def test_phrase_palindromes():
    """Test palindrome phrases with spaces and punctuation"""
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive():
    """Test that palindrome checking is case-insensitive"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaCeCaR") == True

def test_non_palindromes():
    """Test strings that are not palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_empty_and_whitespace():
    """Test empty string and whitespace-only inputs"""
    assert is_palindrome("") == True
    assert is_palindrome("   ") == True

def test_numeric_palindromes():
    """Test numeric palindromes"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_mixed_characters():
    """Test palindromes with mixed alphanumeric characters"""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b2c22c2b1a") == True
    assert is_palindrome("A1b2c3") == False