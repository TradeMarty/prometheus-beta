import pytest
from src.weighted_sum import calculate_weighted_sum

def test_basic_weighted_sum():
    """Test a basic scenario with integer values."""
    numbers = [1, 2, 3]
    weights = [0.5, 1, 1.5]
    assert calculate_weighted_sum(numbers, weights) == 1*0.5 + 2*1 + 3*1.5

def test_float_values():
    """Test weighted sum with float values."""
    numbers = [1.5, 2.5, 3.5]
    weights = [0.5, 1.0, 1.5]
    assert calculate_weighted_sum(numbers, weights) == 1.5*0.5 + 2.5*1.0 + 3.5*1.5

def test_zero_weight():
    """Test scenario with zero weights."""
    numbers = [10, 20, 30]
    weights = [0, 0, 0]
    assert calculate_weighted_sum(numbers, weights) == 0

def test_mismatched_lengths():
    """Test that an error is raised when lists have different lengths."""
    with pytest.raises(ValueError, match="The length of numbers and weights must be the same"):
        calculate_weighted_sum([1, 2], [1, 2, 3])

def test_empty_lists():
    """Test that an error is raised with empty lists."""
    with pytest.raises(ValueError, match="Both numbers and weights lists must be non-empty"):
        calculate_weighted_sum([], [])

def test_non_numeric_input():
    """Test that an error is raised with non-numeric inputs."""
    with pytest.raises(ValueError, match="All numbers and weights must be numeric"):
        calculate_weighted_sum([1, 'a'], [1, 2])
    with pytest.raises(ValueError, match="All numbers and weights must be numeric"):
        calculate_weighted_sum([1, 2], [1, 'b'])