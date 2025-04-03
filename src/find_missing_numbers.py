def find_missing_numbers(arr):
    """
    Find and return all the numbers that are missing from a given array of unique integers.
    
    Args:
        arr (list): A list of unique integers.
    
    Returns:
        list: A sorted list of missing numbers in the range from the minimum to the maximum of the input array.
    
    Raises:
        ValueError: If the input array is empty or None.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input validation
    if arr is None:
        raise ValueError("Input array cannot be None")
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Ensure all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Create a set of the input array for O(1) lookup
    arr_set = set(arr)
    
    # Find missing numbers
    missing_numbers = [
        num for num in range(min_val, max_val + 1) 
        if num not in arr_set
    ]
    
    return missing_numbers