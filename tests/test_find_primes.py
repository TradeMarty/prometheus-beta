import pytest
from src.find_primes import find_primes_below_n

def test_find_primes_below_n_standard_cases():
    """Test standard cases for prime number generation."""
    assert find_primes_below_n(10) == [2, 3, 5, 7]
    assert find_primes_below_n(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert find_primes_below_n(2) == []

def test_find_primes_below_n_edge_cases():
    """Test edge cases and boundary conditions."""
    assert find_primes_below_n(1) == []
    assert find_primes_below_n(0) == []
    assert find_primes_below_n(-5) == []

def test_find_primes_below_n_large_number():
    """Test with a larger number to ensure performance."""
    primes_100 = find_primes_below_n(100)
    assert len(primes_100) == 25
    assert primes_100[-1] == 97

def test_find_primes_below_n_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        find_primes_below_n("not a number")
    
    with pytest.raises(TypeError):
        find_primes_below_n(3.14)
    
    with pytest.raises(TypeError):
        find_primes_below_n(None)