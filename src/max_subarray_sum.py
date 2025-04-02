def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray of length k in the given list.
    
    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray to find maximum sum
    
    Returns:
        list: Subarray with maximum sum, or empty list if k > len(arr)
    
    Raises:
        TypeError: If inputs are not of the correct type
        ValueError: If k is negative
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Validate k
    if k < 0:
        raise ValueError("k cannot be negative")
    
    # If k is larger than list length, return empty list
    if k > len(arr):
        return []
    
    # If k is 0, return empty list
    if k == 0:
        return []
    
    # Handle empty list case
    if not arr:
        return []
    
    # Sliding window approach
    # Initialize the first window sum
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Slide the window and update max sum
    for i in range(k, len(arr)):
        # Remove the first element of previous window and add new element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum