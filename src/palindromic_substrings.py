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
    
    # Find non-overlapping palindromic substrings
    palindromes = set()
    n = len(s)
    used_indices = set()
    
    # Check all possible substrings
    for start in range(n):
        if start in used_indices:
            continue
        
        for end in range(n, start, -1):
            substring = s[start:end]
            
            # Check if substring is a palindrome and doesn't use previously used indices
            if is_palindrome(substring) and len(substring) > 1:
                # Check for index overlap
                new_indices = set(range(start, end))
                if not (new_indices & used_indices):
                    palindromes.add(substring)
                    used_indices.update(new_indices)
                    break  # Stop after finding the longest non-overlapping palindrome
    
    # Add single character palindromes that weren't used
    for i in range(n):
        if i not in used_indices:
            palindromes.add(s[i])
    
    # Sort the palindromes lexicographically
    return sorted(list(palindromes))