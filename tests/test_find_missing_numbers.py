import pytest
from src.find_missing_numbers import find_missing_numbers

def test_find_missing_numbers_basic():
    """Test finding missing numbers in a basic scenario."""
    arr = [1, 2, 4, 6, 3, 7, 8]
    assert find_missing_numbers(arr) == [5]

def test_find_missing_numbers_no_missing():
    """Test when no numbers are missing."""
    arr = [1, 2, 3, 4, 5]
    assert find_missing_numbers(arr) == []

def test_find_missing_numbers_multiple_missing():
    """Test finding multiple missing numbers."""
    arr = [1, 3, 5, 7, 9]
    assert find_missing_numbers(arr) == [2, 4, 6, 8]

def test_find_missing_numbers_negative_numbers():
    """Test finding missing numbers with negative integers."""
    arr = [-3, -1, 0, 2, 4]
    assert find_missing_numbers(arr) == [-2, 1, 3]

def test_find_missing_numbers_single_element():
    """Test finding missing numbers with a single element."""
    arr = [5]
    assert find_missing_numbers(arr) == []

def test_find_missing_numbers_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_numbers([])

def test_find_missing_numbers_none_input_raises_error():
    """Test that None input raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be None"):
        find_missing_numbers(None)

def test_find_missing_numbers_non_integer_raises_error():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_missing_numbers([1, 2, '3', 4])

def test_find_missing_numbers_large_range():
    """Test finding missing numbers in a large range."""
    arr = list(range(1, 100, 2))  # Odd numbers from 1 to 99
    expected_missing = list(range(2, 100, 2))  # Even numbers from 2 to 98
    assert find_missing_numbers(arr) == expected_missing