#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest # of operations.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""
def minOperations(n):
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

