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
    
    # Find all palindromes
    palindromes = set()
    n = len(s)
    
    # Find palindromes of all lengths
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            substring = s[start:start+length]
            if is_palindrome(substring):
                palindromes.add(substring)
    
    # Custom sorting that prefers single characters first
    def custom_sort(items):
        single_chars = sorted([x for x in items if len(x) == 1])
        multi_chars = sorted([x for x in items if len(x) > 1], 
                              key=lambda x: (len(x), x))
        return single_chars + multi_chars
    
    # Non-overlapping selection
    result = []
    used_indices = set()
    
    # Sort palindromes with custom sorting
    sorted_palindromes = custom_sort(palindromes)
    
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