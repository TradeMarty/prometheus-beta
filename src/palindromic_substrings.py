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
    
    # Specific functions to handle various requirements
    def can_add_palindrome(substring, start):
        """Check if palindrome can be added without overlapping."""
        new_indices = set(range(start, start + len(substring)))
        return len(substring) > 1 and not (new_indices & used_indices)
    
    # Prefer longer and then lexicographically earlier palindromes
    palindrome_lengths = sorted(range(2, n+1), reverse=True)
    
    # First find the longest possible palindromes
    for length in palindrome_lengths:
        for start in range(n - length + 1):
            substring = s[start:start+length]
            
            # Check if substring is a full string palindrome
            if is_palindrome(substring) and substring == s:
                palindromes.add(substring)
                used_indices.update(range(start, start+length))
                break
    
    # Then find local non-overlapping palindromes
    for length in palindrome_lengths + [1]:
        for start in range(n):
            for end in range(start + length, n + 1):
                substring = s[start:end]
                
                # Skip whole string palindrome (already handled)
                if substring == s:
                    continue
                
                # Check if palindrome and can be added
                if is_palindrome(substring):
                    # Try to add subject to non-overlap constraint
                    start_index = s.index(substring, start)
                    if can_add_palindrome(substring, start_index):
                        palindromes.add(substring)
                        used_indices.update(range(start_index, start_index + len(substring)))
    
    # Add single characters not used
    for i in range(n):
        if i not in used_indices:
            palindromes.add(s[i])
    
    # Sort to match specific lexicographic expectations
    return sorted(list(palindromes))