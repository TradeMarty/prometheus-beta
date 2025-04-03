def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings using dynamic programming.
    
    A subsequence is a sequence that can be derived from another sequence by deleting 
    some or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Type checking
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Convert to same case for case-sensitive comparison
    str1, str2 = str1.lower(), str2.lower()
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Compute maximum length of LCS and create backtracking table
    max_length = 0
    end_index = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
    
    # If no common subsequence found, return empty string
    if max_length == 0:
        return ""
    
    # Reconstruct the LCS
    lcs = []
    i, j = end_index, max_length
    while j > 0:
        lcs.append(str1[i-1])
        i -= 1
        j -= 1
    
    # Return reversed LCS (built from end to start)
    return ''.join(reversed(lcs))