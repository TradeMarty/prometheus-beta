def find_primes_below_n(n):
    """
    Find all prime numbers below a given number n using the Sieve of Eratosthenes algorithm.
    
    Args:
        n (int): The upper limit (exclusive) for finding prime numbers.
    
    Returns:
        list: A sorted list of prime numbers strictly less than n.
    
    Raises:
        ValueError: If n is less than 2.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        return []
    
    # Create a boolean array "is_prime[0..n]" and initialize all entries as true
    # A value in is_prime[i] will be false if i is not a prime, else true
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, n, i):
                is_prime[j] = False
    
    # Collect prime numbers
    return [num for num in range(2, n) if is_prime[num]]