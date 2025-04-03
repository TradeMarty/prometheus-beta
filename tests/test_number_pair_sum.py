import os
import pytest
from src.number_pair_sum import sum_pairs_with_difference_nine

def test_basic_sum_pairs():
    # Create a test file with numbers
    test_file_path = 'tests/test_numbers.txt'
    with open(test_file_path, 'w') as f:
        f.write("1 10 2 11 3 12 4 13")
    
    # Expected: (1,10), (2,11), (3,12), (4,13) are pairs with difference 9
    # Sum would be: (1+10) + (2+11) + (3+12) + (4+13) = 11 + 13 + 15 + 17 = 56
    assert sum_pairs_with_difference_nine(test_file_path) == 56
    
    # Clean up test file
    os.remove(test_file_path)

def test_empty_file():
    # Create an empty file
    test_file_path = 'tests/empty_test.txt'
    with open(test_file_path, 'w') as f:
        f.write("")
    
    # Should return 0 for an empty file
    assert sum_pairs_with_difference_nine(test_file_path) == 0
    
    # Clean up test file
    os.remove(test_file_path)

def test_file_not_found():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        sum_pairs_with_difference_nine('tests/nonexistent_file.txt')

def test_invalid_input():
    # Create a file with non-numeric content
    test_file_path = 'tests/invalid_input.txt'
    with open(test_file_path, 'w') as f:
        f.write("1 2 three 4")
    
    # Should raise ValueError
    with pytest.raises(ValueError):
        sum_pairs_with_difference_nine(test_file_path)
    
    # Clean up test file
    os.remove(test_file_path)

def test_no_pairs():
    # Create a file with no pairs having difference 9
    test_file_path = 'tests/no_pairs.txt'
    with open(test_file_path, 'w') as f:
        f.write("1 2 3 4 5")
    
    # Should return 0
    assert sum_pairs_with_difference_nine(test_file_path) == 0
    
    # Clean up test file
    os.remove(test_file_path)

def test_duplicate_pairs():
    # Create a file with duplicate pairs
    test_file_path = 'tests/duplicate_pairs.txt'
    with open(test_file_path, 'w') as f:
        f.write("1 10 1 10 2 11 2 11")
    
    # Expected: (1,10), (2,11) - should only count once
    # Sum would be: (1+10) + (2+11) = 11 + 13 = 24
    assert sum_pairs_with_difference_nine(test_file_path) == 24
    
    # Clean up test file
    os.remove(test_file_path)