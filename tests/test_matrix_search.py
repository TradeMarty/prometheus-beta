import pytest
import sys
import os

# Ensure src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from matrix_search import search_matrix

def test_search_matrix_basic():
    """Test basic matrix search scenarios"""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False
    assert search_matrix(matrix, 60) == True
    assert search_matrix(matrix, 1) == True

def test_search_matrix_edge_cases():
    """Test edge cases like single row, single column, and boundary values"""
    # Single row matrix
    single_row = [[1, 3, 5]]
    assert search_matrix(single_row, 3) == True
    assert search_matrix(single_row, 4) == False
    
    # Single column matrix
    single_col = [[1], [3], [5]]
    assert search_matrix(single_col, 3) == True
    assert search_matrix(single_col, 4) == False

def test_search_matrix_error_handling():
    """Test error handling for invalid inputs"""
    # Empty matrix
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        search_matrix([], 5)
    
    # Invalid matrix types
    with pytest.raises(TypeError, match="Matrix must be a 2D list"):
        search_matrix("not a matrix", 5)
    
    with pytest.raises(TypeError, match="Matrix must contain only integers"):
        search_matrix([[1, 2], ['a', 'b']], 5)
    
    # Invalid target type
    with pytest.raises(TypeError, match="Target must be an integer"):
        search_matrix([[1, 2], [3, 4]], "5")

def test_search_matrix_large():
    """Test search in a larger matrix"""
    large_matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert search_matrix(large_matrix, 5) == True
    assert search_matrix(large_matrix, 20) == False
    assert search_matrix(large_matrix, 30) == True
    assert search_matrix(large_matrix, 1) == True