import pytest
from src.binary_search_tree import TreeNode, insert_node

def test_insert_empty_tree():
    """Test inserting into an empty tree"""
    root = None
    root = insert_node(root, 5)
    assert root is not None
    assert root.key == 5
    assert root.left is None
    assert root.right is None

def test_insert_left_subtree():
    """Test inserting a smaller value that goes to the left subtree"""
    root = TreeNode(10)
    root = insert_node(root, 5)
    assert root.left is not None
    assert root.left.key == 5

def test_insert_right_subtree():
    """Test inserting a larger value that goes to the right subtree"""
    root = TreeNode(10)
    root = insert_node(root, 15)
    assert root.right is not None
    assert root.right.key == 15

def test_insert_multiple_nodes():
    """Test inserting multiple nodes to create a more complex tree"""
    root = None
    values = [10, 5, 15, 3, 7, 12, 18]
    for val in values:
        root = insert_node(root, val)
    
    # Verify tree structure
    assert root.key == 10
    assert root.left.key == 5
    assert root.right.key == 15
    assert root.left.left.key == 3
    assert root.left.right.key == 7
    assert root.right.left.key == 12
    assert root.right.right.key == 18

def test_insert_duplicate():
    """Test that duplicate values are not inserted"""
    root = TreeNode(10)
    original_left = root.left
    original_right = root.right
    
    root = insert_node(root, 10)
    
    # Tree should remain unchanged
    assert root.key == 10
    assert root.left == original_left
    assert root.right == original_right

def test_insert_none_raises_error():
    """Test that inserting None raises a ValueError"""
    root = TreeNode(10)
    
    with pytest.raises(ValueError, match="Cannot insert None as a key"):
        insert_node(root, None)

def test_insert_handles_deep_tree():
    """Test inserting into a deeper tree"""
    root = None
    values = [100, 50, 150, 25, 75, 125, 175, 12, 37, 62, 87, 112, 137, 162, 187]
    
    for val in values:
        root = insert_node(root, val)
    
    # Spot check some values to ensure they're in the correct positions
    assert root.key == 100
    assert root.left.key == 50
    assert root.right.key == 150
    assert root.left.left.key == 25
    assert root.left.right.key == 75