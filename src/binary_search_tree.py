class TreeNode:
    """
    Represents a node in a Binary Search Tree.
    
    Attributes:
        key: The value stored in the node
        left: Left child node (smaller values)
        right: Right child node (larger values)
    """
    def __init__(self, key):
        """
        Initialize a new TreeNode.
        
        Args:
            key: The value to be stored in the node
        """
        self.key = key
        self.left = None
        self.right = None

def insert_node(root, key):
    """
    Insert a new node with the given key into the binary search tree.
    
    Args:
        root (TreeNode): The root of the binary search tree
        key: The value to be inserted
    
    Returns:
        TreeNode: The root of the modified binary search tree
    
    Raises:
        ValueError: If the key is None
    """
    # Validate input
    if key is None:
        raise ValueError("Cannot insert None as a key")
    
    # If the tree is empty, create a new root node
    if root is None:
        return TreeNode(key)
    
    # Recursive insertion
    if key < root.key:
        # Insert into left subtree
        root.left = insert_node(root.left, key)
    elif key > root.key:
        # Insert into right subtree
        root.right = insert_node(root.right, key)
    # If key is equal, we don't insert duplicates (BST property)
    
    return root