def search_matrix(matrix, target):
    """
    Search for a target value in a sorted matrix with specific constraints.
    
    The matrix has the following properties:
    - Each row is sorted in ascending order from left to right
    - The first integer of each row is greater than the last integer of the previous row
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The value to search for
    
    Returns:
        bool: True if target is found in the matrix, False otherwise
    
    Time Complexity: O(log(m*n)), where m is the number of rows and n is the number of columns
    Space Complexity: O(1)
    
    Raises:
        TypeError: If input is not a valid matrix or target is not an integer
        ValueError: If matrix is empty
    """
    # Validate input
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check matrix validity
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("Matrix must be a 2D list")
        if not all(isinstance(x, int) for x in row):
            raise TypeError("Matrix must contain only integers")
    
    # Perform binary search across the entire matrix
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D matrix coordinates
        row = mid // n
        col = mid % n
        
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False