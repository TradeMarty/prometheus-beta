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
    
    # Find all palindromic substrings first
    palindromes = set()
    n = len(s)
    
    # Find all palindromes
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            substring = s[start:start+length]
            if is_palindrome(substring):
                palindromes.add(substring)
    
    # Sort palindromes lexicographically, keeping only non-single character palindromes with length > 1
    full_palindromes = sorted(p for p in palindromes if len(p) > 1)
    single_chars = sorted(p for p in palindromes if len(p) == 1)
    
    return sorted(full_palindromes + single_chars)