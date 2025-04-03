def sum_pairs_with_difference_nine(file_path):
    """
    Read numbers from a text file and return the sum of all pairs of numbers 
    that have a difference of exactly 9.

    Args:
        file_path (str): Path to the text file containing numbers.

    Returns:
        int: Sum of all pairs of numbers with a difference of 9.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
        ValueError: If the file contains non-numeric content.
    """
    try:
        # Read numbers from the file
        with open(file_path, 'r') as file:
            # Split the file content and convert to integers
            numbers = [int(num.strip()) for num in file.read().split()]
        
        # Track the total sum of pairs
        total_sum = 0
        
        # Create a set for O(1) lookup
        number_set = set(numbers)
        
        # Find pairs with difference of 9
        for num in numbers:
            # Check if the complementary number exists
            # We look for num + 9 and num - 9
            if num + 9 in number_set:
                total_sum += num + (num + 9)
            
        # Divide by 2 to avoid double-counting pairs
        return total_sum // 2
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except ValueError:
        raise ValueError("File contains non-numeric content")