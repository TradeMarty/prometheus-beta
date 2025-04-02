import pytest
from src.longest_common_subsequence import longest_common_subsequence_length

def test_basic_subsequence():
    """Test a basic common subsequence"""
    assert longest_common_subsequence_length("ABCDGH", "AEDFHR") == 3

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence_length("ABCDEF", "ABCDEF") == 6

def test_no_common_subsequence():
    """Test when there's no common subsequence"""
    assert longest_common_subsequence_length("XYZ", "ABC") == 0

def test_empty_strings():
    """Test with empty strings"""
    assert longest_common_subsequence_length("", "ABC") == 0
    assert longest_common_subsequence_length("", "") == 0

def test_partial_match():
    """Test a partial match"""
    assert longest_common_subsequence_length("AGGTAB", "GXTXAYB") == 4

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence_length(123, "ABC")
    
    with pytest.raises(TypeError):
        longest_common_subsequence_length("ABC", None)

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence_length("abc", "ABC") == 0

def test_longer_strings():
    """Test with longer, more complex strings"""
    test_str1 = "ABCBDAB"
    test_str2 = "BDCABA"
    assert longest_common_subsequence_length(test_str1, test_str2) == 4