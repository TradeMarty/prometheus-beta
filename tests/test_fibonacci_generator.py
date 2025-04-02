import pytest
from src.fibonacci_generator import fibonacci_generator

def test_fibonacci_generator_zero():
    """Test generating 0 Fibonacci numbers"""
    assert fibonacci_generator(0) == []

def test_fibonacci_generator_one():
    """Test generating 1 Fibonacci number"""
    assert fibonacci_generator(1) == [0]

def test_fibonacci_generator_two():
    """Test generating 2 Fibonacci numbers"""
    assert fibonacci_generator(2) == [0, 1]

def test_fibonacci_generator_multiple():
    """Test generating multiple Fibonacci numbers"""
    assert fibonacci_generator(5) == [0, 1, 1, 2, 3]
    assert fibonacci_generator(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_generator_negative_input():
    """Test that negative input raises ValueError"""
    with pytest.raises(ValueError, match="Number of Fibonacci numbers must be non-negative"):
        fibonacci_generator(-1)

def test_fibonacci_generator_non_integer_input():
    """Test that non-integer input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator(None)