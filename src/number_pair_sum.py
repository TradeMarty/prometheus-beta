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
        
        # Use a set for O(1) lookup
        number_set = set(numbers)
        
        # Keep track of used pairs to avoid double-counting
        used_pairs = set()
        
        # Find pairs with difference of 9
        for num in numbers:
            # Check pairs (num, num+9) and (num, num-9)
            complement1 = num + 9
            complement2 = num - 9
            
            # Check complement1
            if complement1 in number_set:
                # Sort the pair to create a unique identifier 
                pair = tuple(sorted((num, complement1)))
                if pair not in used_pairs:
                    total_sum += num + complement1
                    used_pairs.add(pair)
            
            # Check complement2
            if complement2 in number_set:
                # Sort the pair to create a unique identifier
                pair = tuple(sorted((num, complement2)))
                if pair not in used_pairs:
                    total_sum += num + complement2
                    used_pairs.add(pair)
        
        return total_sum
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except ValueError:
        raise ValueError("File contains non-numeric content")