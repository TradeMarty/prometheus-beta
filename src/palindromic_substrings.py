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
    
    # Find all possible palindromes first
    all_palindromes = set()
    n = len(s)
    
    # Find all palindromes
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            substring = s[start:start+length]
            if is_palindrome(substring):
                all_palindromes.add(substring)
    
    # Sort palindromes by length (descending) and lexicographically
    sorted_palindromes = sorted(all_palindromes, key=lambda x: (-len(x), x))
    
    # Select non-overlapping palindromes
    result = []
    used_indices = set()
    
    for palindrome in sorted_palindromes:
        # Check if this palindrome overlaps with used indices
        new_indices = set(range(s.index(palindrome), s.index(palindrome) + len(palindrome)))
        
        # If no overlap, add to result and mark indices as used
        if not (new_indices & used_indices):
            result.append(palindrome)
            used_indices.update(new_indices)
    
    # Sort result lexicographically
    return sorted(result)