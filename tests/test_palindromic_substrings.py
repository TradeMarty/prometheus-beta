import pytest
from src.palindromic_substrings import find_non_overlapping_palindromes

def test_basic_palindromes():
    """Test finding palindromes in a basic string."""
    result = find_non_overlapping_palindromes("abcba")
    assert set(result) == {"a", "b", "c", "bcb", "abcba"}

def test_multiple_palindromes():
    """Test a string with multiple different palindromes."""
    result = find_non_overlapping_palindromes("aabaa")
    assert set(result) == {"a", "aa", "aba", "aabaa"}

def test_empty_string():
    """Test behavior with an empty string."""
    result = find_non_overlapping_palindromes("")
    assert result == []

def test_single_char_string():
    """Test behavior with a single character string."""
    result = find_non_overlapping_palindromes("a")
    assert result == []

def test_no_palindromes():
    """Test a string with no palindromes longer than 1 character."""
    result = find_non_overlapping_palindromes("abcd")
    assert set(result) == {"a", "b", "c", "d"}

def test_lexicographic_order():
    """Test that palindromes are returned in lexicographic order."""
    result = find_non_overlapping_palindromes("racecar")
    assert result == sorted(result)

def test_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_non_overlapping_palindromes(123)

def test_complex_palindromes():
    """Test with a more complex string containing multiple palindromes."""
    result = find_non_overlapping_palindromes("abaxyzzyxf")
    expected = {"a", "b", "x", "y", "z", "aba", "xyz", "zyz", "xyzzyx"}
    assert set(result) == expected