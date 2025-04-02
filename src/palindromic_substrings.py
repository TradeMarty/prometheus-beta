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
    
    # Find palindromes: single characters and longer
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            substring = s[start:start+length]
            if is_palindrome(substring):
                all_palindromes.add(substring)
    
    # Separate single and multi-character palindromes
    single_chars = {p for p in all_palindromes if len(p) == 1}
    multi_chars = sorted((p for p in all_palindromes if len(p) > 1), 
                         key=lambda x: (-len(x), x))
    
    # Select non-overlapping palindromes
    result = []
    used_indices = set()
    
    # Add multi-character palindromes first
    for palindrome in multi_chars:
        # Prefer longer palindromes
        indices = [i for i in range(n) if s.startswith(palindrome, i)]
        
        for start in indices:
            new_indices = set(range(start, start + len(palindrome)))
            
            # If no overlap with used indices, add and mark as used
            if not (new_indices & used_indices):
                result.append(palindrome)
                used_indices.update(new_indices)
                break
    
    # Add single characters that have not been used
    for char in sorted(single_chars):
        for i in range(n):
            if i not in used_indices and s[i] == char:
                result.append(char)
                used_indices.add(i)
                break
    
    # Sort and return
    return sorted(result)