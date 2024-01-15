#!/usr/bin/python3
def minOperations(n):
     """
    Calculate the minimum number of operations needed to obtain exactly n 'H' characters in a text file.

    Parameters:
    - n (int): The desired number of 'H' characters.

    Returns:
    - int: The minimum number of operations.

    If n is 1 or less, the file is already at the minimum size, so 0 operations are needed.
     """
    if n <= 1:
        return 0
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    # Calculate the minimun operations using the prime factors
    min_operations = sum(factors)
    return min_operations

