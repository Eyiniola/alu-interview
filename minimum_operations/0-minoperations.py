#!/usr/bin/python3
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
# Example use 
n = 9
result = minOperations(n)
print(f"The minimum number of operations for n={n} is: {result}")

