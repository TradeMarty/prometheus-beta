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
    used_indices = set()
    n = len(s)
    
    # First pass: find single character palindromes
    for i in range(n):
        if i not in used_indices:
            palindromes.add(s[i])
            used_indices.add(i)
    
    # Second pass: longer palindromes
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            substring = s[start:start+length]
            if is_palindrome(substring):
                # Check for overlap
                new_indices = set(range(start, start+length))
                
                # If no overlap with previously used indices
                if not (new_indices & used_indices):
                    # If this is the longest palindrome at this position
                    if length > 1:
                        palindromes.add(substring)
                        used_indices.update(new_indices)
    
    # Sort palindromes lexicographically
    return sorted(list(palindromes))