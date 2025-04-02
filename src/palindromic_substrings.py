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
    
    # Special cases: whole string and local palindromes
    if is_palindrome(s):
        palindromes.add(s)
    
    # Find single characters, shorter palindromes, and longer palindromes
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            substring = s[start:start+length]
            
            # Only add if palindrome and not previously added
            if is_palindrome(substring):
                palindromes.add(substring)
    
    # Create a list of palindromes, ensuring non-overlapping
    result = []
    used_indices = set()
    
    # Sort palindromes by length first (then lexicographically)
    # This helps us prefer longer palindromes
    sorted_palindromes = sorted(palindromes, key=lambda x: (-len(x), x))
    
    for palindrome in sorted_palindromes:
        # Find indices of this palindrome in original string
        indices = [i for i in range(n) if s.startswith(palindrome, i)]
        
        # Check each potential starting index for overlap
        for start in indices:
            new_indices = set(range(start, start + len(palindrome)))
            
            # If no overlap with used indices, add palindrome
            if not (new_indices & used_indices):
                result.append(palindrome)
                used_indices.update(new_indices)
                break
    
    # Sort lexicographically as final step
    return sorted(result)