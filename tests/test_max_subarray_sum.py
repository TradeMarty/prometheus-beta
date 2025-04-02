import pytest
from src.max_subarray_sum import max_subarray_sum

def test_standard_case():
    """Test with a standard list and k value"""
    assert max_subarray_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39

def test_k_equals_list_length():
    """Test when k is equal to list length"""
    assert max_subarray_sum([1, 2, 3, 4, 5], 5) == 15

def test_k_larger_than_list():
    """Test when k is larger than list length"""
    assert max_subarray_sum([1, 2, 3], 5) == []

def test_empty_list():
    """Test with an empty list"""
    assert max_subarray_sum([], 3) == []

def test_k_zero():
    """Test when k is zero"""
    assert max_subarray_sum([1, 2, 3, 4], 0) == []

def test_negative_numbers():
    """Test with a list containing negative numbers"""
    assert max_subarray_sum([-1, -2, 3, 4, -5, 6, 7], 3) == 8

def test_type_error_non_list():
    """Test type error when input is not a list"""
    with pytest.raises(TypeError):
        max_subarray_sum(123, 3)

def test_type_error_non_integer_k():
    """Test type error when k is not an integer"""
    with pytest.raises(TypeError):
        max_subarray_sum([1, 2, 3], '3')

def test_negative_k():
    """Test value error when k is negative"""
    with pytest.raises(ValueError):
        max_subarray_sum([1, 2, 3], -1)

def test_single_element_list():
    """Test with a single element list"""
    assert max_subarray_sum([5], 1) == 5