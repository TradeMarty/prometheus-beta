import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_all_digits():
    """Test a string containing only digits."""
    assert sum_of_digits('1234567890') == 45

def test_sum_of_digits_mixed_string():
    """Test a string with letters and digits."""
    assert sum_of_digits('abc123') == 6

def test_sum_of_digits_no_digits():
    """Test a string with no digits."""
    assert sum_of_digits('no digits') == 0

def test_sum_of_digits_empty_string():
    """Test an empty string."""
    assert sum_of_digits('') == 0

def test_sum_of_digits_leading_zeros():
    """Test a string with leading zeros."""
    assert sum_of_digits('00123') == 6

def test_sum_of_digits_special_characters():
    """Test a string with special characters."""
    assert sum_of_digits('!@#$123%^&*()') == 6

def test_sum_of_digits_multiple_digits_sequence():
    """Test a string with multiple digit sequences."""
    assert sum_of_digits('a1b2c3d4e5') == 15