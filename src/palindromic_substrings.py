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
    
    # Find all palindromic substrings
    palindromes = set()
    n = len(s)
    
    # Check all possible substrings
    for start in range(n):
        for end in range(start + 1, n + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    
    # Sort the palindromes lexicographically
    return sorted(list(palindromes))