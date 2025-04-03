def reverse_words_and_characters(input_string: str) -> str:
    """
    Reverse the order of words in a string and reverse the characters of each word.
    
    Args:
        input_string (str): The input string to be transformed
    
    Returns:
        str: A string with words in reverse order and each word's characters reversed
    
    Examples:
        >>> reverse_words_and_characters("Hello World")
        'dlroW olleH'
        >>> reverse_words_and_characters("Python is awesome")
        'emosewa si nohtyP'
        >>> reverse_words_and_characters("")
        ''
    """
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string into words, reverse the order, 
    # then reverse characters of each word
    reversed_words = input_string.split()[::-1]
    reversed_words_and_chars = [word[::-1] for word in reversed_words]
    
    # Join the transformed words back into a string
    return " ".join(reversed_words_and_chars)