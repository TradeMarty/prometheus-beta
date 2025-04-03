import pytest
from src.multi_array_manipulator import multiArrayManipulator

def test_multiply_operation():
    # Test basic multiplication
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2}
    assert multiArrayManipulator(arr, manipulations) == [[2, 4], [6, 8]]

def test_add_operation():
    # Test basic addition
    arr = [[1, 2], [3, 4]]
    manipulations = {'add': 3}
    assert multiArrayManipulator(arr, manipulations) == [[4, 5], [6, 7]]

def test_transpose_operation():
    # Test array transposition
    arr = [[1, 2], [3, 4]]
    manipulations = {'transpose': True}
    assert multiArrayManipulator(arr, manipulations) == [[1, 3], [2, 4]]

def test_multiple_operations():
    # Test multiple operations in sequence
    arr = [[1, 2], [3, 4]]
    manipulations = {'multiply': 2, 'add': 1, 'transpose': True}
    assert multiArrayManipulator(arr, manipulations) == [[3, 7], [5, 9]]

def test_empty_array_error():
    # Test error for empty array
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        multiArrayManipulator([], {})

def test_invalid_input_type():
    # Test error for invalid input type
    with pytest.raises(TypeError, match="Input must be a 2D list of integers"):
        multiArrayManipulator("not a list", {})

def test_invalid_multiply_type():
    # Test error for invalid multiply value
    arr = [[1, 2], [3, 4]]
    with pytest.raises(TypeError, match="Multiply value must be a number"):
        multiArrayManipulator(arr, {'multiply': 'invalid'})

def test_invalid_add_type():
    # Test error for invalid add value
    arr = [[1, 2], [3, 4]]
    with pytest.raises(TypeError, match="Add value must be a number"):
        multiArrayManipulator(arr, {'add': 'invalid'})

def test_unsupported_operation():
    # Test error for unsupported operation
    arr = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Unsupported operation"):
        multiArrayManipulator(arr, {'unknown': True})