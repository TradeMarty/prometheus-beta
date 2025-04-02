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
    
    # First find the whole string palindrome
    if is_palindrome(s):
        palindromes.add(s)
    
    # Find the single character and multi-character non-overlapping palindromes
    used_indices = set()
    
    # First look for single characters
    for i in range(n):
        if i not in used_indices:
            used_indices.add(i)
            palindromes.add(s[i])
    
    # Then look for palindromic substrings of different lengths
    lengths = sorted(range(2, n+1), reverse=True)
    for length in lengths:
        for start in range(n - length + 1):
            substring = s[start:start+length]
            
            # Check if substring is a palindrome
            if is_palindrome(substring):
                # Check indices
                new_indices = set(range(start, start+length))
                
                # Check no overlap with used indices
                if not (new_indices & used_indices):
                    palindromes.add(substring)
                    used_indices.update(new_indices)
    
    # Find some local small palindromes like 'bcb'
    for length in range(3, n+1):
        for start in range(n - length + 1):
            substring = s[start:start+length]
            
            # Ensure it's a palindrome but not the whole string
            if is_palindrome(substring) and substring != s:
                palindromes.add(substring)
    
    # Sort palindromes lexicographically
    return sorted(list(palindromes))