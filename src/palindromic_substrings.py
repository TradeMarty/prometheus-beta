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
    
    # Find palindromes from longest to shortest to ensure non-overlapping
    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            substring = s[start:start+length]
            
            # Check if substring is a palindrome
            if is_palindrome(substring):
                # Check for index overlap
                new_indices = set(range(start, start+length))
                
                # If no overlap with previously used indices, add the palindrome
                if not (new_indices & used_indices):
                    palindromes.add(substring)
                    used_indices.update(new_indices)
    
    # Sort the palindromes lexicographically
    return sorted(list(palindromes))