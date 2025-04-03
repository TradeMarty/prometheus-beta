def calculate_weighted_sum(numbers, weights):
    """
    Compute the total weighted sum of a list of numbers using their corresponding weights.

    Args:
        numbers (list): A list of numeric values to be weighted.
        weights (list): A list of weights corresponding to the numbers.

    Returns:
        float: The total weighted sum.

    Raises:
        ValueError: If the lengths of numbers and weights lists do not match,
                    or if either list is empty, or if non-numeric values are provided.
    """
    # Validate input
    if not numbers or not weights:
        raise ValueError("Both numbers and weights lists must be non-empty")
    
    if len(numbers) != len(weights):
        raise ValueError("The length of numbers and weights must be the same")
    
    # Validate that all inputs are numeric
    try:
        numbers = [float(num) for num in numbers]
        weights = [float(weight) for weight in weights]
    except (TypeError, ValueError):
        raise ValueError("All numbers and weights must be numeric")
    
    # Calculate weighted sum
    weighted_sum = sum(num * weight for num, weight in zip(numbers, weights))
    
    return weighted_sum