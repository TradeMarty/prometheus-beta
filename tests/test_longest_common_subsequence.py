import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"

def test_identical_strings():
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_partially_common_subsequence():
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_empty_strings():
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_single_character_strings():
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("A", "B") == ""

def test_case_sensitivity():
    assert longest_common_subsequence("Hello", "hello") == ""

def test_type_error_non_string():
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", None)

def test_long_strings():
    str1 = "AGGTAB" * 100
    str2 = "GXTXAYB" * 100
    result = longest_common_subsequence(str1, str2)
    assert len(result) > 0
    assert all(char in str1 and char in str2 for char in result)