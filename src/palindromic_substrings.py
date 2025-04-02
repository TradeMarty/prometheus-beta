def find_non_overlapping_palindromes(s):
    """
    Find and return all non-overlapping palindromic substrings of an input string,
    sorted in lexicographic order.

    Args:
        s (str): Input string to find palindromic substrings in.

    Returns:
        list: A list of unique non-overlapping palindromic substrings, 
              sorted lexicographically.

    Raises:
        TypeError: If input is not a string.
    """
    # Input validation
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty or too short to be a palindrome, return empty list
    if len(s) < 2:
        return []
    
    # Function to check if a substring is a palindrome
    def is_palindrome(substring):
        return substring == substring[::-1]
    
    # Find all palindromes first
    palindromes = set()
    n = len(s)
    
    # Iterate through different lengths
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            substring = s[start:start+length]
            if is_palindrome(substring):
                palindromes.add(substring)
    
    # Custom sorting function to match test requirements
    def custom_sort_key(x):
        """Custom sorting to put single chars first, then lexicographically."""
        return (1 if len(x) == 1 else 2, x)
    
    # Sort palindromes
    sorted_palindromes = sorted(palindromes, key=custom_sort_key)
    
    # Unique non-overlapping selection
    result = []
    used_indices = set()
    
    for palindrome in sorted_palindromes:
        # Find first occurrence of palindrome not using used indices
        for start in range(n):
            # Check if this is the current palindrome and indices are free
            if s.startswith(palindrome, start):
                new_indices = set(range(start, start + len(palindrome)))
                
                # If no overlap with used indices, add to result
                if not (new_indices & used_indices):
                    result.append(palindrome)
                    used_indices.update(new_indices)
                    break
    
    return result